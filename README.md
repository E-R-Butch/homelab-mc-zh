# Homelab MC 简体中文本地化合集 / Minecraft Mod zh_cn Localization Collection

NeoForge **1.21.1** 模组服务器的简体中文本地化合集。覆盖服务器全部自定义内容模组，
其中 NukaCraft 部分与《辐射 76》官方简体中文逐条对齐。

An unified Simplified Chinese (zh_cn) localization resource pack for our NeoForge 1.21.1
modded server. The NukaCraft portion is aligned with the official Fallout 76 zhhans
localization (254k string pairs decoded from `SeventySix - Localization.ba2`).

## 覆盖范围 / Coverage

| 模组 Mod | 版本 Version | 词条 Keys | 来源 Source |
|---|---|---|---|
| NukaCraft: Fallout mod | 1.19.10-alpha | 1739 | F76 官方对齐 413 + 人工翻译 |
| Create | 6.0.10 | 22 (缺口补齐) | 人工翻译 |
| Create Deco | 2.1.3 | 411 (全量) | [CFPA](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package) 1.21 |
| FramedBlocks | 10.6.1 | 330 (缺口补齐) | 构词引擎（沿用 jar 内官方译名风格） |
| Supplementaries | 3.9.9 | 2 (缺口补齐) | 人工翻译 |
| Farmer's Delight | 1.3.4 | 2 (缺口补齐) | 人工翻译 |
| Moonlight (lib) | 3.6.8 | 253 (全量) | 人工翻译 |
| NTGL (NukaTeam Gun Lib) | 3.2.0 | 227 (全量) | 人工翻译（术语沿用 TaCZ 惯例） |
| ModernFix | 5.27.24 | 22 (全量) | 人工翻译 |

合计约 **3000+ 词条**，模组内英文键覆盖率 100%（不存在半汉化的 Mixed Language 界面）。

> 配套仓库：配方/标签修复见 [nukacraft-recipe-fix](https://github.com/E-R-Butch/nukacraft-recipe-fix)

## 安装 / Install

### A. 服务器管理员：强制下发（推荐）

把 `homelab-zh-pack.zip` 放到任意可直链下载的位置（GitHub raw / 自建静态服务），在
`server.properties` 里配置：

```properties
resource-pack=https://raw.githubusercontent.com/E-R-Butch/homelab-mc-zh/main/homelab-zh-pack.zip
resource-pack-sha1=8a6982d11c1ebf58b8f4ed7bf27b811c5cc07c6d
resource-pack-prompt=Homelab 简体中文汉化包
require-resource-pack=false
```

玩家进服时自动弹窗提示启用，无需任何手动操作。

### B. 单个玩家：手动安装

下载 `homelab-zh-pack.zip`，放进 `.minecraft/resourcepacks/`，在游戏中启用即可。

### C. 其他模组的汉化：I18nUpdateMod

本合集只覆盖上面表格里的模组。想要 CFPA 生态的**全量模组汉化**（自动下载更新），
额外安装 [I18nUpdateMod](https://modrinth.com/mod/i18nupdatemod)（客户端 mod，与本品共存）。

## 源码与再生成 / Sources & Regeneration

`sources/` 内为可复现的生成管线，任何装有 Python 3 的机器可重跑：

| 文件 | 作用 |
|---|---|
| `gap-fill.py` | 合成器：合并全部来源 → 按模组输出 `assets/<ns>/lang/zh_cn.json` → 打包 |
| `fb_tr.py` | FramedBlocks 构词引擎 + UI 手翻词典 |
| `gap_tr_hand.py` | NTGL / Moonlight / Create / ModernFix / 零碎手翻词典 |
| `gap_tr_hand.py` 依赖 | homelab 上的 `gap-export.json`（各模组缺口键清单） |

再生成流程（模组更新后）：

```bash
python3 gap-fill.py   # 重新产出 homelab-zh-pack.zip
```

### 翻译方法论（NukaCraft）

1. 从《辐射 76》官方简中 BA2 解码 254,000+ 对英中字符串（`.strings`/`.dlstrings`/`.ilstrings`）
2. 按字符串 ID 与英文原文精确/归一化匹配 NukaCraft 词条（413 条直接继承官方译名：
   核子可乐、哔哔小子、辐射极琉矿、钢铁兄弟会……）
3. 其余词条人工翻译，术语严格遵循官方惯例：`Perk→辅助能力`、`Raider→掠夺者`、
   `caps→瓶盖`；`S.P.E.C.I.A.L.`、`Pip-Boy` 等约定俗成缩写保留原文
4. 格式符（`%s`/`%1$s`/`%%`）与 `§` 色码逐条校验，不符即构建失败

### FramedBlocks 构词引擎

jar 内自带 108 条官方中文（其余 330 条缺失），官方构词风格为「几何描述+框架」后缀
（`门框架`、`复合坡框架`）。`fb_tr.py` 用最长 token 分词 + 词表映射复刻该风格，
与官方已有译名零冲突。

## 质量 / Quality

- ✅ 全部模组英文键 100% 覆盖（构建时校验，缺一条即报错）
- ✅ 格式符 parity 校验（占位符数量/位置逐一比对）
- ✅ `§` 色码保真（官方对齐丢失的前缀色码自动回填）
- ✅ 官方译名优先级高于人工翻译（F76 官方 > CFPA > 人工）

## 许可 / License

CC0 1.0（公共领域）。CFPA 部分遵循其上游许可（详见
[CFPA 仓库](https://github.com/CFPAOrg/Minecraft-Mod-Language-Package)）。
NukaCraft 译名含《辐射 76》官方本地化对齐内容，版权归 Bethesda/贝塞斯达所有，仅作互操作用途。
