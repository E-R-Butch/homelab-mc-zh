# -*- coding: utf-8 -*-
"""FramedBlocks gap translations: word-map engine for block names + hand dict for UI text.
Official zh style from in-jar seeds: '框架' suffix, 复合/竖向/反向 modifiers."""

# Full-name overrides where the engine would be awkward
FB_OVERRIDE = {
    "Framing Saw": "框架锯",
    "Powered Framing Saw": "动力框架锯",
}

# token -> zh (tuned to official in-jar seed vocabulary)
FB_WORDS = {
    "Framed": "框架",
    "Slope": "坡",
    "Panel": "侧板",
    "Slab": "台阶",
    "Stairs": "楼梯",
    "Prism": "棱",
    "Corner": "角",
    "Threeway": "三角",
    "Double": "复合",
    "Inner": "内",
    "Elevated": "高",
    "Extended": "竖向",
    "Inverted": "反向",
    "Inverse": "反向",
    "Vertical": "竖直",
    "Horizontal": "水平",
    "Divided": "分割",
    "Sliced": "切分",
    "Sloped": "斜",
    "Half": "半",
    "Stacked": "堆叠",
    "Flat": "扁平",
    "Small": "小型",
    "Large": "大型",
    "Adjustable": "可调",
    "Compound": "组合",
    "Centered": "居中",
    "Layered": "分层",
    "Checkered": "棋盘格",
    "Collapsible": "自定义",
    "Copycat": "仿制",
    "Pyramid": "金字塔",
    "Fancy": "华丽",
    "One-Way Window": "单向窗",
    "Bookshelf": "书架",
    "Chiseled Bookshelf": "雕纹书架",
    "Chain": "锁链",
    "Lantern": "灯笼",
    "Soul Lantern": "灵魂灯笼",
    "Hopper": "漏斗",
    "Item Frame": "物品展示框",
    "Glow Item Frame": "发光物品展示框",
    "Hanging Sign": "悬挂式告示牌",
    "Lightning Rod": "避雷针",
    "Masonry": "砖砌",
    "Mini Cube": "迷你方块",
    "Path": "土径",
    "Pillar Socket": "柱座",
    "Split Pillar Socket": "分割柱座",
    "Tank": "储罐",
    "Thick Lattice": "加厚格栅",
    "Tube": "管道",
    "Upper": "上层",
    "Edge": "边",
    "Wrench": "扳手",
    "Hammer": "锤子",
    "Axe": "斧",
    "Reinforcement": "加固件",
    "Pattern": "样板",
    "Phantom Paste": "幻影黏膏",
    "Pressure Plate": "压力板",
    "Obsidian": "黑曜石",
    "Stone": "石制",
    "Activator Rail": "激活铁轨",
    "Detector Rail": "探测铁轨",
    "Powered Rail": "充能铁轨",
    "Rail": "铁轨",
    "Waterlogged": "含水",
    "Wall": "墙",
    "Cube": "方块",
    "Segment": "段",
    "Weighted": "测重",
    "Light": "轻质",
    "Heavy": "重质",
    "Pillar": "柱",
    "Redstone Torch": "红石火把",
    "Redstone": "红石",
    "Torch": "火把",
    "Strip": "条",
    "Block": "方块",
    "(Slope)": "（坡）",
    "(Slab)": "（台阶）",
    "(Panel)": "（侧板）",
    "(Vertical)": "（竖直）",
    "(Horizontal)": "（水平）",
}

