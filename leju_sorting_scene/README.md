# Leju 快递分拣工作区仿真场景

这是从推理服务器上 `leju_workbench_aligned` 整理的静态工作区：输送台、斜槽、木板、支架、地面及机器人底盘定位参考。仓库根目录的 [README](../README.md) 是 Astra Real-to-Sim 流程文档；这份文件说明现有资产的打开方式和验证边界。

![Isaac Sim 场景预览](preview.png)

## 打开

- 在 Isaac Sim 中打开 `exports/aligned_neutral.usda`。`aligned_warm.usda` 和 `aligned_hdri.usda` 是其他光照版本。
- 若要嵌入自己的 Isaac Sim / Isaac Lab 场景，引用 `exports/aligned_asset.usda`。它依赖同目录的 `aligned_geometry.usdc` 和 `exports/textures/`，请保留相对路径。
- 在 Blender 4.5 中打开 `leju_workbench_aligned.blend`，材质图片已打包。
- Linux 上也可设置 `ISAAC_SIM_ROOT` 后运行 `./open_isaac.sh`，或设置 `BLENDER_BIN` 后运行 `./open_blender.sh`。

USD 使用米和 Z-up。`exports/aligned_neutral.usda` 建立重力场景；`exports/aligned_asset.usda` 用于外部场景引用。

## 来源和边界

此版基于扫描与照片修订。木板厚度按 15 mm、银架外宽约 0.75 m、支撑横梁顶面高约 0.85 m 设置；其他未测尺寸含估计。`measured_dimensions.json`、`assembly_alignment.json` 和 `robot_dock_reference.json` 记录这些约束及坐标。

两条侧胶带间距约 0.75 m。`/World/Leju/RobotDock/RearEdgeDatum` 和 `BasePlacementReference` 是放置参考，不是已标定的机器人 `base_link`。胶带是视觉薄片，不增加碰撞障碍。

这里是**静态工作区资产**。仓库的 [机器人与动态包裹场景](../leju_robot_parcels/README.md) 另行叠加机器人本体和五个包裹。输送带没有动力学驱动，仓库不包含策略服务。材质、摩擦和未测尺寸是近似值。用于抓取策略或实机对齐前，应重新测量关键尺寸和接触参数。

原服务器上的 `isaac_validation.json`、`alignment_validation.json` 和 `dimension_validation.json` 是该版本当时的检查记录；仓库迁移后尚未重新运行 Isaac Sim 验证。
