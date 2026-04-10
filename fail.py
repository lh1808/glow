20:17:13 INFO [rubin.analysis] Base-Learner-Tuning: 5 Tasks abgeschlossen (80 Trials/Task). Ø Score: -0.142223
20:24:50 INFO [rubin.analysis] FMT R-Score: final__DRLearner → 0.00687681
20:24:50 INFO [rubin.analysis] FMT R-Score: final__DRLearner__penalized → 0.00687681
20:24:50 INFO [rubin.analysis] FMT R-Score: final__NonParamDML → -9.94688e-10
20:24:50 INFO [rubin.analysis] FMT R-Score: final__NonParamDML__penalized → -9.94688e-10
20:24:51 INFO [rubin.analysis] [rubin] Step 4/8: Training & Cross-Predictions
20:24:51 INFO [rubin.training] TLearner: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
20:25:04 INFO [rubin.analysis]   TLearner: Training + Cross-Predictions in 13.4s
20:25:05 INFO [rubin.analysis] Predictions_TLearner: CATE min=-0.0385555, median=0.000523753, max=0.0460212, std=0.00183503, unique=282414/389988, non-zero=389988/389988
20:25:05 INFO [rubin.analysis] DRLearner model_final effektive Params: {'n_estimators': 125, 'num_leaves': 20, 'max_depth': 6, 'min_child_samples': 192, 'min_child_weight': 2.8544878229795287, 'colsample_bytree': 0.6648816776009254, 'reg_alpha': 5.265609152796357, 'reg_lambda': 5.672363044043851, 'path_smooth': 19.366643725166636} (explicit_tuned=ja, fmt_fixed=False)
20:25:06 INFO [rubin.training] DRLearner: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
20:26:41 INFO [rubin.analysis]   DRLearner: Training + Cross-Predictions in 95.5s
20:26:42 WARNING [rubin.analysis] WARNUNG: Predictions_DRLearner hat nur 5 distinkte Werte bei 5 Folds (Range=1.49e-05, Mean=8.49e-04). Das CATE-Modell ist wahrscheinlich zu einem Intercept kollabiert. Empfehlungen: (1) final_model_tuning.enabled=true aktivieren, (2) Prüfen ob base_fixed_params zu restriktiv sind (min_child_samples, num_leaves, max_depth), (3) Mehr Features oder Feature-Engineering.
20:26:42 INFO [rubin.analysis] NonParamDML model_final effektive Params: {'n_estimators': 183, 'num_leaves': 37, 'max_depth': 4, 'min_child_samples': 289, 'min_child_weight': 37.07453147796602, 'colsample_bytree': 0.39719916752787854, 'reg_alpha': 0.7350436975818627, 'reg_lambda': 1.3372199191016219, 'path_smooth': 4.854199076354936} (explicit_tuned=ja, fmt_fixed=False)
20:26:43 INFO [rubin.training] NonParamDML: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
20:28:49 INFO [rubin.analysis]   NonParamDML: Training + Cross-Predictions in 127.2s
20:28:50 WARNING [rubin.analysis] WARNUNG: Predictions_NonParamDML hat nur 5 distinkte Werte bei 5 Folds (Range=2.16e-05, Mean=8.49e-04). Das CATE-Modell ist wahrscheinlich zu einem Intercept kollabiert. Empfehlungen: (1) final_model_tuning.enabled=true aktivieren, (2) Prüfen ob base_fixed_params zu restriktiv sind (min_child_samples, num_leaves, max_depth), (3) Mehr Features oder Feature-Engineering.
20:28:51 INFO [rubin.training] XLearner: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
20:29:32 INFO [rubin.analysis]   XLearner: Training + Cross-Predictions in 41.7s
20:29:33 INFO [rubin.analysis] Predictions_XLearner: CATE min=-0.029876, median=0.000633762, max=0.0375046, std=0.00120217, unique=369518/389988, non-zero=389988/389988
20:29:34 INFO [rubin.training] ParamDML: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
20:31:05 INFO [rubin.analysis]   ParamDML: Training + Cross-Predictions in 91.4s
20:31:06 INFO [rubin.analysis] Predictions_ParamDML: CATE min=-0.0492972, median=0.000682022, max=0.0320619, std=0.00221818, unique=389448/389988, non-zero=389988/389988
21:58:37 INFO [rubin.analysis] CausalForestDML EconML tune(): train=311990 Beobachtungen. Wald-Parameter optimiert.
21:58:38 INFO [rubin.training] CausalForestDML: Erzwinge sequentielle Folds (GRF nutzt intern joblib-Prozesse, die in Threads zu Deadlocks führen).
21:58:38 INFO [rubin.training] CausalForestDML: 5 Folds sequentiell.
03:20:38 INFO [rubin.analysis]   CausalForestDML: Training + Cross-Predictions in 24571.5s
03:20:38 INFO [rubin.analysis] Predictions_CausalForestDML: CATE min=-0.00251592, median=0.000734282, max=0.0197453, std=0.000629298, unique=389444/389988, non-zero=389988/389988
Traceback (most recent call last):
  File "/mnt/rubin/run_analysis.py", line 132, in <module>
    main()
  File "/mnt/rubin/run_analysis.py", line 128, in main
    pipe.run(export_bundle=args.export_bundle, bundle_dir=args.bundle_dir, bundle_id=args.bundle_id)
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 2737, in run
    models, preds, fold_models = self._run_training(cfg, X, T, Y, tuned_params_by_model, holdout_data, mlflow)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 641, in _run_training
    model = self.registry.create(name, ctx)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/model_registry.py", line 174, in create
    return self._factories[name](ctx)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/model_registry.py", line 314, in <lambda>
    lambda ctx: CausalForestAdapter(
                ^^^^^^^^^^^^^^^^^^^^
TypeError: Can't instantiate abstract class CausalForestAdapter without an implementation for abstract method 'marginal_effect'
