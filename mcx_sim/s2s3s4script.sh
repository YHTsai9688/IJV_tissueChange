#python S2_make_simfile.py "ctchen_1e9_ijv_small_to_large" 1000000000
#python S3_run_sim.py "ctchen_1e9_ijv_small_to_large" 1  1225
#python S4_wmc_generate_dataset.py "ctchen_dataset_small" "ctchen_1e9_ijv_small_to_large" 1 1225
#python S2_make_simfile.py "ctchen_1e9_ijv_large_to_small" 1000000000
python S3_run_sim.py "ctchen_1e9_ijv_large_to_small" 55 249
python S4_wmc_generate_dataset.py "ctchen_dataset_large" "ctchen_1e9_ijv_large_to_small" 1 249