# coding: utf-8

"""
HH -> bbWW datasets for the 2024 Cross-trigger studies
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v8 import campaign_run3_2024_nano_v8 as cpn


cpn.add_dataset(
    name="ggHH_kl_1_kt_1_sl_hbbhww_powheg",
    id=14857752,
    processes=[procs.ggHH_kl_1_kt_1_sl_hbbhww],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter24NanoAOD-133X_mcRun3_2024_realistic_v8-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=498062,
)

