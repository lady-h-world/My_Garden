from scipy import stats
from scipy.spatial import distance

import matplotlib.pyplot as plt
import seaborn as sns

from psi import calculate_psi


def get_ks_score(df, group_col, feature, group_values=[0, 1]):
    """
    When `alternative` is set as "two-sided", the null hypothesis is,
    "the two distributions are identical".
    When output p-value is larger than than significance level (0.05 by default),
    we can't reject the null hypothesis.
    """
    s1 = df[df[group_col] == group_values[0]][feature].values
    s2 = df[df[group_col] == group_values[1]][feature].values
    ks = stats.ks_2samp(s1, s2, alternative='two-sided', method='exact')[1]

    return ks


def get_psi_score(df, group_col, feature, group_values=[0, 1]):
    """
    Calculate the PSI (population stability index) across all variables:
        PSI < 0.1: no significant population change
        0.1 <= PSI < 0.2: moderate population change
        PSI >= 0.2: significant population change

    Larger PSI value indicates larger difference between the distributions.
    """
    s1 = df[df[group_col] == group_values[0]][feature].values
    s2 = df[df[group_col] == group_values[1]][feature].values
    psi = calculate_psi(s1, s2, buckettype='quantiles', buckets=100, axis=1)

    return psi


def plot_num_feature_distribution_per_group(grouped_df, group_col, n_rows, n_cols, exclude_cols=[],
                                            figsize=[20, 10], font_scale=1, group_values=[0, 1],
                                            bins=100, palette=["red", "blue", "green"],
                                            distribution_metrics='psi',  # choose 'psi' or 'ks'
                                            enable_dist_comp=True
                                            ):
    sns.set(font_scale=font_scale)
    f, axes = plt.subplots(n_rows, n_cols, figsize=(figsize[0], figsize[1]))

    features = [col for col in grouped_df.columns if col not in exclude_cols]
    for ax, feature in zip(axes.flat, features):
        if enable_dist_comp:
            if distribution_metrics == 'psi':
                psi = get_psi_score(grouped_df[[feature, group_col]],
                                    group_col, feature, group_values=group_values)
                ax.set_title(f'PSI: {psi}')
            else:
                ks = get_ks_score(grouped_df[[feature, group_col]],
                                  group_col, feature, group_values=group_values)
                ax.set_title(f'KS: {ks}')

        sns.histplot(grouped_df, x=feature,
                     hue=group_col, ax=ax,
                     stat='density', palette=palette, bins=bins)


def make_cat2proba(df, feature, group_col):
    class_ct_df = df[[feature, group_col]] \
        .groupby([feature, group_col], as_index=False)[group_col] \
        .agg(['count']).reset_index()
    class_ct_df['perct'] = round(class_ct_df['count'] * 100 / len(df), 2)

    return class_ct_df


def get_js_dist(feature_group_perct_df, group_col, feature, group_values):
    """
    Get Jensen-Shannon distance, it's a value between [0, 1].
    0 JS score means idential; 1 JS means absolute different.
    """
    s1 = feature_group_perct_df[feature_group_perct_df[group_col] == group_values[0]]['perct'].values
    s2 = feature_group_perct_df[feature_group_perct_df[group_col] == group_values[1]]['perct'].values
    js_dist = distance.jensenshannon(s1, s2)

    return js_dist


def plot_cat_feature_distribution_per_group(grouped_df, group_col, n_rows, n_cols,
                                            exclude_cols=[], figsize=[40, 20], group_values=[0, 1],
                                            font_size=20, palette=['green', 'red', 'orange'],
                                            enable_dist_comp=True):
    plt.rcParams.update({'font.size': font_size})

    feature_df = grouped_df.copy()
    feature_df = feature_df.astype('str').fillna('NA')
    features = feature_df.columns

    i = 0
    fig = plt.figure(figsize=(figsize[0], figsize[1]))
    for feature in features:
        if feature in exclude_cols:
            continue
        i += 1
        ax = fig.add_subplot(n_rows, n_cols, i)
        axes = plt.gca()

        class_ct_df = make_cat2proba(feature_df, feature, group_col)

        if enable_dist_comp:
            js_dist = get_js_dist(class_ct_df, group_col, feature, group_values)
            ax.set_title(f'JS Distance: {js_dist}')

        ax = sns.barplot(x=feature, hue=group_col, y='perct', data=class_ct_df, palette=palette)
        plt.xticks(rotation=45, ha="right")
        for container in ax.containers:
            ax.bar_label(container)
    fig.tight_layout()
    plt.show()
