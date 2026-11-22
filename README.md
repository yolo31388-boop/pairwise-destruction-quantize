# pairwise-destruction-quantize

## 领域

游戏、图形与多媒体

## 主题

破坏碎片定点化

## 说明

定点量化、关键帧同步与容差收敛。

初始状态下 `gameplay/destruction_quantize.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
