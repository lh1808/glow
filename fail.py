Pipeline-Logs
59 Zeilen
Ausblenden
[rubin] Step 1/8: Daten laden & Preprocessing
[rubin] Step 2/8: Feature-Selektion
[rubin] Step 3/8: Base-Learner-Tuning
[rubin] Step 4/8: Training & Cross-Predictions
[rubin] Step 5/8: Evaluation & Metriken
17:16:54 INFO [rubin.analysis] MLflow-Experiment 'rubin_WG_all' (identisch mit DataPrep).
17:16:54 INFO [rubin.analysis] Run-Name-Suffix 'grüner-sperber' aus DataPrep übernommen.
17:16:54 INFO [rubin.analysis] DataPrep-Config nach MLflow geloggt: /mnt/rubin/data/processed/dataprep_config.yml
17:16:54 INFO [rubin.analysis] [rubin] Step 1/8: Daten laden & Preprocessing
17:16:54 INFO [rubin.analysis] Historischer Score: 5 NaN-Werte durch 0 ersetzt.
17:16:56 INFO [rubin.analysis] Memory-Reduktion: 1085.7 MB → 1039.3 MB (4% gespart).
17:16:56 INFO [rubin.analysis] Daten geladen: X=(389988, 696), T=(389988,) (unique=[0, 1]), Y=(389988,) (unique=[0, 1]), S=(389988,)
17:16:57 INFO [rubin.analysis] [rubin] Step 2/8: Feature-Selektion
17:16:57 INFO [rubin.feature_selection] Feature-Selektion: 2 Methoden sequentiell (alle Kerne pro Methode).
17:20:28 INFO [rubin.feature_selection] CausalForest FS: X=(389988, 696) (dtypes: 696 numeric, 0 category), T=(389988,) (unique=2), Y=(389988,), n_jobs=-1, in_thread=False
17:20:29 INFO [rubin.feature_selection] CausalForest FS: Subsampling 389988 → 99999 Zeilen (stratifiziert nach T).
17:20:29 INFO [rubin.feature_selection] CausalForest FS: fit(99999×696, T unique=2, n_estimators=100, n_jobs=-1)...
17:34:15 INFO [rubin.feature_selection] Korrelationsfilter (|r| > 0.90, importance-gesteuert): 293 Features entfernt, 403 verbleiben.
17:34:16 INFO [rubin.analysis] Importance-Umverteilung: 293 entfernte Features → Importance auf Partner übertragen.
17:34:16 INFO [rubin.feature_selection] Feature-Selection 'lgbm_importance': Top-15% = 61 / 403 Features.
17:34:16 INFO [rubin.feature_selection] Feature-Selection 'causal_forest': Top-15% = 61 / 403 Features.
17:34:16 INFO [rubin.feature_selection] Feature-Selection Union: 82 / 403 Features behalten, 321 entfernt.
17:34:16 INFO [rubin.analysis] Feature-Selektion gesamt: 696 → 82 Features (Korrelation: −293, Importance: −321)
17:34:16 INFO [rubin.analysis] [rubin] Step 3/8: Base-Learner-Tuning
17:34:16 INFO [rubin.analysis] Starte Tuning: X=(389988, 82), Y=(389988,) (unique=[0, 1]), T=(389988,) (unique=[0, 1])
17:34:16 INFO [rubin.tuning] tune_all gestartet: models=['NonParamDML', 'CausalForest', 'CausalForestDML', 'ParamDML'], X=(389988, 82), Y=(389988,) (unique=[0, 1]), T=(389988,) (unique=[0, 1]), cv_splits=5, n_trials=30, parallel_trials=16
17:34:17 INFO [rubin.tuning] Tuning-Task 'catboost__outcome__classifier__all__no_t__y': X_input=389988 rows, indices=389988, X_task=(389988, 82), target=(389988,) (unique=[0, 1]), T_task unique=[0, 1], cv_splits=5, target_name=Y, objective=outcome
17:35:20 INFO [rubin.tuning] Tuning-Task 'catboost__propensity__classifier__all__no_t__t': X_input=389988 rows, indices=389988, X_task=(389988, 82), target=(389988,) (unique=[0, 1]), T_task unique=[0, 1], cv_splits=5, target_name=T, objective=propensity
17:40:34 INFO [rubin.analysis] [rubin] Step 4/8: Training & Cross-Predictions
17:40:34 INFO [rubin.analysis] NonParamDML model_final effektive Params: {'iterations': 135, 'depth': 3, 'l2_leaf_reg': 50.58586054053267, 'rsm': 0.3937706093913401, 'min_data_in_leaf': 468, 'model_size_reg': 2.16672830207965} (explicit_tuned=ja, fmt_fixed=False)
17:40:34 INFO [rubin.training] NonParamDML: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
17:43:19 INFO [rubin.analysis] Predictions_NonParamDML: CATE min=-0.0939672, median=0.000778542, max=0.0199976, std=0.000746284, unique=386447/389988, non-zero=389988/389988
17:54:37 INFO [rubin.analysis] CausalForest Tune: 12 Kombis auf Fold 1 (train=311990, val=77998) → best={'min_samples_leaf': 5, 'max_depth': 10, 'max_samples': 0.5}, R-Loss=0.00189376
17:54:37 INFO [rubin.training] CausalForest: Erzwinge sequentielle Folds (GRF nutzt intern joblib-Prozesse, die in Threads zu Deadlocks führen).
17:54:37 INFO [rubin.training] CausalForest: 5 Folds sequentiell.
18:01:27 INFO [rubin.analysis] Predictions_CausalForest: CATE min=-0.0279995, median=0.00062925, max=0.0420871, std=0.00128431, unique=389448/389988, non-zero=389988/389988
18:05:46 INFO [rubin.training] CausalForestDML: Erzwinge sequentielle Folds (GRF nutzt intern joblib-Prozesse, die in Threads zu Deadlocks führen).
18:05:46 INFO [rubin.training] CausalForestDML: 5 Folds sequentiell.
18:13:36 INFO [rubin.analysis] Predictions_CausalForestDML: CATE min=-0.00452092, median=0.000716851, max=0.0200235, std=0.000636807, unique=389422/389988, non-zero=389988/389988
18:13:37 INFO [rubin.training] ParamDML: 5 Folds parallel (n_jobs=5, threads) auf 64 Kernen.
18:16:30 INFO [rubin.analysis] Predictions_ParamDML: CATE min=-0.0451928, median=0.000676918, max=0.0305543, std=0.00220734, unique=389448/389988, non-zero=389988/389988
18:16:30 WARNING [rubin.analysis] Ensemble-Erstellung fehlgeschlagen.
Traceback (most recent call last):
  File "/mnt/rubin/rubin/pipelines/analysis_pipeline.py", line 2698, in run
    ensemble_model = EnsembleCateEstimator(
                     ^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/rubin/.pixi/envs/default/lib/python3.12/site-packages/econml/score/ensemble_cate.py", line 29, in __init__
    self.cate_models = cate_models
    ^^^^^^^^^^^^^^^^
  File "/mnt/rubin/.pixi/envs/default/lib/python3.12/site-packages/econml/score/ensemble_cate.py", line 57, in cate_models
    raise ValueError('Parameter `cate_models` should be a list of `BaseCateEstimator` objects.')
ValueError: Parameter `cate_models` should be a list of `BaseCateEstimator` objects.
18:16:30 INFO [rubin.analysis] [rubin] Step 5/8: Evaluation & Metriken
18:16:49 INFO [rubin.analysis] DRTester Nuisance einmalig gefittet (BT, cv=3, n_est≤100). Wird für alle Modelle wiederverwendet.
