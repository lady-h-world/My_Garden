from zenml.core.repo import Repository

repo = Repository()
p = repo.get_pipeline(pipeline_name="super_mini_pipeline")
runs = p.runs
print(f"Pipeline `super_mini_pipeline` has {len(runs)} run(s)")
run = runs[-1]
print(f"The run you just made has {len(run.steps)} steps.")
step = run.get_step('train_evaltor')
print(f"The `train_evaltor` step has {len(step.outputs)} output artifacts.")
for k, o in step.outputs.items():
    performance = o.read()
    print(f"Output performance is {performance}")