FB_HAND = {
    "config.framedblocks.client.altGhostRenderer": "使用备用的放置预览渲染器",
    "config.framedblocks.client.camoMessageVerbosity": "禁用伪装提示的详细程度",
    "config.framedblocks.client.camoRotationMode": "伪装旋转叠加层：显示模式",
    "config.framedblocks.client.conTexDisabled": "禁用连贯纹理支持",
    "config.framedblocks.client.conTexMode": "连贯纹理模式",
    "config.framedblocks.client.copycatStyleMode": "仿制样式叠加层：显示模式",
    "config.framedblocks.client.detailedCulling": "细节面剔除",
    "config.framedblocks.client.discreteUVSteps": "使用离散 UV 步进",
    "config.framedblocks.client.fancyHitboxes": "精美碰撞箱",
    "config.framedblocks.client.forceAoOnGlowingBlocks": "强制发光框架块的环境光遮蔽",
    "config.framedblocks.client.ghostRenderOpacity": "放置预览不透明度",
    "config.framedblocks.client.itemFrameBackgroundMode": "物品展示框背景叠加层：显示模式",
    "config.framedblocks.client.maxOverlayMode": "最大叠加层显示模式",
    "config.framedblocks.client.oneWayWindowMode": "单向窗叠加层：显示模式",
    "config.framedblocks.client.prismOffsetMode": "棱偏移叠加层：显示模式",
    "config.framedblocks.client.reinforcedMode": "加固叠加层：显示模式",
    "config.framedblocks.client.renderCamoInJade": "在 Jade 中渲染伪装外观",
    "config.framedblocks.client.renderItemModelsWithCamo": "物品模型带伪装渲染",
    "config.framedblocks.client.showAllRecipePermutationsInEmi": "在 EMI 中显示框架锯全部配方变体",
    "config.framedblocks.client.showButtonPlateTypeOverlay": "显示按钮与压力板类型叠加层",
    "config.framedblocks.client.showCamoCraftingInJei": "在 JEI 中显示伪装应用配方",
    "config.framedblocks.client.showGhostBlocks": "显示幽灵方块（放置预览）",
    "config.framedblocks.client.showSpecialCubeTypeOverlay": "显示特殊方块类型叠加层",
    "config.framedblocks.client.solidFrameMode": "实心框架模式",
    "config.framedblocks.client.splitLineMode": "自定义方块分割线叠加层：显示模式",
    "config.framedblocks.client.stateLockMode": "方块状态锁定叠加层：显示模式",
    "config.framedblocks.client.toggleWaterlogMode": "含水切换叠加层：显示模式",
    "config.framedblocks.client.toggleYSlopeMode": "Y 轴坡面切换叠加层：显示模式",
    "config.framedblocks.client.trapdoorTextureRotationMode": "活板门纹理旋转叠加层：显示模式",
    "config.framedblocks.devtools.connectionDebug": "连接判定调试",
    "config.framedblocks.devtools.doubleBlockPartDebug": "双方块部件调试",
    "config.framedblocks.devtools.occlusionShapeDebug": "遮挡形状调试",
    "config.framedblocks.devtools.quadWindingDebug": "四边形绕序调试",
    "config.framedblocks.devtools.stateMergerDebug": "StateMerger 调试",
    "config.framedblocks.devtools.stateMergerDebugFilter": "StateMerger 调试过滤器",
    "config.framedblocks.server.allowBlockEntities": "允许方块实体",
    "config.framedblocks.server.consumeCamoItem": "消耗伪装物品",
    "config.framedblocks.server.consumption": "能耗",
    "config.framedblocks.server.craftingDuration": "合成时长",
    "config.framedblocks.server.enableIntangibleFeature": "启用无形特性",
    "config.framedblocks.server.energyCapacity": "能量容量",
    "config.framedblocks.server.fireproofBlocks": "防火方块",
    "config.framedblocks.server.glowstoneLightLevel": "荧石光照等级",
    "config.framedblocks.server.maxReceive": "最大输入功率",
    "config.framedblocks.server.oneWayWindowOwnable": "单向窗可认领",
    "config.jade.plugin_framedblocks.framed_block_generic": "FramedBlocks 伪装",
    "config.jade.plugin_framedblocks.framed_item_frame": "物品展示框框架",
    "desc.framedblocks.block.fluid_tank.contents": "存储流体：%s",
    "desc.framedblocks.block.fluid_tank.contents.empty": "空",
    "desc.framedblocks.block.stored_camo": "伪装：%s",
    "desc.framedblocks.blueprint_intangible": "无形：%s",
    "desc.framedblocks.blueprint_missing_materials": "[框架蓝图] 缺少所需材料：",
    "desc.framedblocks.blueprint_reinforced": "已加固：%s",
    "desc.framedblocks.camo.empty": "空",
    "desc.framedblocks.framed_axe.retain_camo": "用这把斧破坏的框架方块会保留伪装，而不是将伪装单独掉落",
    "desc.framedblocks.slope_slab.place_upside_down": "按住潜行键倒置放置",
    "framedblocks.configuration.general": "常规",
    "framedblocks.configuration.overlay": "叠加层",
    "framedblocks.configuration.powered_framing_saw": "动力框架锯",
    "framedblocks.configuration.section.framedblocks.devtools.toml": "开发工具设置",
    "framedblocks.configuration.section.framedblocks.devtools.toml.title": "FramedBlocks 开发工具配置",
    "framedblocks.key.wipe_cache": "清除模型缓存",
    "item.framedblocks.framed_axe": "框架斧",
    "item.framedblocks.framed_reinforcement": "框架加固件",
    "item.framedblocks.framing_saw_pattern": "框架锯样板",
    "item.framedblocks.phantom_paste": "幻影黏膏",
    "label.framedblocks.jade.camo.details_prefix": "    %s",
    "label.framedblocks.jade.camo.double.one": "伪装一：%s",
    "label.framedblocks.jade.camo.double.two": "伪装二：%s",
    "label.framedblocks.jade.camo.single": "伪装：%s",
    "label.framedblocks.source_tooltip.anim_splitter.frames": "帧",
    "label.framedblocks.source_tooltip.anim_splitter.texture": "纹理",
    "msg.framedblocks.camo.non_solid": "未标记的非固体方块无法插入框架方块！",
    "msg.framedblocks.camo_application.camo.most_supported": "支持绝大多数可通过方块交互应用的伪装物品",
    "msg.framedblocks.feature.intangibility.disabled": "无形特性已被禁用，此物品因此没有作用！",
    "msg.framedblocks.frame_crafter.fail.camo_present": "输入物品不能带有伪装",
    "msg.framedblocks.frame_crafter.fail.incorrect_additive_0": "第一格中存在错误的添加物",
    "msg.framedblocks.frame_crafter.fail.incorrect_additive_1": "第二格中存在错误的添加物",
    "msg.framedblocks.frame_crafter.fail.incorrect_additive_2": "第三格中存在错误的添加物",
    "msg.framedblocks.frame_crafter.fail.insufficient_additive_0": "第一格中的添加物数量不足",
    "msg.framedblocks.frame_crafter.fail.insufficient_additive_1": "第二格中的添加物数量不足",
    "msg.framedblocks.frame_crafter.fail.insufficient_additive_2": "第三格中的添加物数量不足",
    "msg.framedblocks.frame_crafter.fail.material_lcm": "输入物品太少，无法均分转换为此产物",
    "msg.framedblocks.frame_crafter.fail.material_value": "输入材料不足",
    "msg.framedblocks.frame_crafter.fail.missing_additive_0": "第一格缺少添加物",
    "msg.framedblocks.frame_crafter.fail.missing_additive_1": "第二格缺少添加物",
    "msg.framedblocks.frame_crafter.fail.missing_additive_2": "第三格缺少添加物",
    "msg.framedblocks.frame_crafter.fail.output_size": "产物数量超过最大堆叠上限",
    "msg.framedblocks.frame_crafter.fail.success": "可合成",
    "msg.framedblocks.frame_crafter.fail.unexpected_additive_0": "第一格中出现了意料之外的添加物",
    "msg.framedblocks.frame_crafter.fail.unexpected_additive_1": "第二格中出现了意料之外的添加物",
    "msg.framedblocks.frame_crafter.fail.unexpected_additive_2": "第三格中出现了意料之外的添加物",
    "msg.framedblocks.framing_saw.search": "搜索…",
    "msg.framedblocks.framing_saw.transfer.invalid_recipe": "无效配方",
    "msg.framedblocks.framing_saw.transfer.not_implemented": "未实现传输，不会传输任何物品",
    "msg.framedblocks.powered_saw.status": "状态：",
    "msg.framedblocks.powered_saw.status.no_match": "配方不匹配",
    "msg.framedblocks.powered_saw.status.no_recipe": "无配方",
    "msg.framedblocks.powered_saw.status.ready": "就绪",
    "msg.framedblocks.prism_offset.switch": "用框架锤敲击以切换偏移",
    "msg.framedblocks.split_line.switch": "用框架扳手敲击以切换分割线方向",
    "tag.block.framedblocks.group.full": "完整框架方块",
    "tag.item.c.tools.wrench": "扳手",
    "tag.item.framedblocks.disable_intangible": "禁用无形",
    "title.framedblocks.framed_hopper": "框架漏斗",
    "title.framedblocks.framing_saw": "框架锯",
    "title.framedblocks.powered_framing_saw": "动力框架锯",
    "title.framedblocks.powered_saw.target_block": "目标：",
    "tooltip.framedblocks.camo_rotation.false": "目标伪装无法旋转",
    "tooltip.framedblocks.camo_rotation.true": "目标伪装可以旋转",
    "tooltip.framedblocks.copycat_style.set_copycat": "用框架锤敲击以使用仿制样式外观",
    "tooltip.framedblocks.copycat_style.set_standard": "用框架锤敲击以使用标准外观",
    "tooltip.framedblocks.copycat_style.use_copycat": "目标方块使用仿制样式外观",
    "tooltip.framedblocks.copycat_style.use_standard": "目标方块使用标准外观",
    "tooltip.framedblocks.frame_bg.set_camo": "用框架锤敲击以使用伪装作为背景",
    "tooltip.framedblocks.frame_bg.set_leather": "用框架锤敲击以使用皮革作为背景",
    "tooltip.framedblocks.frame_bg.use_camo": "物品展示框框架使用伪装作为背景",
    "tooltip.framedblocks.frame_bg.use_leather": "物品展示框框架使用皮革作为背景",
    "tooltip.framedblocks.framing_saw.have_item_none": "无",
    "tooltip.framedblocks.framing_saw.have_x_but_need_y_item": "拥有 %s，但需要 %s",
    "tooltip.framedblocks.framing_saw.have_x_but_need_y_item_count": "拥有 %s 个物品，但至少需要 %s 个",
    "tooltip.framedblocks.framing_saw.have_x_but_need_y_item_multi": "拥有 %s，但需要 %s 或列出的替代品",
    "tooltip.framedblocks.framing_saw.have_x_but_need_y_material_count": "拥有 %s 份材料，但至少需要 %s 份",
    "tooltip.framedblocks.framing_saw.have_x_but_need_y_tag": "拥有 %s，但需要任意 %s",
    "tooltip.framedblocks.framing_saw.loose_additive": "该物品由添加物参与合成，这些添加物将会丢失",
    "tooltip.framedblocks.framing_saw.material": "材料值：%s",
    "tooltip.framedblocks.framing_saw.mode.crafting": "合成",
    "tooltip.framedblocks.framing_saw.mode.pattern_encode": "AE2 样板编码",
    "tooltip.framedblocks.framing_saw.output_count": "产物数量：%s，上限：%s",
    "tooltip.framedblocks.framing_saw.press_to_show": "按 [%s] 显示所有可用物品",
    "tooltip.framedblocks.framing_saw.use_intermediate": "使用更小的方块作为中间步骤",
    "tooltip.framedblocks.is_waterloggable.false": "方块不可含水。",
    "tooltip.framedblocks.is_waterloggable.true": "方块可含水。",
    "tooltip.framedblocks.make_waterloggable.false": "用框架锤敲击以使其不可含水",
    "tooltip.framedblocks.make_waterloggable.true": "用框架锤敲击以使其可含水",
    "tooltip.framedblocks.one_way_window.clear_face": "潜行时用框架扳手敲击以清除透视面",
    "tooltip.framedblocks.one_way_window.curr_face": "当前透视面：%s",
    "tooltip.framedblocks.one_way_window.dir.down": "下",
    "tooltip.framedblocks.one_way_window.dir.east": "东",
    "tooltip.framedblocks.one_way_window.dir.north": "北",
    "tooltip.framedblocks.one_way_window.dir.south": "南",
    "tooltip.framedblocks.one_way_window.dir.up": "上",
    "tooltip.framedblocks.one_way_window.dir.west": "西",
    "tooltip.framedblocks.one_way_window.face.down": "下",
    "tooltip.framedblocks.one_way_window.face.east": "东",
    "tooltip.framedblocks.one_way_window.face.none": "无",
    "tooltip.framedblocks.one_way_window.face.north": "北",
    "tooltip.framedblocks.one_way_window.face.south": "南",
    "tooltip.framedblocks.one_way_window.face.up": "上",
    "tooltip.framedblocks.one_way_window.face.west": "西",
    "tooltip.framedblocks.one_way_window.face_abbr.down": "下",
    "tooltip.framedblocks.one_way_window.face_abbr.east": "东",
    "tooltip.framedblocks.one_way_window.face_abbr.none": "-",
    "tooltip.framedblocks.one_way_window.face_abbr.north": "北",
    "tooltip.framedblocks.one_way_window.face_abbr.south": "南",
    "tooltip.framedblocks.one_way_window.face_abbr.up": "上",
    "tooltip.framedblocks.one_way_window.face_abbr.west": "西",
    "tooltip.framedblocks.one_way_window.set_face": "用框架扳手敲击以将透视面设为 %s",
    "tooltip.framedblocks.powered_saw.energy": "%s / %s FE",
    "tooltip.framedblocks.powered_saw.status.no_recipe": "未选择配方：用任意框架方块点击目标栏位即可选择配方",
    "tooltip.framedblocks.prism_offset.false": "三角纹理未偏移。",
    "tooltip.framedblocks.prism_offset.true": "三角纹理偏移了半个方块。",
    "tooltip.framedblocks.reinforce_state": "方块%s。",
    "tooltip.framedblocks.reinforce_state.false": "未加固",
    "tooltip.framedblocks.reinforce_state.true": "已加固",
    "tooltip.framedblocks.split_line.false": "变形面的分割线沿陡对角线延伸。",
    "tooltip.framedblocks.split_line.true": "变形面的分割线沿缓对角线延伸。",
    "tooltip.framedblocks.trapdoor_texture_rotation.false": "打开活板门时伪装纹理不会旋转",
    "tooltip.framedblocks.trapdoor_texture_rotation.toggle": "用框架锤敲击以切换纹理旋转",
    "tooltip.framedblocks.trapdoor_texture_rotation.true": "打开活板门时伪装纹理会旋转",
    "tooltip.framedblocks.y_slope": "方块的竖向坡面使用%s面。",
    "tooltip.framedblocks.y_slope.alt": "方块的横向坡面使用%s面。",
    "tooltip.framedblocks.y_slope.alt.toggle": "用框架扳手敲击以切换到%s面",
    "tooltip.framedblocks.y_slope.front": "前",
    "tooltip.framedblocks.y_slope.horizontal": "水平",
    "tooltip.framedblocks.y_slope.side": "右",
    "tooltip.framedblocks.y_slope.toggle": "用框架扳手敲击以切换到%s面",
    "tooltip.framedblocks.y_slope.vertical": "竖直",
}

