#! /bin/bash
cd /gs-backend
python ./run_worker_api.py &
python ./run_reducer_admin.py