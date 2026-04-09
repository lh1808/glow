16:41:40 INFO [rubin.training] CausalForestDML: 5 Folds sequentiell.
16:47:12 INFO [rubin.analysis] Predictions_CausalForestDML: CATE min=-0.0056871, median=0.000717207, max=0.0216319, std=0.000670701, unique=389418/389988, non-zero=389988/389988
16:47:13 INFO [rubin.training] ParamDML: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
16:49:00 INFO [rubin.analysis] Predictions_ParamDML: CATE min=-0.0464705, median=0.000677872, max=0.0312632, std=0.00219879, unique=389449/389988, non-zero=389988/389988
Traceback (most recent call last):
  File "/mnt/rubin/run_analysis.py", line 132, in <module>
    main()
  File "/mnt/rubin/run_analysis.py", line 128, in main
    pipe.run(export_bundle=args.export_bundle, bundle_dir=args.bundle_dir, bundle_id=args.bundle_id)
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 2657, in run
    models, preds, fold_models = self._run_training(cfg, X, T, Y, tuned_params_by_model, holdout_data, mlflow)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 608, in _run_training
    model = self.registry.create(name, ctx)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/model_registry.py", line 171, in create
    return self._factories[name](ctx)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/model_registry.py", line 310, in <lambda>
    lambda ctx: CausalForestAdapter(
                ^^^^^^^^^^^^^^^^^^^^
TypeError: rubin.model_registry.CausalForestAdapter() got multiple values for keyword argument 'n_jobs'