# --- engine: token-segmented translation for block/item names ---
def fb_translate_name(en):
    if en in FB_OVERRIDE:
        return FB_OVERRIDE[en]
    body = en
    suffix = ""
    # official in-jar style puts 框架 last: 门框架/复合坡框架/自定义方块框架
    if body.startswith("Framed "):
        body = body[7:]
        suffix = "框架"
    # longest-token-first segmentation
    toks = sorted(FB_WORDS, key=len, reverse=True)
    out, rest = [], body
    while rest:
        rest2 = rest.lstrip()
        if rest2 != rest:
            rest = rest2
            continue
        for t in toks:
            if rest.startswith(t):
                out.append(FB_WORDS[t])
                rest = rest[len(t):]
                break
        else:
            # one word ahead (split by space)
            sp = rest.find(" ")
            word = rest if sp < 0 else rest[:sp]
            out.append("⟦" + word + "⟧")
            rest = rest[len(word):]
    return "".join(out) + suffix


def build(gaps):
    """gaps: {modid: {key: en}} -> {modid: {key: zh}} for framedblocks."""
    fb = {}
    for k, en in gaps.get("framedblocks", {}).items():
        if k in FB_HAND:
            fb[k] = FB_HAND[k]
        elif en in FB_OVERRIDE:
            fb[k] = FB_OVERRIDE[en]
        elif en.startswith(("Framed", "Powered Framing")) or " Framed " in en:
            fb[k] = fb_translate_name(en)
        else:
            fb[k] = None  # leave for review
    return {k: v for k, v in fb.items() if v}

if __name__ == "__main__":
    import json
    gaps = json.load(open("/tmp/f76-loc/cfpa/gap-export.json"))
    tr = build(gaps)
    total = len(gaps.get("framedblocks", {}))
    print(f"framedblocks: {len(tr)}/{total} translated")
    missing = [k for k, en in gaps.get("framedblocks", {}).items()
               if k not in FB_HAND and build({"framedblocks": {k: en}}).get(k) is None]
    for k in missing[:20]:
        print("MISS", k, "=>", gaps["framedblocks"][k])
    json.dump(tr, open("/tmp/f76-loc/cfpa/tr-framedblocks.json", "w"), ensure_ascii=False, indent=1)
