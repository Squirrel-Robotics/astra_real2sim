from pathlib import Path
import argparse
p=argparse.ArgumentParser()
p.add_argument('--view',choices=['overview','joint','dock'],default='overview')
args=p.parse_args()
from isaacsim import SimulationApp
app=SimulationApp({'headless':False,'create_new_stage':False,'width':1440,'height':1080})
from isaacsim.core.utils.stage import open_stage
from isaacsim.core.utils.viewports import set_camera_view
stage=Path(__file__).resolve().parents[1]/'exports/aligned_neutral.usda'
assert open_stage(str(stage))
for _ in range(12):app.update()
poses={'overview':([1.82,2.20,2.40],[.30,-.28,.52]),'joint':([-.25,.60,1.49],[.37,-.70,.82]),'dock':([1.55,1.13,1.40],[.76,-.03,.035])}
eye,target=poses[args.view];set_camera_view(eye=eye,target=target)
print('ALIGNED_SCENE_OPENED',str(stage),flush=True)
while app.is_running():app.update()
app.close(wait_for_replicator=False)
