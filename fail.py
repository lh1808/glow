12:17:16 INFO [rubin.analysis] Ensemble erstellt (EconML EnsembleCateEstimator): 3 Modelle gleichgewichtet (CausalForestDML, ParamDML, NonParamDML).
12:17:16 INFO [rubin.analysis] [rubin] Step 5/6: Evaluation & Metriken
12:17:38 INFO [rubin.analysis] DRTester Nuisance einmalig gefittet (BT, cv=3, n_est≤100). Wird für alle Modelle wiederverwendet.
12:17:39 INFO [rubin.analysis] Evaluation Predictions_CausalForestDML: n=389988, min=-0.000892275, median=0.00075225, max=0.0089181, std=0.000325844, non-zero=389988/389988, unique=999
12:17:39 INFO [rubin.analysis] Evaluation Predictions_ParamDML: n=389988, min=-0.0479861, median=0.000676784, max=0.0316661, std=0.00221398, non-zero=389988/389988, unique=999
12:17:40 INFO [rubin.analysis] Evaluation Predictions_NonParamDML: n=389988, min=-0.0178867, median=0.000804738, max=0.014292, std=0.000443451, non-zero=389988/389988, unique=999
12:17:40 WARNING [rubin.analysis] Uplift-Evaluation fehlgeschlagen.
Traceback (most recent call last):
  File "/mnt/rubin/.pixi/envs/default/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Y'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 2685, in run
    eval_summary, _, fitted_tester_bt = self._run_evaluation(cfg, X, T, Y, S, holdout_data, preds, models, tuned_params_by_model, mlflow, eval_mask=eval_mask)
                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 920, in _run_evaluation
    y = dfp["Y"].to_numpy()
        ~~~^^^^^
  File "/mnt/rubin/.pixi/envs/default/lib/python3.12/site-packages/pandas/core/frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/.pixi/envs/default/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'Y'
12:17:41 INFO [rubin.analysis] RAM-Optimierung: gc.collect() nach Surrogate.
12:17:41 INFO [rubin.analysis] RAM-Optimierung: Modelle, Predictions und X_full freigegeben.
12:17:41 INFO [rubin.analysis] [rubin] Step 6/6: HTML-Report
12:17:41 INFO [rubin.reporting] HTML-Report geschrieben: /mnt/rubin/.rubin_cache/analysis_report.html
12:17:41 INFO [rubin.analysis] HTML-Report geschrieben: /mnt/rubin/.rubin_cache/analysis_report.html
