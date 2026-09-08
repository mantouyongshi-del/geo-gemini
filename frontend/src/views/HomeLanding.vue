<template>
  <div class="landing-container">
    <!-- 1. 顶部公告彩带 (Top Announcement Ribbon - Similarweb Style) -->
    <div class="top-promo-ribbon">
      <div class="ribbon-inner">
        <span class="ribbon-pill">Now live ✦</span>
        <span class="ribbon-text">
          <strong>2026 生成式 AI 搜索与 GEO 商业白皮书发布：</strong>当大模型重塑搜索流量，您的品牌处于哪个梯队？
        </span>
        <router-link to="/console" class="ribbon-link">
          <span>免费体验体检</span>
          <span class="ribbon-arrow">→</span>
        </router-link>
      </div>
    </div>

    <!-- 2. 悬浮磨砂暗黑导航栏 (Header) -->
    <header class="landing-header">
      <div class="header-inner">
        <!-- 左上角自然舒展、大气通透的品牌 Logo (无小气边框拘束) -->
        <router-link to="/" class="brand-link" title="蜉蝣小宝 · AI 营销智能大脑">
          <div class="logo-aura-wrap">
            <div class="logo-soft-glow"></div>
            <img src="/logo-white.png" alt="蜉蝣小宝" class="logo-unconstrained" />
          </div>
          <div class="brand-badge-tag">GEO 2.0</div>
        </router-link>

        <nav class="nav-links">
          <a href="#hero-search" class="nav-item">搜索透视</a>
          <a href="#shift-slider" class="nav-item">攻防对比</a>
          <a href="#solutions" class="nav-item">行业方案</a>
          <a href="#architecture" class="nav-item">认知引擎</a>
          <a href="#roadmap" class="nav-item">30天交付</a>
          <a href="#roi" class="nav-item">商业账本</a>
          <a href="#faq" class="nav-item">常见问题</a>
        </nav>

        <div class="header-actions">
          <router-link to="/diagnostic_report" class="btn-ghost-nav">标杆报告</router-link>
          <router-link to="/console" class="btn-ghost-nav">工作台</router-link>
          <router-link to="/console" class="btn-primary-nav">
            <span class="btn-glow-bg"></span>
            <span class="btn-text">免费体检 ✨</span>
          </router-link>
        </div>
      </div>
    </header>

    <!-- 3. 品牌首屏 (Hero Section - 精炼、大气、深邃留白) -->
    <section class="hero-section">
      <!-- 动态深空环境光晕 -->
      <div class="ambient-glow orb-blue"></div>
      <div class="ambient-glow orb-purple"></div>
      <div class="ambient-glow orb-orange"></div>
      <div class="grid-overlay"></div>

      <div class="section-inner hero-inner">
        <!-- 标签气泡 -->
        <div class="hero-pill-badge">
          <span class="badge-dot-live"></span>
          <span class="badge-text">2026 新一代企业生成式引擎优化 · GEO 认知中枢</span>
        </div>

        <!-- 极简主标题：磅礴、从容、直击痛点 -->
        <h1 class="hero-headline">
          当 5 亿客户向 AI 提问<br />
          让您的品牌成为 <span class="text-gradient">第一推荐</span>
        </h1>

        <!-- 精炼副标题：突出核心价值 -->
        <p class="hero-subtext">
          穿透豆包、DeepSeek、通义千问等主流大模型推荐决策层<br />
          测算潜在客源流失 · 构建专属于企业的不可替代权威知识资产
        </p>

        <!-- 核心交互式搜索诊断框 (Similarweb Style Input Bar) -->
        <div id="hero-search" class="hero-search-wrapper">
          <div class="search-input-box">
            <div class="search-mode-select">
              <span class="mode-icon">🏢</span>
              <span class="mode-label">全网诊断</span>
              <span class="mode-caret">▾</span>
            </div>
            
            <div class="search-divider"></div>

            <div class="search-input-field">
              <input
                type="text"
                v-model="heroBrandInput"
                :placeholder="currentPlaceholder"
                @keyup.enter="handleHeroSubmit"
              />
            </div>

            <button class="btn-search-action" @click="handleHeroSubmit">
              <span class="action-glow"></span>
              <span class="action-content">
                <span class="action-icon">✨</span>
                <span class="action-label">立即透视</span>
              </span>
            </button>
          </div>

          <!-- 精炼标杆案例 Chips -->
          <div class="quick-chips-row">
            <span class="chips-label">标杆案例：</span>
            <button
              v-for="(chip, idx) in quickChips"
              :key="idx"
              class="chip-btn"
              @click="applyQuickChip(chip)"
            >
              {{ chip.label }}
            </button>
          </div>

          <!-- 3 个核心信任徽章 -->
          <div class="trust-metrics-row">
            <div class="trust-metric">
              <span class="metric-icon">⚡</span>
              <span class="metric-text">10秒穿透实测</span>
            </div>
            <div class="trust-metric-dot"></div>
            <div class="trust-metric">
              <span class="metric-icon">🤖</span>
              <span class="metric-text">直连 5 大基座大模型</span>
            </div>
            <div class="trust-metric-dot"></div>
            <div class="trust-metric">
              <span class="metric-icon">🛡️</span>
              <span class="metric-text">知识本体 Schema 权威确权</span>
            </div>
          </div>
        </div>

        <!-- 4. 首屏大模型双端切面遥测控制台 -->
        <div class="hero-dashboard-mockup">
          <div class="mockup-window-header">
            <div class="window-controls">
              <span class="window-dot dot-red"></span>
              <span class="window-dot dot-yellow"></span>
              <span class="window-dot dot-green"></span>
            </div>
            <div class="window-address-bar">
              <span class="lock-icon">🔒</span>
              <span class="url-text">mayfly-geo.ai/telemetry/live-scan?target=恒瑞智能装备</span>
            </div>
            <div class="window-status-pill">
              <span class="pulse-green"></span>
              <span>5 大基座大模型实时直连中</span>
            </div>
          </div>

          <div class="mockup-window-body">
            <!-- 左栏：生成式推荐切面对比 -->
            <div class="mockup-panel comparison-panel">
              <div class="panel-top-tabs">
                <button
                  class="compare-tab"
                  :class="{ active: activeCompareMode === 'after' }"
                  @click="activeCompareMode = 'after'"
                >
                  <span class="tab-indicator green"></span>
                  <span>🟢 GEO 优化后：92% 行业首推</span>
                </button>
                <button
                  class="compare-tab"
                  :class="{ active: activeCompareMode === 'before' }"
                  @click="activeCompareMode = 'before'"
                >
                  <span class="tab-indicator red"></span>
                  <span>🔴 优化前：0% 隐形被截流</span>
                </button>
              </div>

              <!-- 搜索提问模拟 -->
              <div class="chat-query-pill">
                <span class="query-avatar">👤</span>
                <div class="query-content">
                  <div class="query-meta">采购提问场景 · 豆包/DeepSeek 实测</div>
                  <div class="query-str">“2026年 工业数控激光切管机哪家口碑好性价比高？”</div>
                </div>
              </div>

              <!-- 大模型回答卡片 -->
              <div v-if="activeCompareMode === 'after'" class="ai-response-box state-after">
                <div class="ai-box-header">
                  <div class="ai-brand-badge">
                    <span class="ai-badge-icon">🤖</span>
                    <span>字节跳动 · 豆包 & DeepSeek-R1 综合推荐</span>
                  </div>
                  <span class="ai-rank-tag gold">🏆 首选推荐 #1 · Schema实体确权</span>
                </div>

                <div class="ai-box-body">
                  <div class="highlight-brand-card">
                    <div class="h-card-top">
                      <span class="h-name">恒瑞智能装备（无锡恒瑞智能装备科技有限公司）</span>
                      <span class="h-score">推荐指数 98.4</span>
                    </div>
                    <div class="h-card-desc">
                      经国家工信部专精特新核验与全网 19 篇权威研报交叉验证，在重管数控切管领域综合满意度位列第 1。
                    </div>
                    <div class="h-citation-row">
                      <span class="cite-tag">🔗 搜狐科技 · 深度评测报告</span>
                      <span class="cite-tag">🔗 企查查 · 官方专利资质核验</span>
                      <span class="cite-tag">🔗 知乎专栏 · 选型避坑指南</span>
                      <span class="cite-tag">🔗 新浪财经 · 优质制造名录</span>
                    </div>
                  </div>
                </div>
              </div>

              <div v-else class="ai-response-box state-before">
                <div class="ai-box-header">
                  <div class="ai-brand-badge">
                    <span class="ai-badge-icon">⚠️</span>
                    <span>字节跳动 · 豆包 & DeepSeek-R1 综合推荐</span>
                  </div>
                  <span class="ai-rank-tag red">⚠️ 贵司完全隐形 · 客源被截流</span>
                </div>

                <div class="ai-box-body">
                  <div class="competitor-brand-card">
                    <div class="c-title">1. 大族激光 / 宏山激光（推荐提及率 85%）</div>
                    <div class="c-desc">公域第三方研报与高权重报道覆盖充分，稳居大模型推荐首位。</div>
                  </div>

                  <div class="leak-alert-card">
                    <div class="alert-icon">🚨</div>
                    <div class="alert-text">
                      <strong>目标客户诊断结果：恒瑞智能装备 (0% 提及)</strong><br />
                      公域信源空白，大模型在决策层直接淘汰，意向客户被竞品无声截流！
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 右栏：实时遥测雷达 -->
            <div class="mockup-panel telemetry-panel">
              <div class="telemetry-card score-card">
                <div class="card-header-clean">
                  <span class="card-label">GEO 综合健康指数</span>
                  <span class="status-badge excellent">优异卓越</span>
                </div>
                <div class="gauge-display">
                  <div class="gauge-circle">
                    <span class="gauge-num">88.6</span>
                    <span class="gauge-unit">/ 100</span>
                  </div>
                  <div class="gauge-meta">
                    <div class="meta-row">
                      <span class="dot-green"></span>
                      <span>优化前：12.4 (严重失血)</span>
                    </div>
                    <div class="meta-row highlight">
                      <span class="dot-purple"></span>
                      <span>GEO跃升：+614% 提升</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="telemetry-card leads-card">
                <div class="card-header-clean">
                  <span class="card-label">月度挽回流失订单资产</span>
                  <span class="trend-pill">+340% 转化</span>
                </div>
                <div class="leads-val-row">
                  <span class="currency">￥</span>
                  <span class="number">240,000</span>
                  <span class="period">/ 月</span>
                </div>
                <p class="leads-note">依据：每月约 150 位采购决策者向 AI 提问选型，不再被同行截流。</p>
              </div>

              <div class="telemetry-card model-breakdown-card">
                <div class="card-header-clean">
                  <span class="card-label">基座大模型首推覆盖率</span>
                  <span class="radar-live-text">📡 实时巡检中</span>
                </div>
                <div class="model-bars-list">
                  <div class="model-bar-item">
                    <div class="bar-info">
                      <span class="m-name">字节跳动 · 豆包</span>
                      <span class="m-val">92%</span>
                    </div>
                    <div class="bar-track"><div class="bar-fill" style="width: 92%"></div></div>
                  </div>
                  <div class="model-bar-item">
                    <div class="bar-info">
                      <span class="m-name">深度求索 · DeepSeek</span>
                      <span class="m-val">89%</span>
                    </div>
                    <div class="bar-track"><div class="bar-fill" style="width: 89%"></div></div>
                  </div>
                  <div class="model-bar-item">
                    <div class="bar-info">
                      <span class="m-name">阿里巴巴 · 通义千问</span>
                      <span class="m-val">94%</span>
                    </div>
                    <div class="bar-track"><div class="bar-fill" style="width: 94%"></div></div>
                  </div>
                  <div class="model-bar-item">
                    <div class="bar-info">
                      <span class="m-name">腾讯科技 · 元宝</span>
                      <span class="m-val">86%</span>
                    </div>
                    <div class="bar-track"><div class="bar-fill" style="width: 86%"></div></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. 权威大模型与信源无限循环跑马灯 (大幅强化尺寸与清晰度，大字、大卡、清晰醒目) -->
    <section class="marquee-section scroll-reveal">
      <div class="marquee-header-wrap">
        <div class="marquee-title-row">
          <span class="marquee-pulse-dot"></span>
          <h3 class="marquee-title">直连中国主流基座大模型 · 覆盖国家级及高权重权威信源生态</h3>
          <span class="marquee-sub-note">全天候 24/7 实时探针检索与数据回溯</span>
        </div>
      </div>

      <div class="marquee-wrapper">
        <div class="marquee-track">
          <!-- 跑马灯元素 1 组 (大卡片、大图标、大字号) -->
          <div
            v-for="(item, i) in marqueePartners"
            :key="'p1-' + i"
            class="marquee-card"
          >
            <div class="card-icon-halo">{{ item.icon }}</div>
            <div class="card-text-block">
              <div class="card-main-name">{{ item.name }}</div>
              <div class="card-sub-tag">{{ item.tag }}</div>
            </div>
            <div class="card-live-dot" title="实时直连在线"></div>
          </div>
          <!-- 跑马灯元素 2 组 (无缝平滑衔接) -->
          <div
            v-for="(item, i) in marqueePartners"
            :key="'p2-' + i"
            class="marquee-card"
          >
            <div class="card-icon-halo">{{ item.icon }}</div>
            <div class="card-text-block">
              <div class="card-main-name">{{ item.name }}</div>
              <div class="card-sub-tag">{{ item.tag }}</div>
            </div>
            <div class="card-live-dot" title="实时直连在线"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. 范式转移动态滑块 -->
    <section id="shift-slider" class="shift-section scroll-reveal">
      <div class="section-inner">
        <div class="section-header-center scroll-reveal delay-1">
          <div class="section-badge">范式突围 · PARADIGM SHIFT</div>
          <h2 class="section-title">
            搜索规则彻底变了：<br />
            在 AI 时代赢得生意的 <span class="text-gradient">四大关键战场</span>
          </h2>
          <p class="section-sub">
            用户不再翻阅 10 页传统网页，大模型每次只推荐 1~3 个品牌。若未建立知识本体，在客户心智中等同于“不存在”。
          </p>
        </div>

        <!-- 交互式轮播 Slider -->
        <div class="shift-slider-container scroll-reveal delay-2">
          <!-- 顶部横向进度 Tabs -->
          <div class="slider-tabs-row">
            <button
              v-for="(slide, sIdx) in shiftSlides"
              :key="sIdx"
              class="slider-tab-btn"
              :class="{ active: currentSlideIndex === sIdx }"
              @click="switchSlide(sIdx)"
            >
              <div class="tab-progress-track">
                <div
                  class="tab-progress-fill"
                  :style="{ width: currentSlideIndex === sIdx ? `${slideProgress}%` : (currentSlideIndex > sIdx ? '100%' : '0%') }"
                ></div>
              </div>
              <div class="tab-header-content">
                <span class="tab-index">{{ slide.number }}</span>
                <span class="tab-title">{{ slide.shortTitle }}</span>
              </div>
            </button>
          </div>

          <!-- 滑块主体卡片 -->
          <div class="slider-card-body">
            <div class="slide-content-left">
              <div class="slide-badge">{{ currentSlide.tag }}</div>
              <h3 class="slide-headline">{{ currentSlide.headline }}</h3>
              <p class="slide-desc">{{ currentSlide.description }}</p>

              <div class="slide-points-list">
                <div class="point-item" v-for="(p, pIdx) in currentSlide.points" :key="pIdx">
                  <span class="p-icon">✓</span>
                  <span class="p-text">{{ p }}</span>
                </div>
              </div>

              <div class="slide-cta-row">
                <router-link to="/console" class="btn-slide-primary">
                  <span>查看针对贵司的防御方案</span>
                  <span class="arrow">→</span>
                </router-link>
              </div>
            </div>

            <div class="slide-content-right">
              <div class="slide-visual-card">
                <div class="visual-header">
                  <span class="v-pill">{{ currentSlide.visualBadge }}</span>
                  <span class="v-model">实时计算模拟</span>
                </div>
                
                <div class="visual-body">
                  <div class="metric-big-highlight">
                    <span class="m-num">{{ currentSlide.metricNum }}</span>
                    <span class="m-unit">{{ currentSlide.metricUnit }}</span>
                  </div>
                  <div class="m-label">{{ currentSlide.metricLabel }}</div>

                  <div class="visual-interactive-preview">
                    <div class="flow-step step-bad">
                      <div class="step-tag">传统旧时代</div>
                      <div class="step-text">{{ currentSlide.oldState }}</div>
                    </div>
                    <div class="flow-arrow-down">⬇ 规则被大模型颠覆</div>
                    <div class="flow-step step-good">
                      <div class="step-tag">蜉蝣小宝 GEO</div>
                      <div class="step-text">{{ currentSlide.newState }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. 行业解决方案选项卡 -->
    <section id="solutions" class="solutions-section scroll-reveal">
      <div class="section-inner">
        <div class="section-header-center scroll-reveal delay-1">
          <div class="section-badge">行业全景 · INDUSTRY SOLUTIONS</div>
          <h2 class="section-title">
            专为不同行业打造的 <span class="text-gradient">GEO 获客增长战法</span>
          </h2>
          <p class="section-sub">
            针对 B2B制造、大宅定制、现代消费、专科医疗、高端法律等长决策周期行业，击穿大模型推荐层。
          </p>
        </div>

        <!-- 行业横向 Pills -->
        <div class="industry-pills-wrap scroll-reveal delay-2">
          <button
            v-for="(ind, indIdx) in industries"
            :key="ind.id"
            class="ind-pill-btn"
            :class="{ active: activeIndustryIndex === indIdx }"
            @click="activeIndustryIndex = indIdx"
          >
            <span class="ind-icon">{{ ind.icon }}</span>
            <span class="ind-name">{{ ind.name }}</span>
          </button>
        </div>

        <!-- 行业展示卡片 -->
        <div class="industry-detail-card scroll-reveal delay-3">
          <div class="ind-left-content">
            <div class="ind-meta-tag">{{ currentIndustry.category }}</div>
            <h3 class="ind-headline">{{ currentIndustry.headline }}</h3>
            
            <div class="ind-scenario-box">
              <div class="scenario-label">🎯 典型高频客户意图提问</div>
              <div class="scenario-query">{{ currentIndustry.scenarioQuery }}</div>
            </div>

            <div class="ind-challenge-box">
              <span class="c-title">🚨 行业失血痛点：</span>
              <span class="c-text">{{ currentIndustry.painPoint }}</span>
            </div>

            <div class="ind-tactics-list">
              <div class="tactic-title">🛡️ 蜉蝣小宝 30 天落地攻防打法：</div>
              <div class="tactic-item" v-for="(t, tIdx) in currentIndustry.tactics" :key="tIdx">
                <span class="t-badge">{{ tIdx + 1 }}</span>
                <span class="t-text">{{ t }}</span>
              </div>
            </div>

            <div class="ind-actions-row">
              <router-link
                :to="{ path: '/console', query: { industry: currentIndustry.name, brand: currentIndustry.defaultBrand } }"
                class="btn-ind-action"
              >
                <span>体验该行业体检方案</span>
                <span class="arrow">→</span>
              </router-link>
            </div>
          </div>

          <div class="ind-right-metrics">
            <div class="stat-card-gold">
              <div class="stat-badge">真实标杆验证成果</div>
              <div class="stat-number-row">
                <span class="stat-num">{{ currentIndustry.statValue }}</span>
              </div>
              <div class="stat-label">{{ currentIndustry.statDesc }}</div>
              
              <div class="stat-bar-compare">
                <div class="comp-row">
                  <span class="comp-title">优化前推荐提及</span>
                  <span class="comp-val red">{{ currentIndustry.preRate }}</span>
                </div>
                <div class="comp-row">
                  <span class="comp-title">GEO优化后提及率</span>
                  <span class="comp-val green">{{ currentIndustry.postRate }}</span>
                </div>
              </div>
            </div>

            <div class="testimonial-quote-card">
              <div class="quote-mark">“</div>
              <p class="quote-text">{{ currentIndustry.clientQuote }}</p>
              <div class="client-info-row">
                <div class="client-avatar">{{ currentIndustry.clientAvatar }}</div>
                <div class="client-meta">
                  <div class="client-name">{{ currentIndustry.clientName }}</div>
                  <div class="client-title">{{ currentIndustry.clientTitle }}</div>
                </div>
                <div class="verified-seal">✓ 已核验标杆</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. 核心底层：4 层 GEO 认知工程架构 -->
    <section id="architecture" class="arch-section scroll-reveal">
      <div class="section-inner">
        <div class="section-header-center scroll-reveal delay-1">
          <div class="section-badge">核心技术 · ENGINE ARCHITECTURE</div>
          <h2 class="section-title">
            穿透大模型决策的 <span class="text-gradient">四层认知工程体系</span>
          </h2>
          <p class="section-sub">
            专为 Transformer 大模型与 RAG 检索召回设计的确定性知识工程。
          </p>
        </div>

        <div class="arch-cards-grid">
          <div
            v-for="(arch, aIdx) in archLayers"
            :key="aIdx"
            class="arch-card scroll-reveal"
            :class="'delay-' + (aIdx + 1)"
          >
            <div class="card-glow-border"></div>
            <div class="card-inner-box">
              <div class="arch-layer-pill">LAYER 0{{ aIdx + 1 }}</div>
              <div class="arch-icon-wrap">{{ arch.icon }}</div>
              <h3 class="arch-name">{{ arch.name }}</h3>
              <div class="arch-sub-en">{{ arch.enName }}</div>
              <p class="arch-summary">{{ arch.desc }}</p>
              
              <div class="arch-checklist">
                <div class="check-item" v-for="(item, cIdx) in arch.items" :key="cIdx">
                  <span class="dot"></span>
                  <span>{{ item }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. 30 天闭环交付体系 -->
    <section id="roadmap" class="roadmap-section scroll-reveal">
      <div class="section-inner">
        <div class="section-header-center scroll-reveal delay-1">
          <div class="section-badge">确定性保障 · 30-DAY DELIVERY</div>
          <h2 class="section-title">
            从完全隐形到全网首推：<br />
            <span class="text-gradient">30 天闭环战役交付蓝图</span>
          </h2>
          <p class="section-sub">
            每一步皆有确权文档与权威索引链接核验，让投入落地为不可逆的公域数字资产。
          </p>
        </div>

        <div class="roadmap-timeline-grid">
          <div
            v-for="(step, sIdx) in roadmapSteps"
            :key="sIdx"
            class="roadmap-phase-card scroll-reveal"
            :class="'delay-' + (sIdx + 1)"
          >
            <div class="phase-top">
              <span class="phase-badge">PHASE {{ step.phase }}</span>
              <span class="phase-days">{{ step.days }}</span>
            </div>
            <h3 class="phase-title">{{ step.title }}</h3>
            <p class="phase-action">{{ step.action }}</p>
            <div class="phase-deliverable">
              <div class="d-label">📦 阶段交付物：</div>
              <div class="d-val">{{ step.deliverable }}</div>
            </div>
            <div class="phase-status">
              <span class="status-dot"></span>
              <span>100% 验收达标推进</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 10. 商业账本：传统获客 VS 蜉蝣小宝 GEO -->
    <section id="roi" class="roi-section scroll-reveal">
      <div class="section-inner">
        <div class="section-header-center scroll-reveal delay-1">
          <div class="section-badge">商业价值 · ECONOMIC VALUE</div>
          <h2 class="section-title">
            算清企业的商业账本：<br />
            为什么说 <span class="text-gradient">GEO 是极高 ROI 的战略资产</span>？
          </h2>
          <p class="section-sub">
            传统竞价是“持续租用流量”，停充即停流；GEO 是“购买永久数字房产”，一次构筑，长效享受大模型推荐复利。
          </p>
        </div>

        <div class="roi-table-card scroll-reveal delay-2">
          <div class="roi-table-header">
            <div class="col-dim">对比维度</div>
            <div class="col-sem">传统搜索竞价 (SEM)</div>
            <div class="col-seo">传统网站 SEO</div>
            <div class="col-geo highlight">蜉蝣小宝 GEO 认知工程</div>
          </div>

          <div class="roi-table-row" v-for="(row, rIdx) in roiRows" :key="rIdx">
            <div class="col-dim font-bold">{{ row.dimension }}</div>
            <div class="col-sem">{{ row.sem }}</div>
            <div class="col-seo">{{ row.seo }}</div>
            <div class="col-geo highlight-cell">
              <span class="check-icon">✓</span>
              <span>{{ row.geo }}</span>
            </div>
          </div>
        </div>

        <div class="roi-summary-banner scroll-reveal delay-3">
          <div class="banner-icon">💡</div>
          <div class="banner-text">
            <strong>核心战略结论：</strong>大模型不看您在竞价里充了多少钱，它只采信公域中不可篡改的权威知识。越早布局 GEO，越早以极低成本筑起同行无法逾越的认知壁垒！
          </div>
        </div>
      </div>
    </section>

    <!-- 11. 常见问题解答 -->
    <section id="faq" class="faq-section scroll-reveal">
      <div class="section-inner">
        <div class="section-header-center scroll-reveal delay-1">
          <div class="section-badge">疑问解答 · FAQ</div>
          <h2 class="section-title">
            企业管理者最关心的 <span class="text-gradient">核心问题</span>
          </h2>
        </div>

        <div class="faq-accordion-list scroll-reveal delay-2">
          <div
            v-for="(faq, fIdx) in faqs"
            :key="fIdx"
            class="faq-item"
            :class="{ open: openFaqIndex === fIdx }"
            @click="toggleFaq(fIdx)"
          >
            <div class="faq-question">
              <span class="q-icon">Q</span>
              <span class="q-text">{{ faq.question }}</span>
              <span class="q-toggle">{{ openFaqIndex === fIdx ? '−' : '+' }}</span>
            </div>
            <div v-show="openFaqIndex === fIdx" class="faq-answer">
              <p>{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 12. 转化底栏 -->
    <section class="bottom-cta-banner scroll-reveal">
      <div class="cta-cosmic-glow"></div>
      <div class="cta-inner scroll-reveal delay-1">
        <div class="cta-badge">✦ 即刻行动 · 截断客源失血</div>
        <h2 class="cta-headline">
          准备好在 AI 搜索时代，彻底终结客源被竞品截流的局面了吗？
        </h2>
        <p class="cta-sub">
          无需安装任何插件 · 现场直连 5 大主流基座大模型 · 10秒出具专属体检书
        </p>

        <div class="cta-action-box">
          <div class="cta-input-wrap">
            <input
              type="text"
              v-model="bottomBrandInput"
              placeholder="输入您的企业名称或核心品牌（如：无锡恒瑞智能装备）"
              @keyup.enter="handleBottomSubmit"
            />
            <button class="btn-cta-submit" @click="handleBottomSubmit">
              <span>免费启动体检</span>
              <span class="arrow">→</span>
            </button>
          </div>
        </div>

        <div class="cta-footer-tags">
          <span>🟢 字节豆包直连</span>
          <span class="sep">·</span>
          <span>🧠 DeepSeek-R1 核验</span>
          <span class="sep">·</span>
          <span>🌐 阿里通义千问召回</span>
          <span class="sep">·</span>
          <span>💬 腾讯元宝对标</span>
        </div>
      </div>
    </section>

    <!-- 13. 暗黑品牌页脚 (Footer) -->
    <footer class="landing-footer">
      <div class="footer-inner">
        <div class="footer-brand-col">
          <div class="footer-logo">
            <img src="/logo-white.png" alt="蜉蝣小宝" class="f-logo-img" />
          </div>
          <p class="footer-slogan">
            新一代企业生成式 AI 搜索引擎商业认知与拓客中枢。帮助中国优质实体企业抢占主流大模型第一推荐位。
          </p>
          <div class="footer-live-status">
            <span class="status-live-dot"></span>
            <span>五大基座大模型接口：运行稳定 (2026 官方最新引擎)</span>
          </div>
        </div>

        <div class="footer-links-col">
          <h4 class="col-title">平台能力</h4>
          <router-link to="/console" class="f-link">准客户 AI 可见度体检</router-link>
          <router-link to="/diagnostic_report" class="f-link">标杆企业体检书</router-link>
          <router-link to="/ai_report" class="f-link">GEO 攻防监控看板</router-link>
          <a href="#hero-search" class="f-link">行业高频词透视</a>
        </div>

        <div class="footer-links-col">
          <h4 class="col-title">行业方案</h4>
          <a href="#solutions" class="f-link">工业装备与高客单制造</a>
          <a href="#solutions" class="f-link">高端大宅与系统门窗定制</a>
          <a href="#solutions" class="f-link">连锁餐饮与商业加盟</a>
          <a href="#solutions" class="f-link">专科医疗与数字化齿科</a>
          <a href="#solutions" class="f-link">商务法务与大型律所</a>
        </div>

        <div class="footer-links-col">
          <h4 class="col-title">关于与保障</h4>
          <a href="#roadmap" class="f-link">30 天落地交付流程</a>
          <a href="#roi" class="f-link">商业账本与投入产出</a>
          <a href="#faq" class="f-link">常见问题解答</a>
          <span class="f-link disabled">企业知识产权保护协议</span>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <div class="copy-text">
          © 2026 蜉蝣小宝 (MAYFLY GEO) 认知工程实验室. All Rights Reserved.
        </div>
        <div class="legal-text">
          声明：测评数据基于公域公开信源抓取与大模型标准接口客观召回。
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// 搜索栏状态
const heroBrandInput = ref('');
const bottomBrandInput = ref('');

// 动态循环切换的 Placeholder
const placeholders = [
  '例如：无锡恒瑞智能装备（工业数控激光切管机）',
  '例如：佛山佳豪系统门窗（高端断桥铝定制）',
  '例如：老乡鸡 / 特色快餐连锁（招商加盟）',
  '例如：数字化种植牙与正畸专科门诊',
  '例如：企业常年法律顾问与商事律所'
];
const currentPlaceholderIndex = ref(0);
const currentPlaceholder = computed(() => placeholders[currentPlaceholderIndex.value]);

let placeholderTimer = null;
let scrollObserver = null;

onMounted(() => {
  // 占位符打字轮播
  placeholderTimer = setInterval(() => {
    currentPlaceholderIndex.value = (currentPlaceholderIndex.value + 1) % placeholders.length;
  }, 3500);

  // 初始化页面滚动渐显渐隐监听器
  initScrollObserver();
});

// 滚动渐显渐隐监听函数
function initScrollObserver() {
  const targets = document.querySelectorAll('.scroll-reveal');
  if (!targets.length) return;

  scrollObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const el = entry.target;
        const rect = entry.boundingClientRect;

        if (entry.isIntersecting) {
          el.classList.add('is-revealed');
          el.classList.remove('is-exited-top');
        } else {
          if (rect.top < 0) {
            el.classList.add('is-exited-top');
            el.classList.remove('is-revealed');
          } else {
            el.classList.remove('is-revealed');
            el.classList.remove('is-exited-top');
          }
        }
      });
    },
    {
      threshold: [0, 0.08, 0.9, 1],
      rootMargin: '-30px 0px -30px 0px'
    }
  );

  targets.forEach((el) => scrollObserver.observe(el));
}

// 快速体验 Chips
const quickChips = [
  { label: '🏭 工业切管机', brand: '恒瑞智能装备', company: '无锡恒瑞智能装备科技有限公司', industry: '工业数控激光切管机制造', city: '无锡' },
  { label: '🏡 高端系统门窗', brand: '佳豪系统门窗', company: '佛山尚品佳豪智能家居系统有限公司', industry: '高端断桥铝系统门窗与阳光房', city: '佛山' },
  { label: '🍲 快餐加盟', brand: '老乡鸡', company: '安徽老乡鸡餐饮股份有限公司', industry: '中式快餐连锁加盟与招商', city: '全国' },
  { label: '🦷 数字化齿科', brand: '恒伦口腔', company: '数字化种植牙与隐形正畸专科门诊', industry: '专科医疗与数字化齿科', city: '全国' },
  { label: '⚖️ 商事常法', brand: '金杜律所', company: '商事争议与常年法律顾问律所', industry: '企业商事争议解决与常年合规', city: '全国' }
];

function applyQuickChip(chip) {
  router.push({
    path: '/console',
    query: {
      brand: chip.brand,
      company: chip.company,
      industry: chip.industry,
      city: chip.city
    }
  });
}

function handleHeroSubmit() {
  const q = heroBrandInput.value.trim();
  if (!q) {
    router.push('/console');
    return;
  }
  router.push({
    path: '/console',
    query: { brand: q }
  });
}

function handleBottomSubmit() {
  const q = bottomBrandInput.value.trim();
  if (!q) {
    router.push('/console');
    return;
  }
  router.push({
    path: '/console',
    query: { brand: q }
  });
}

// 首屏画报 Before / After 模式切换
const activeCompareMode = ref('after');

// 跑马灯生态名单
const marqueePartners = [
  { icon: '⚡', name: '字节跳动 · 豆包', tag: '火山引擎方舟直连' },
  { icon: '🧠', name: '深度求索 · DeepSeek', tag: 'R1推理全量核验' },
  { icon: '🌐', name: '阿里巴巴 · 通义千问', tag: '百炼原生B2B召回' },
  { icon: '💬', name: '腾讯科技 · 元宝', tag: '混元大模型生态' },
  { icon: '🔍', name: '百度智能云 · 文心一言', tag: '搜索语义穿透' },
  { icon: '📚', name: '百度百科官方确权', tag: '权威知识本体' },
  { icon: '🛡️', name: '企查查商业资质', tag: '官方资质核验' },
  { icon: '📰', name: '搜狐科技 · 工业评测', tag: '高权重采信信源' },
  { icon: '📈', name: '新浪财经 · 产业研报', tag: '权威媒体矩阵' },
  { icon: '💡', name: '知乎专业问答矩阵', tag: '深度决策背书' },
  { icon: '📱', name: '抖音同城生活圈', tag: '移动端切面召回' },
  { icon: '🍽️', name: '大众点评实体图谱', tag: '消费实体锚点' }
];

// 范式转移滑块
const currentSlideIndex = ref(0);
const slideProgress = ref(0);
let slideTimer = null;
let progressTimer = null;

const shiftSlides = [
  {
    number: '01',
    shortTitle: '可见度隐形',
    tag: '可见度革命 · VISIBILITY',
    headline: '您的品牌在 AI 时代彻底隐形？在对话流中抢占第一提及率',
    description: '传统搜索用户翻阅 10 条链接，企业还能靠长尾词捡漏；AI 时代每次只直接输出 1~3 个推荐实体。若未注入知识图谱 Schema 结构化实体，您的品牌在 5 亿客户面前等同于“不存在”。',
    points: [
      '百度百科权威词条与知识图谱 Schema 唯一标识确权',
      '攻破主流大模型底层 RAG 知识检索库，确立企业法定知识锚点',
      '让每一次“哪家好”、“知名品牌”的提问，都稳居首选第一梯队'
    ],
    visualBadge: '大模型实体召回率',
    metricNum: '92%',
    metricUnit: '首推胜率',
    metricLabel: '行业权威首推率跃升',
    oldState: '仅有官网，大模型知识库完全空白，提及率为 0%',
    newState: 'Schema本体确权，5大模型稳居首选推荐位 (92%)'
  },
  {
    number: '02',
    shortTitle: '客源被截流',
    tag: '意图防御 · TRAFFIC & DEFENSE',
    headline: '搜索习惯转向 AI，您的潜在客源正被竞品无声截流',
    description: '当企业采购决策者在手机端豆包或 DeepSeek 询问“选哪家靠谱”、“避坑指南”时，竞争对手早已通过权威研报公域投喂完成霸屏拦截，您的订单在决策第一步就被掠夺殆尽。',
    points: [
      '深度扫描 50+ 个行业高频采购拦截意图词库',
      '反制竞品恶意单向对比，扭转大模型偏见评价',
      '在买家产生意向的黄金 3 秒内，锁定专属品牌信任链路'
    ],
    visualBadge: '意图拦截防御率',
    metricNum: '+340%',
    metricUnit: '挽回订单',
    metricLabel: '高意向采购线索回流',
    oldState: '采购提问被同行竞品全量拦截，客户严重流失',
    newState: '构建高权重测评公域矩阵，将采购需求定向截流至贵司'
  },
  {
    number: '03',
    shortTitle: '获客成本失控',
    tag: '效率飞跃 · EFFICIENCY & ROI',
    headline: '传统竞价单次点击翻倍，构建 0 持续边际成本的 GEO 护城河',
    description: '百度竞价与信息流单次点击费用逐年暴涨，且停充即停流；GEO 沉淀的是公域中不可篡改的永久知识资产，一次建设，长效享受全网基座大模型的免费精准推荐。',
    points: [
      '摆脱无底洞式的关键词竞价点击扣费陷阱',
      '权威媒体研报与百科资产永久收录，不随时间被轻易稀释',
      '边际获客成本趋近于 0，构筑同行业极具抗周期的增长壁垒'
    ],
    visualBadge: '单次提问边际成本',
    metricNum: '￥0',
    metricUnit: '单次扣费',
    metricLabel: '永久知识资产复利',
    oldState: '每次点击扣费 30~80 元，停充流量瞬间归零',
    newState: '知识沉淀为大模型内生记忆，无需持续支付提问费'
  },
  {
    number: '04',
    shortTitle: '三重飞轮',
    tag: '全域增长 · THE TRIPLE EFFECT',
    headline: '流量 · 声誉 · 成交：构建企业生成式推荐的全链路增长飞轮',
    description: 'GEO 不仅是简单的名词排位，更是企业在 AI 心智中的全方位声誉重塑。从知识本体的确立，到第三方权威公信力的背书，再到商业订单的自然水到渠成。',
    points: [
      '双端（移动端同城生活圈 + PC端权威知识库）双切面协同覆盖',
      '24/7 自动化雷达巡检，实时预警大模型知识漂移与竞品反扑',
      '30 天确定性闭环交付，以权威索引链接与体检报告作为铁证验收'
    ],
    visualBadge: '交付确定性闭环',
    metricNum: '30天',
    metricUnit: '全量达标',
    metricLabel: '四层认知体系落地上线',
    oldState: '盲目投放软文，无体系、无监测、无确定性结果',
    newState: '四层认知工程体系 + 24/7 攻防雷达长期护航'
  }
];

const currentSlide = computed(() => shiftSlides[currentSlideIndex.value]);

function switchSlide(idx) {
  currentSlideIndex.value = idx;
  slideProgress.value = 0;
  restartSlideTimer();
}

function startSlideLoop() {
  progressTimer = setInterval(() => {
    if (slideProgress.value < 100) {
      slideProgress.value += 2;
    }
  }, 100);

  slideTimer = setInterval(() => {
    currentSlideIndex.value = (currentSlideIndex.value + 1) % shiftSlides.length;
    slideProgress.value = 0;
  }, 5000);
}

function restartSlideTimer() {
  if (slideTimer) clearInterval(slideTimer);
  if (progressTimer) clearInterval(progressTimer);
  startSlideLoop();
}

onMounted(() => {
  startSlideLoop();
});

onUnmounted(() => {
  if (placeholderTimer) clearInterval(placeholderTimer);
  if (slideTimer) clearInterval(slideTimer);
  if (progressTimer) clearInterval(progressTimer);
  if (scrollObserver) scrollObserver.disconnect();
});

// 行业解决方案
const activeIndustryIndex = ref(0);

const industries = [
  {
    id: 'b2b',
    name: '工业设备制造',
    icon: '🏭',
    category: '工业装备制造 · B2B高客单决策',
    defaultBrand: '恒瑞智能装备',
    headline: '打破工业装备行业龙头垄断，在 AI 采购选型横评中稳居前二推荐位',
    scenarioQuery: '“无锡光纤激光切管机生产厂家推荐哪家质量好性价比高？”',
    painPoint: '高客单装备客户决策链路长，极度依赖权威资质与同行横评。未优化前公域空白，采购提问被龙头大族、宏山全额拦截。',
    tactics: [
      '建立国家工信部专精特新认证与国家专利储备 Schema 实体标签',
      '在搜狐科技与机械行业垂直媒体定向发布 18 篇深度技术测评研报',
      '抢占“重管切割哪家好”、“激光切管机选型避坑”等 50+ 个采购拦截词'
    ],
    statValue: '+340%',
    statDesc: 'AI 意图推荐爆发 · 月度挽回约 24 万潜在设备订单',
    preRate: '0% (完全隐形)',
    postRate: '92% (首推梯队)',
    clientQuote: '以前客户采购几十万的切管机在豆包搜横评，推荐的都是龙头。做完GEO后，豆包直接把我们列为华东重管首选推荐，当月就有两台意向客户主动加微信！',
    clientAvatar: '👨‍💼',
    clientName: '张总 (无锡恒瑞智能装备)',
    clientTitle: '市场营销副总裁'
  },
  {
    id: 'window',
    name: '高端系统门窗',
    icon: '🪟',
    category: '大宅定制与家居建材',
    defaultBrand: '佳豪系统门窗',
    headline: '突破传统建材卖场瓶颈，在同城手机生活圈截获大宅业主直接咨询',
    scenarioQuery: '“本地高端断桥铝系统门窗十大品牌实力排名与避坑指南”',
    painPoint: '大宅装修业主决策前习惯在手机端搜索“系统门窗选哪家靠谱”。过去同行皇派大量霸屏，区域优质品牌面临严重客源失血。',
    tactics: [
      '双端切面协同：打通手机端生活圈同城实录与真实业主装修评价',
      'PC端沉淀门窗五金水密性、隔音国标参数与行业横评长文',
      '在豆包“本地线下机构/服务商对比”中稳居前二，打消小作坊质量顾虑'
    ],
    statValue: '￥180,000',
    statDesc: '月度挽回大宅业主订单资产 · 获客成本下降 68%',
    preRate: '12% (被动收录)',
    postRate: '89% (同城首推)',
    clientQuote: '商场进店客流越来越少，年轻业主全部用大模型搜避坑。把水密国标和本地案例喂给大模型后，现在客户进店就说“AI推荐你们做大宅封窗靠谱”！',
    clientAvatar: '🏡',
    clientName: '李总 (佛山佳豪系统门窗)',
    clientTitle: '品牌创始人'
  },
  {
    id: 'catering',
    name: '连锁餐饮加盟',
    icon: '🍲',
    category: '现代连锁消费与招商',
    defaultBrand: '老乡鸡',
    headline: '抢占全国快餐第一提及率，招商加盟与堂食口碑双爆发',
    scenarioQuery: '“全国中式快餐连锁加盟哪个品牌扶持政策好存活率高？”',
    painPoint: '餐饮加盟竞争极度激烈，投资者向 AI 咨询选型时，AI 只采信大众点评与高权重财经媒体多维度背书的成熟品牌。',
    tactics: [
      '在知乎专业问答与财经门户沉淀供应链支持、门店存活率客观研报',
      '打通大众点评店铺矩阵与高权重美食媒体权威背书实体',
      '在千问与元宝的商业决策对比矩阵中，被列为标准化成熟度最高推荐'
    ],
    statValue: '+180%',
    statDesc: '全国加盟意向线索增长 · 招商成交转化周期缩短 45%',
    preRate: '18% (边缘提及)',
    postRate: '94% (首选标杆)',
    clientQuote: '现在加盟商极为理智，先用千问把加盟政策和倒闭率扒个底朝天。帮我们建立公信力数据资产后，AI 回答全是中央厨房和冷链优势，谈单轻松太多了。',
    clientAvatar: '🍲',
    clientName: '陈总 (知名连锁快餐总部)',
    clientTitle: '全国招商总监'
  },
  {
    id: 'medical',
    name: '专科医疗齿科',
    icon: '🦷',
    category: '大健康与高净值专科',
    defaultBrand: '恒伦口腔',
    headline: '重塑种植牙声誉，化解公域负面疑虑，首诊预约提升 150%',
    scenarioQuery: '“本地种植牙哪家专科医院技术靠谱收费透明无隐形增项？”',
    painPoint: '患者在选择机构时必定深挖合规资质、医生资历与价格透明度。公域资产单薄会导致患者直接流向公立医院。',
    tactics: [
      '深度覆盖企查查医疗合规公示与卫健委执业医师备案真实引用',
      '在知乎与权威健康门户发布种植牙集采避坑指南与数字化导板横评',
      '大模型回答中明确标识“资质合规、收费透明”，成为同城首诊推荐'
    ],
    statValue: '150%',
    statDesc: '高客单数字化种植牙首诊预约提升 · 消除患者信任壁垒',
    preRate: '8% (信任缺失)',
    postRate: '86% (权威推荐)',
    clientQuote: '患者最怕过度消费。大模型把卫健委备案和明码标价直接引述出来，相当于权威机构替我们做了背书，转化率非常惊人！',
    clientAvatar: '🦷',
    clientName: '王院长 (数字化口腔专科门诊)',
    clientTitle: '业务院长'
  },
  {
    id: 'legal',
    name: '商务律所咨询',
    icon: '⚖️',
    category: '高端专业服务与合规',
    defaultBrand: '金杜律所',
    headline: '打破传统熟人介绍局限，在大模型企业采购决策流中直获常法委托',
    scenarioQuery: '“企业常年法律顾问与复杂商事纠纷解决律所哪家专业？”',
    painPoint: '企业法务与总经理常直接用 AI 快速检索律所胜诉率与团队背景。缺乏深度案例背书将被传统头部大所无情截流。',
    tactics: [
      '定向发布行业重大商事经典判例研报，建立包含胜诉率的高权重词条',
      '沉淀专业委员会任职、知识产权与股权设计专家知识实体',
      '通义千问与 DeepSeek 商业评测中，以高响应度重点推介给企业'
    ],
    statValue: '￥210,000',
    statDesc: '单月新增 3 家企业常年法律顾问委托 · 建立行业专家权威',
    preRate: '5% (无实体背书)',
    postRate: '91% (专家首选)',
    clientQuote: '许多拟上市企业的董秘和法务用通义千问寻找擅长股权合规的律所，AI 把胜诉案例列在第一位，直接为我们带来了两家优质企业客户！',
    clientAvatar: '⚖️',
    clientName: '周律师 (知名商事律所)',
    clientTitle: '高级合伙人'
  }
];

const currentIndustry = computed(() => industries[activeIndustryIndex.value]);

// 四层认知工程架构
const archLayers = [
  {
    icon: '🏷️',
    name: '知识本体确权工程',
    enName: 'Schema & Entity Ontology',
    desc: '在权威词条完成认证，注入 Schema.org 知识图谱结构化标记，确立大模型 RAG 召回的唯一法定身份。',
    items: [
      '企业本体词条全量认证过审',
      'Schema.org 知识图谱元数据注入',
      '排除歧义同名实体干扰'
    ]
  },
  {
    icon: '📰',
    name: '权威信源公信力矩阵',
    enName: 'Authority Citation Feeder',
    desc: '穿透搜狐、新浪、网易、知乎等高权重门户，定向投喂 15~20 篇客观专业测评研报，建立可信证据链。',
    items: [
      '大模型高权重引爆炸点媒体矩阵',
      '第三方客观横评与真实案例背书',
      '权威索引长期保留与反稀释'
    ]
  },
  {
    icon: '🎯',
    name: '采购意图精准拦截',
    enName: 'Intent Interception Grid',
    desc: '围绕“哪家好”、“选型对比”、“避坑评测”等 50+ 行业高频意向词，构建标准化问答库，抢占第一梯队。',
    items: [
      '50+ 行业采购决策意向词覆盖',
      '反制竞品恶意单向对比霸屏',
      '大模型首推胜率稳定 85% 以上'
    ]
  },
  {
    icon: '📡',
    name: '双端攻防全天候雷达',
    enName: 'Dual-End Telemetry Radar',
    desc: '手机端生活圈 + PC 知识库切面 24/7 自动化巡检，实时预警大模型更新、知识漂移与竞品反扑。',
    items: [
      '覆盖 5 大基座大模型双端切面',
      '每周自动化巡检报表推送',
      '算法更新与模型漂移秒级预警'
    ]
  }
];

// 30 天闭环交付体系
const roadmapSteps = [
  {
    phase: '01',
    days: 'Day 1 - Day 7',
    title: '品牌专有词确权与 Schema 结构化注入',
    action: '建立专属企业本体实体，完成百科词条认证及 Schema.org 结构化标记，建立大模型 RAG 召回根基。',
    deliverable: '《企业知识本体架构书》、官方百科词条过审、Schema 实体认证'
  },
  {
    phase: '02',
    days: 'Day 8 - Day 15',
    title: '主流高权重权威信源矩阵定向投喂',
    action: '针对 DeepSeek、豆包、通义千问优先采信的核心门户，定向发布 15~20 篇深度技术测评研报。',
    deliverable: '国家级/行业高权重媒体收录链接清单、外链索引报告、第三方权威背书'
  },
  {
    phase: '03',
    days: 'Day 16 - Day 22',
    title: '行业高频意向词与长尾对比词精准拦截',
    action: '围绕“哪家好”、“口碑推荐”、“选型对比”等 50+ 个采购场景构建标准 QA 问答库，抢占第一推荐位。',
    deliverable: '《行业采购意向拦截词库》、多轮问答覆盖表、竞品对比反制策略库'
  },
  {
    phase: '04',
    days: 'Day 23 - Day 30',
    title: '双端多平台自动化复测与雷达大屏开通',
    action: '对豆包、DeepSeek、千问、元宝等 10 大双端切面执行全量自动化巡检，出具终审报表并交付雷达大屏。',
    deliverable: '《GEO 优化终审成果报表》、开通【蜉蝣小宝 · 交付期数据监控看板】账号'
  }
];

// 商业账本数据
const roiRows = [
  {
    dimension: '计费扣费模式',
    sem: '按次扣费，单次 10~80 元，恶意点击难防',
    seo: '按月外包，排名波动频繁且见效极慢',
    geo: '一次构筑知识工程体系，0 单次提问点击费'
  },
  {
    dimension: '流量与决策质量',
    sem: '用户对“广告”标签天生防备，跳出率高',
    seo: '传统搜索流量年下滑 30% 以上，被大模型分流',
    geo: 'AI 深度推理回答，具备极高公信力，转化意向强'
  },
  {
    dimension: '资产时效与持久度',
    sem: '账户余额扣尽瞬间流量归零，停充即停流',
    seo: '极易因搜索引擎算法调整被一夜降权',
    geo: '内生化为大模型底层训练与知识外链，长效享受复利'
  },
  {
    dimension: '意向拦截效果',
    sem: '无法干预大模型自然语言对话流中的推荐内容',
    seo: '仅能在传统十条网页链接中被动排列',
    geo: '在“哪家好/选型对比”意图提问中占据唯一首选推荐'
  },
  {
    dimension: '抗周期壁垒',
    sem: '竞品只要出价更高即可强行压制贵司展现',
    seo: '缺乏权威公信力背书，容易被同行泛滥站群超越',
    geo: '权威百科+国家专利+第三方深度研报，竞品极难反超'
  }
];

// FAQ
const openFaqIndex = ref(0);
function toggleFaq(idx) {
  openFaqIndex.value = openFaqIndex.value === idx ? -1 : idx;
}

const faqs = [
  {
    question: 'GEO 与传统 SEO 有什么本质区别？',
    answer: '传统 SEO 争夺的是网页在搜索引擎列表中的点击位，依赖关键词堆砌；而 GEO 是面向大模型推荐机制的认知工程。它通过知识本体确权（Schema+百科）和权威高权重媒体公信力矩阵投喂，让大模型在理解用户自然语言问题（如“推荐一家靠谱的切管机厂家”）时，把您的品牌作为经过深度验证的答案推荐给用户。'
  },
  {
    question: '大模型更新这么快，优化后的效果会被覆盖或失效吗？',
    answer: '不会。大模型的自然语言检索（RAG 架构）每次回答问题时，都会实时召回公网中权重最高、公信力最强、被多家权威媒体交叉引用的信源。蜉蝣小宝为企业注入的是符合工信部、国家知识产权局及搜狐、新浪等国家级媒体标准的深度专业研报与官方百科实体。只要底层知识资产在公域稳固存在，大模型就会长期将其作为可信答案输出。'
  },
  {
    question: '为什么必须同时覆盖“手机端生活圈”与“PC端知识库”双端切面？',
    answer: '因为中国主流大模型（特别是字节跳动·豆包）在不同终端的召回逻辑完全不同。手机端豆包优先聚合抖音同城生活圈、大众点评、本地服务商实体；而 PC 端与 DeepSeek 则优先检索知乎长文、行业研报与企业官方知识库。双端协同探测方能杜绝“电脑端查得到、手机端完全隐形”的漏洞。'
  },
  {
    question: '企业做一次 AI 体检需要多长时间？需要我们提供什么？',
    answer: '直连实测仅需 10~15 秒！您只需在工作台输入企业名称、品牌名和核心业务，系统即可自动调用五大主流大模型接口进行实时探针扫描，出具穿透级的《企业 AI 可见度体检书》，包含客源流失测算、竞品截流深度及改善建议。'
  }
];
</script>

<style scoped>
/* ================= 全局暗黑深空主题 (Similarweb DarkHomePage) ================= */
.landing-container {
  min-height: 100vh;
  background-color: #080C14;
  color: #F1F5F9;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  overflow-x: hidden;
  position: relative;
}

/* ================= 滚动渐显渐隐系统 (Scroll-driven Reveal & Fade-out) ================= */
.scroll-reveal {
  opacity: 0;
  transform: translateY(36px) scale(0.99);
  filter: blur(6px);
  transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.85s cubic-bezier(0.16, 1, 0.3, 1),
              filter 0.85s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform, filter;
}

.scroll-reveal.is-revealed {
  opacity: 1;
  transform: translateY(0) scale(1);
  filter: blur(0px);
}

.scroll-reveal.is-exited-top {
  opacity: 0.18;
  transform: translateY(-24px) scale(0.99);
  filter: blur(4px);
}

.delay-1 { transition-delay: 0.08s; }
.delay-2 { transition-delay: 0.16s; }
.delay-3 { transition-delay: 0.24s; }
.delay-4 { transition-delay: 0.32s; }
.delay-5 { transition-delay: 0.40s; }

/* ================= 1. 顶部公告彩带 ================= */
.top-promo-ribbon {
  background: linear-gradient(89.84deg, #195AFE 0.13%, #3A56E8 37.72%, #B4528C 72.54%, #FF6D03 88.92%, #FF9603 99.86%);
  padding: 0.52rem 1.5rem;
  font-size: 0.84rem;
  color: #ffffff;
  position: relative;
  z-index: 101;
}

.ribbon-inner {
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.ribbon-pill {
  background: rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(8px);
  padding: 0.15rem 0.6rem;
  border-radius: 9999px;
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.ribbon-text strong {
  font-weight: 700;
}

.ribbon-link {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  color: #ffffff;
  text-decoration: underline;
  text-underline-offset: 3px;
  font-weight: 600;
  transition: opacity 0.2s;
}

.ribbon-link:hover {
  opacity: 0.85;
}

.ribbon-arrow {
  transition: transform 0.2s;
}

.ribbon-link:hover .ribbon-arrow {
  transform: translateX(3px);
}

/* ================= 2. 悬浮磨砂暗黑导航栏 ================= */
.landing-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(8, 12, 20, 0.82);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding: 0.8rem 2rem;
}

.header-inner {
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* 左上角品牌链接：舒展、大气、无拘束 */
.brand-link {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
  cursor: pointer;
}

.logo-aura-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 柔和无边框深空光晕：不框住 logo，让其自由发光 */
.logo-soft-glow {
  position: absolute;
  inset: -12px -20px;
  background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.5) 0%, rgba(168, 85, 247, 0.25) 50%, transparent 72%);
  filter: blur(14px);
  pointer-events: none;
  opacity: 0.75;
  transition: opacity 0.3s ease;
}

.brand-link:hover .logo-soft-glow {
  opacity: 1;
}

/* 品牌原标：完整大图自然展现，不锁在小方格内 */
.logo-unconstrained {
  position: relative;
  height: 38px;
  width: auto;
  max-width: 155px;
  object-fit: contain;
  filter: drop-shadow(0 2px 12px rgba(25, 90, 254, 0.4));
  transition: transform 0.25s ease;
}

.brand-link:hover .logo-unconstrained {
  transform: scale(1.04);
}

.brand-badge-tag {
  background: linear-gradient(135deg, #195AFE, #7C3AED);
  color: #ffffff;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 0.18rem 0.55rem;
  border-radius: 6px;
  letter-spacing: 0.5px;
  box-shadow: 0 0 12px rgba(25, 90, 254, 0.45);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 1.6rem;
}

.nav-item {
  color: #94A3B8;
  text-decoration: none;
  font-size: 0.92rem;
  font-weight: 500;
  transition: all 0.2s ease;
  position: relative;
  padding: 0.25rem 0;
}

.nav-item:hover {
  color: #ffffff;
}

.nav-item:hover::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #195AFE, #A855F7);
  border-radius: 2px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.btn-ghost-nav {
  color: #CBD5E1;
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
  padding: 0.45rem 0.85rem;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  transition: all 0.2s;
  background: rgba(255, 255, 255, 0.03);
}

.btn-ghost-nav:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.25);
  color: #ffffff;
}

.btn-primary-nav {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  padding: 0.48rem 1.15rem;
  border-radius: 9999px;
  font-size: 0.88rem;
  font-weight: 700;
  color: #ffffff;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(25, 90, 254, 0.4);
  background: linear-gradient(135deg, #195AFE 0%, #3B82F6 50%, #A855F7 100%);
  transition: all 0.3s ease;
}

.btn-primary-nav:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 28px rgba(25, 90, 254, 0.65);
}

.btn-glow-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
  transform: translateX(-100%);
  transition: transform 0.6s ease;
}

.btn-primary-nav:hover .btn-glow-bg {
  transform: translateX(100%);
}

.btn-text {
  position: relative;
  z-index: 1;
}

/* ================= 3. Hero Section ================= */
.hero-section {
  position: relative;
  padding: 5rem 1.5rem 5.5rem;
  overflow: hidden;
  background: #080C14;
}

.ambient-glow {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(120px);
}

.orb-blue {
  width: 580px;
  height: 580px;
  top: -120px;
  left: -80px;
  background: radial-gradient(circle, rgba(25, 90, 254, 0.22) 0%, transparent 70%);
}

.orb-purple {
  width: 620px;
  height: 620px;
  top: 10%;
  right: -100px;
  background: radial-gradient(circle, rgba(168, 85, 247, 0.18) 0%, transparent 70%);
}

.orb-orange {
  width: 520px;
  height: 520px;
  bottom: -40px;
  left: 28%;
  background: radial-gradient(circle, rgba(255, 109, 3, 0.12) 0%, transparent 70%);
}

.grid-overlay {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
  mask-image: radial-gradient(circle at center, black 40%, transparent 80%);
}

.section-inner {
  max-width: 1280px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.hero-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.hero-pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: rgba(25, 90, 254, 0.12);
  border: 1px solid rgba(25, 90, 254, 0.35);
  padding: 0.38rem 1.15rem;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #93C5FD;
  margin-bottom: 2rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 0 18px rgba(25, 90, 254, 0.2);
}

.badge-dot-live {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #10B981;
  box-shadow: 0 0 8px #10B981;
  animation: pulseDot 2s infinite;
}

@keyframes pulseDot {
  0% { transform: scale(0.9); opacity: 0.8; }
  50% { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.8; }
}

.hero-headline {
  font-size: 3.8rem;
  font-weight: 900;
  line-height: 1.22;
  letter-spacing: -1.2px;
  color: #ffffff;
  margin: 0 0 1.4rem 0;
  max-width: 980px;
}

.text-gradient {
  background: linear-gradient(135deg, #60A5FA 0%, #C084FC 50%, #FB923C 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtext {
  font-size: 1.15rem;
  line-height: 1.75;
  color: #94A3B8;
  max-width: 780px;
  margin: 0 0 2.8rem 0;
}

.hero-search-wrapper {
  width: 100%;
  max-width: 860px;
  margin-bottom: 3.8rem;
}

.search-input-box {
  position: relative;
  display: flex;
  align-items: center;
  background: rgba(15, 22, 38, 0.82);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 9999px;
  padding: 0.45rem 0.55rem 0.45rem 1.4rem;
  box-shadow: 0 14px 45px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(25, 90, 254, 0.25);
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}

.search-input-box:focus-within {
  border-color: #3B82F6;
  box-shadow: 0 18px 55px rgba(0, 0, 0, 0.6), 0 0 28px rgba(59, 130, 246, 0.45);
}

.search-mode-select {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #CBD5E1;
  font-size: 0.88rem;
  font-weight: 600;
  white-space: nowrap;
  user-select: none;
}

.mode-caret {
  color: #64748B;
  font-size: 0.75rem;
}

.search-divider {
  width: 1px;
  height: 22px;
  background: rgba(255, 255, 255, 0.15);
  margin: 0 1rem;
}

.search-input-field {
  flex: 1;
}

.search-input-field input {
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  color: #ffffff;
  font-size: 1.02rem;
  font-weight: 500;
}

.search-input-field input::placeholder {
  color: #64748B;
  transition: color 0.3s;
}

.btn-search-action {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #195AFE 0%, #3B82F6 45%, #8B5CF6 100%);
  border: none;
  border-radius: 9999px;
  padding: 0.82rem 1.8rem;
  color: #ffffff;
  font-size: 0.96rem;
  font-weight: 700;
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 0 24px rgba(25, 90, 254, 0.5);
  transition: all 0.3s ease;
  white-space: nowrap;
}

.btn-search-action:hover {
  transform: scale(1.03);
  box-shadow: 0 0 32px rgba(25, 90, 254, 0.75);
}

.action-content {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  position: relative;
  z-index: 1;
}

.quick-chips-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.chips-label {
  font-size: 0.82rem;
  color: #64748B;
  font-weight: 500;
}

.chip-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #CBD5E1;
  font-size: 0.8rem;
  font-weight: 500;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 0.2s;
}

.chip-btn:hover {
  background: rgba(25, 90, 254, 0.15);
  border-color: rgba(25, 90, 254, 0.4);
  color: #93C5FD;
  transform: translateY(-1px);
}

.trust-metrics-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.4rem;
  margin-top: 1.6rem;
  flex-wrap: wrap;
}

.trust-metric {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #94A3B8;
  font-size: 0.84rem;
  font-weight: 500;
}

.trust-metric-dot {
  width: 4px;
  height: 4px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
}

/* ================= 4. 首屏高科技画报 ================= */
.hero-dashboard-mockup {
  width: 100%;
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 20px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.75), 0 0 50px rgba(25, 90, 254, 0.15);
  overflow: hidden;
  text-align: left;
}

.mockup-window-header {
  background: #090E1A;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding: 0.75rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.window-controls {
  display: flex;
  align-items: center;
  gap: 6px;
}

.window-dot {
  width: 11px;
  height: 11px;
  border-radius: 50%;
}

.dot-red { background: #EF4444; }
.dot-yellow { background: #F59E0B; }
.dot-green { background: #10B981; }

.window-address-bar {
  flex: 1;
  max-width: 460px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 0.3rem 0.85rem;
  font-size: 0.75rem;
  color: #94A3B8;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: monospace;
}

.window-status-pill {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.76rem;
  font-weight: 600;
  color: #6EE7B7;
  background: rgba(16, 185, 129, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  border: 1px solid rgba(16, 185, 129, 0.25);
}

.pulse-green {
  width: 6px;
  height: 6px;
  background: #10B981;
  border-radius: 50%;
  box-shadow: 0 0 6px #10B981;
}

.mockup-window-body {
  display: grid;
  grid-template-columns: 1.45fr 1fr;
  gap: 1.5rem;
  padding: 1.8rem;
}

.comparison-panel {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.panel-top-tabs {
  display: flex;
  gap: 0.6rem;
  background: rgba(255, 255, 255, 0.03);
  padding: 0.35rem;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.compare-tab {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  padding: 0.55rem 0.85rem;
  border-radius: 8px;
  border: 1px solid transparent;
  background: transparent;
  color: #94A3B8;
  font-size: 0.84rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.compare-tab.active {
  background: #162035;
  color: #ffffff;
  border-color: rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.tab-indicator {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.tab-indicator.green { background: #10B981; box-shadow: 0 0 6px #10B981; }
.tab-indicator.red { background: #EF4444; box-shadow: 0 0 6px #EF4444; }

.chat-query-pill {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 0.75rem 1rem;
}

.query-avatar {
  font-size: 1.1rem;
}

.query-meta {
  font-size: 0.72rem;
  color: #64748B;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.2rem;
}

.query-str {
  font-size: 0.94rem;
  font-weight: 600;
  color: #E2E8F0;
}

.ai-response-box {
  background: rgba(13, 20, 36, 0.9);
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.ai-response-box.state-after {
  border-color: rgba(16, 185, 129, 0.3);
  box-shadow: 0 0 30px rgba(16, 185, 129, 0.08);
}

.ai-response-box.state-before {
  border-color: rgba(239, 68, 68, 0.3);
  box-shadow: 0 0 30px rgba(239, 68, 68, 0.08);
}

.ai-box-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.ai-brand-badge {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.82rem;
  font-weight: 700;
  color: #CBD5E1;
}

.ai-rank-tag {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 9999px;
}

.ai-rank-tag.gold {
  background: rgba(245, 158, 11, 0.15);
  color: #FBBF24;
  border: 1px solid rgba(245, 158, 11, 0.3);
}

.ai-rank-tag.red {
  background: rgba(239, 68, 68, 0.15);
  color: #F87171;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.highlight-brand-card {
  background: rgba(25, 90, 254, 0.08);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 10px;
  padding: 1rem;
}

.h-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.h-name {
  font-size: 0.98rem;
  font-weight: 800;
  color: #60A5FA;
}

.h-score {
  font-size: 0.78rem;
  font-weight: 700;
  color: #34D399;
  background: rgba(16, 185, 129, 0.15);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.h-card-desc {
  font-size: 0.84rem;
  color: #CBD5E1;
  line-height: 1.6;
  margin-bottom: 0.8rem;
}

.h-citation-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.cite-tag {
  font-size: 0.72rem;
  color: #93C5FD;
  background: rgba(25, 90, 254, 0.15);
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  border: 1px solid rgba(25, 90, 254, 0.25);
}

.competitor-brand-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  padding: 0.85rem;
}

.c-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: #E2E8F0;
  margin-bottom: 0.3rem;
}

.c-desc {
  font-size: 0.8rem;
  color: #94A3B8;
  line-height: 1.5;
}

.leak-alert-card {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: 8px;
  padding: 0.85rem 1rem;
  margin-top: 0.5rem;
}

.alert-icon {
  font-size: 1.2rem;
}

.alert-text {
  font-size: 0.82rem;
  color: #FCA5A5;
  line-height: 1.5;
}

.alert-text strong {
  color: #EF4444;
}

.telemetry-panel {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.telemetry-card {
  background: rgba(13, 20, 36, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 1.15rem;
}

.card-header-clean {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.85rem;
}

.card-label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #94A3B8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-badge.excellent {
  background: rgba(16, 185, 129, 0.15);
  color: #34D399;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.55rem;
  border-radius: 9999px;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.gauge-display {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}

.gauge-circle {
  width: 78px;
  height: 78px;
  border-radius: 50%;
  border: 3px solid #10B981;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.35);
  background: rgba(16, 185, 129, 0.05);
}

.gauge-num {
  font-size: 1.55rem;
  font-weight: 900;
  color: #ffffff;
  line-height: 1;
}

.gauge-unit {
  font-size: 0.68rem;
  color: #6EE7B7;
  font-weight: 600;
}

.gauge-meta {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  font-size: 0.78rem;
  color: #94A3B8;
}

.meta-row {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.meta-row.highlight {
  color: #C084FC;
  font-weight: 700;
}

.trend-pill {
  font-size: 0.72rem;
  font-weight: 700;
  color: #FB923C;
  background: rgba(251, 146, 60, 0.15);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.leads-val-row {
  display: flex;
  align-items: baseline;
  gap: 0.2rem;
  margin-bottom: 0.4rem;
}

.leads-val-row .currency {
  font-size: 1.2rem;
  font-weight: 800;
  color: #F59E0B;
}

.leads-val-row .number {
  font-size: 1.95rem;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: -0.5px;
}

.leads-val-row .period {
  font-size: 0.85rem;
  color: #94A3B8;
  margin-left: 0.3rem;
}

.leads-note {
  font-size: 0.75rem;
  color: #64748B;
  line-height: 1.5;
  margin: 0;
}

.radar-live-text {
  font-size: 0.72rem;
  color: #60A5FA;
  font-weight: 600;
}

.model-bars-list {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.model-bar-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.bar-info {
  display: flex;
  justify-content: space-between;
  font-size: 0.76rem;
  color: #CBD5E1;
  font-weight: 600;
}

.bar-track {
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 9999px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #195AFE, #A855F7);
  border-radius: 9999px;
  box-shadow: 0 0 8px rgba(168, 85, 247, 0.5);
}

/* ================= 5. 跑马灯生态 (大幅提升字号与卡片尺寸，醒目清晰) ================= */
.marquee-section {
  padding: 4.5rem 0 5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  background: #060910;
  overflow: hidden;
  position: relative;
}

.marquee-header-wrap {
  text-align: center;
  margin-bottom: 2.6rem;
}

.marquee-title-row {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  flex-wrap: wrap;
  justify-content: center;
}

.marquee-pulse-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 10px #10B981;
  animation: pulseDot 2s infinite;
}

.marquee-title {
  font-size: 1.12rem;
  font-weight: 800;
  color: #E2E8F0;
  letter-spacing: 0.5px;
  margin: 0;
}

.marquee-sub-note {
  font-size: 0.82rem;
  color: #64748B;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.2rem 0.65rem;
  border-radius: 9999px;
  font-weight: 500;
}

.marquee-wrapper {
  display: flex;
  width: 100%;
  overflow: hidden;
  padding: 0.5rem 0;
  mask-image: linear-gradient(to right, transparent, black 8%, black 92%, transparent);
}

.marquee-track {
  display: flex;
  align-items: center;
  gap: 2rem;
  white-space: nowrap;
  animation: marqueeScroll 40s linear infinite;
}

.marquee-wrapper:hover .marquee-track {
  animation-play-state: paused;
}

@keyframes marqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* 跑马灯大卡片：大图标、大字号、高对比度、清晰不费力 */
.marquee-card {
  display: inline-flex;
  align-items: center;
  gap: 1.1rem;
  background: rgba(15, 22, 38, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.14);
  padding: 1rem 1.8rem;
  border-radius: 18px;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(12px);
  cursor: pointer;
  transition: all 0.25s ease;
}

.marquee-card:hover {
  background: #162035;
  border-color: rgba(59, 130, 246, 0.6);
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 16px 36px rgba(25, 90, 254, 0.35);
}

.card-icon-halo {
  font-size: 2.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.card-text-block {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.card-main-name {
  font-size: 1.18rem;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.2px;
}

.card-sub-tag {
  font-size: 0.84rem;
  font-weight: 600;
  color: #93C5FD;
  background: rgba(25, 90, 254, 0.15);
  padding: 0.15rem 0.55rem;
  border-radius: 6px;
  border: 1px solid rgba(25, 90, 254, 0.25);
  width: fit-content;
}

.card-live-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 8px #10B981;
  margin-left: 0.3rem;
}

/* ================= 6. 范式转移滑块 ================= */
.shift-section {
  padding: 6rem 1.5rem;
  position: relative;
  background: #080C14;
}

.section-header-center {
  text-align: center;
  max-width: 840px;
  margin: 0 auto 3.5rem auto;
}

.section-badge {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: #60A5FA;
  background: rgba(25, 90, 254, 0.12);
  border: 1px solid rgba(25, 90, 254, 0.25);
  padding: 0.3rem 0.9rem;
  border-radius: 9999px;
  margin-bottom: 1.2rem;
}

.section-title {
  font-size: 2.75rem;
  font-weight: 900;
  line-height: 1.25;
  letter-spacing: -0.8px;
  color: #ffffff;
  margin: 0 0 1.2rem 0;
}

.section-sub {
  font-size: 1.05rem;
  color: #94A3B8;
  line-height: 1.7;
  margin: 0;
}

.shift-slider-container {
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6);
}

.slider-tabs-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  background: #0A0F1D;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.slider-tab-btn {
  background: transparent;
  border: none;
  padding: 1.2rem 1.2rem 1.4rem;
  text-align: left;
  cursor: pointer;
  position: relative;
  transition: all 0.2s;
}

.slider-tab-btn:hover {
  background: rgba(255, 255, 255, 0.02);
}

.tab-progress-track {
  width: 100%;
  height: 3px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 9999px;
  margin-bottom: 0.8rem;
  overflow: hidden;
}

.tab-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #195AFE, #A855F7);
  transition: width 0.1s linear;
}

.tab-header-content {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.tab-index {
  font-size: 0.8rem;
  font-weight: 800;
  color: #64748B;
}

.slider-tab-btn.active .tab-index {
  color: #60A5FA;
}

.tab-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #94A3B8;
}

.slider-tab-btn.active .tab-title {
  color: #ffffff;
}

.slider-card-body {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  gap: 3rem;
  padding: 3.5rem;
  align-items: center;
}

.slide-badge {
  font-size: 0.78rem;
  font-weight: 800;
  color: #F59E0B;
  letter-spacing: 1px;
  margin-bottom: 0.8rem;
}

.slide-headline {
  font-size: 1.85rem;
  font-weight: 800;
  line-height: 1.35;
  color: #ffffff;
  margin: 0 0 1.2rem 0;
}

.slide-desc {
  font-size: 0.98rem;
  color: #94A3B8;
  line-height: 1.7;
  margin: 0 0 1.8rem 0;
}

.slide-points-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 2.2rem;
}

.point-item {
  display: flex;
  align-items: flex-start;
  gap: 0.65rem;
  font-size: 0.92rem;
  color: #CBD5E1;
  line-height: 1.5;
}

.p-icon {
  color: #10B981;
  font-weight: 900;
}

.btn-slide-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #195AFE, #3B82F6);
  color: #ffffff;
  text-decoration: none;
  padding: 0.75rem 1.6rem;
  border-radius: 10px;
  font-size: 0.92rem;
  font-weight: 700;
  box-shadow: 0 4px 18px rgba(25, 90, 254, 0.4);
  transition: all 0.2s;
}

.btn-slide-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(25, 90, 254, 0.6);
}

.slide-content-right {
  display: flex;
  justify-content: center;
}

.slide-visual-card {
  width: 100%;
  background: #090E1A;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 1.8rem;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
}

.visual-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.v-pill {
  font-size: 0.75rem;
  font-weight: 700;
  color: #60A5FA;
  background: rgba(25, 90, 254, 0.15);
  padding: 0.2rem 0.65rem;
  border-radius: 4px;
}

.v-model {
  font-size: 0.75rem;
  color: #64748B;
}

.metric-big-highlight {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  margin-bottom: 0.3rem;
}

.m-num {
  font-size: 3.2rem;
  font-weight: 900;
  color: #34D399;
  line-height: 1;
}

.m-unit {
  font-size: 1.2rem;
  font-weight: 700;
  color: #6EE7B7;
}

.m-label {
  font-size: 0.85rem;
  color: #94A3B8;
  font-weight: 500;
  margin-bottom: 1.6rem;
}

.visual-interactive-preview {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.flow-step {
  padding: 0.9rem 1.1rem;
  border-radius: 10px;
  font-size: 0.84rem;
  line-height: 1.5;
}

.step-bad {
  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.25);
  color: #FCA5A5;
}

.step-bad .step-tag {
  color: #EF4444;
  font-weight: 800;
  font-size: 0.72rem;
  margin-bottom: 0.2rem;
}

.flow-arrow-down {
  text-align: center;
  font-size: 0.78rem;
  font-weight: 700;
  color: #64748B;
}

.step-good {
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.3);
  color: #A7F3D0;
}

.step-good .step-tag {
  color: #10B981;
  font-weight: 800;
  font-size: 0.72rem;
  margin-bottom: 0.2rem;
}

/* ================= 7. 行业解决方案 ================= */
.solutions-section {
  padding: 6rem 1.5rem;
  background: #060910;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.industry-pills-wrap {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 2.8rem;
}

.ind-pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.65rem 1.3rem;
  border-radius: 9999px;
  color: #94A3B8;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.ind-pill-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
}

.ind-pill-btn.active {
  background: linear-gradient(135deg, #195AFE, #3B82F6);
  border-color: #3B82F6;
  color: #ffffff;
  box-shadow: 0 4px 18px rgba(25, 90, 254, 0.4);
}

.industry-detail-card {
  max-width: 1240px;
  margin: 0 auto;
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  padding: 3.5rem;
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 3.5rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.ind-left-content {
  display: flex;
  flex-direction: column;
}

.ind-meta-tag {
  font-size: 0.8rem;
  font-weight: 800;
  color: #60A5FA;
  letter-spacing: 1px;
  margin-bottom: 0.75rem;
}

.ind-headline {
  font-size: 1.75rem;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.35;
  margin: 0 0 1.5rem 0;
}

.ind-scenario-box {
  background: rgba(255, 255, 255, 0.03);
  border-left: 3px solid #3B82F6;
  border-radius: 0 8px 8px 0;
  padding: 0.85rem 1.15rem;
  margin-bottom: 1.2rem;
}

.scenario-label {
  font-size: 0.72rem;
  font-weight: 700;
  color: #94A3B8;
  margin-bottom: 0.3rem;
}

.scenario-query {
  font-size: 0.95rem;
  font-weight: 700;
  color: #F8FAFC;
}

.ind-challenge-box {
  font-size: 0.88rem;
  line-height: 1.6;
  color: #94A3B8;
  margin-bottom: 1.5rem;
}

.c-title {
  color: #F87171;
  font-weight: 700;
}

.ind-tactics-list {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  margin-bottom: 2rem;
}

.tactic-title {
  font-size: 0.86rem;
  font-weight: 700;
  color: #CBD5E1;
  margin-bottom: 0.2rem;
}

.tactic-item {
  display: flex;
  align-items: flex-start;
  gap: 0.6rem;
  font-size: 0.88rem;
  color: #CBD5E1;
  line-height: 1.5;
}

.t-badge {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: rgba(25, 90, 254, 0.2);
  color: #60A5FA;
  font-size: 0.72rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 2px;
}

.btn-ind-action {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #195AFE, #3B82F6);
  color: #ffffff;
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-size: 0.92rem;
  font-weight: 700;
  width: fit-content;
  box-shadow: 0 4px 16px rgba(25, 90, 254, 0.4);
  transition: all 0.2s;
}

.btn-ind-action:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(25, 90, 254, 0.6);
}

.ind-right-metrics {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  justify-content: center;
}

.stat-card-gold {
  background: #090E1A;
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-radius: 16px;
  padding: 1.8rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

.stat-badge {
  font-size: 0.75rem;
  font-weight: 700;
  color: #FBBF24;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.6rem;
}

.stat-number-row .stat-num {
  font-size: 2.8rem;
  font-weight: 900;
  color: #ffffff;
  line-height: 1;
}

.stat-label {
  font-size: 0.88rem;
  color: #94A3B8;
  margin: 0.5rem 0 1.2rem 0;
}

.stat-bar-compare {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 0.85rem;
}

.comp-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #CBD5E1;
}

.comp-val.red { color: #EF4444; font-weight: 700; }
.comp-val.green { color: #10B981; font-weight: 700; }

.testimonial-quote-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 1.5rem;
  position: relative;
}

.quote-mark {
  font-size: 2.5rem;
  font-family: Georgia, serif;
  color: #3B82F6;
  line-height: 1;
  margin-bottom: -0.5rem;
}

.quote-text {
  font-size: 0.86rem;
  color: #CBD5E1;
  line-height: 1.6;
  margin: 0 0 1rem 0;
  font-style: italic;
}

.client-info-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.client-avatar {
  font-size: 1.6rem;
}

.client-name {
  font-size: 0.84rem;
  font-weight: 700;
  color: #ffffff;
}

.client-title {
  font-size: 0.74rem;
  color: #64748B;
}

.verified-seal {
  margin-left: auto;
  font-size: 0.72rem;
  font-weight: 700;
  color: #10B981;
  background: rgba(16, 185, 129, 0.1);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

/* ================= 8. 四层认知工程架构 ================= */
.arch-section {
  padding: 6rem 1.5rem;
  background: #080C14;
}

.arch-cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.arch-card {
  position: relative;
  border-radius: 18px;
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2rem 1.5rem;
  overflow: hidden;
  transition: all 0.3s ease;
}

.arch-card:hover {
  transform: translateY(-5px);
  border-color: rgba(59, 130, 246, 0.5);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(25, 90, 254, 0.2);
}

.arch-layer-pill {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 1px;
  color: #60A5FA;
  margin-bottom: 1.2rem;
}

.arch-icon-wrap {
  font-size: 2.2rem;
  margin-bottom: 1rem;
}

.arch-name {
  font-size: 1.25rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 0.3rem 0;
}

.arch-sub-en {
  font-size: 0.74rem;
  color: #64748B;
  font-weight: 600;
  margin-bottom: 1rem;
}

.arch-summary {
  font-size: 0.84rem;
  color: #94A3B8;
  line-height: 1.6;
  margin-bottom: 1.4rem;
}

.arch-checklist {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 1rem;
}

.check-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  color: #CBD5E1;
}

.check-item .dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #3B82F6;
}

/* ================= 9. 30 天闭环交付 ================= */
.roadmap-section {
  padding: 6rem 1.5rem;
  background: #060910;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.roadmap-timeline-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.roadmap-phase-card {
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 1.8rem;
  display: flex;
  flex-direction: column;
}

.phase-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.phase-badge {
  font-size: 0.75rem;
  font-weight: 800;
  color: #F59E0B;
}

.phase-days {
  font-size: 0.75rem;
  font-weight: 700;
  color: #64748B;
  background: rgba(255, 255, 255, 0.04);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.phase-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.4;
  margin: 0 0 0.75rem 0;
}

.phase-action {
  font-size: 0.82rem;
  color: #94A3B8;
  line-height: 1.6;
  margin-bottom: 1.2rem;
  flex: 1;
}

.phase-deliverable {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 0.75rem;
  margin-bottom: 1.2rem;
}

.d-label {
  font-size: 0.72rem;
  font-weight: 700;
  color: #60A5FA;
  margin-bottom: 0.2rem;
}

.d-val {
  font-size: 0.78rem;
  color: #CBD5E1;
  line-height: 1.4;
}

.phase-status {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.74rem;
  font-weight: 600;
  color: #10B981;
}

.phase-status .status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10B981;
}

/* ================= 10. 商业账本 ================= */
.roi-section {
  padding: 6rem 1.5rem;
  background: #080C14;
}

.roi-table-card {
  max-width: 1180px;
  margin: 0 auto 2.5rem auto;
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
}

.roi-table-header {
  display: grid;
  grid-template-columns: 1fr 1.3fr 1.3fr 1.5fr;
  background: #0A0F1D;
  padding: 1.2rem 1.5rem;
  font-size: 0.88rem;
  font-weight: 800;
  color: #CBD5E1;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.roi-table-header .highlight {
  color: #60A5FA;
}

.roi-table-row {
  display: grid;
  grid-template-columns: 1fr 1.3fr 1.3fr 1.5fr;
  padding: 1.15rem 1.5rem;
  font-size: 0.85rem;
  color: #94A3B8;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  align-items: center;
}

.roi-table-row:last-child {
  border-bottom: none;
}

.roi-table-row .font-bold {
  font-weight: 700;
  color: #ffffff;
}

.highlight-cell {
  color: #E2E8F0;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.45rem;
  background: rgba(25, 90, 254, 0.08);
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border-left: 2px solid #3B82F6;
}

.highlight-cell .check-icon {
  color: #10B981;
  font-weight: 900;
}

.roi-summary-banner {
  max-width: 1180px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 1rem;
  background: rgba(25, 90, 254, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.2rem 1.5rem;
  font-size: 0.9rem;
  color: #CBD5E1;
  line-height: 1.6;
}

.banner-icon {
  font-size: 1.6rem;
}

.banner-text strong {
  color: #60A5FA;
}

/* ================= 11. FAQ Accordion ================= */
.faq-section {
  padding: 5rem 1.5rem 6rem;
  background: #060910;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.faq-accordion-list {
  max-width: 860px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.faq-item {
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.faq-item:hover {
  border-color: rgba(255, 255, 255, 0.16);
}

.faq-item.open {
  border-color: rgba(59, 130, 246, 0.4);
}

.faq-question {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.q-icon {
  font-size: 0.88rem;
  font-weight: 800;
  color: #3B82F6;
}

.q-text {
  flex: 1;
  font-size: 1.02rem;
  font-weight: 700;
  color: #ffffff;
}

.q-toggle {
  font-size: 1.2rem;
  font-weight: 700;
  color: #64748B;
}

.faq-answer {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.faq-answer p {
  font-size: 0.9rem;
  color: #94A3B8;
  line-height: 1.7;
  margin: 0;
}

/* ================= 12. 转化底栏 ================= */
.bottom-cta-banner {
  position: relative;
  padding: 6.5rem 1.5rem;
  background: #080C14;
  overflow: hidden;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.cta-cosmic-glow {
  position: absolute;
  inset: -100px;
  background: radial-gradient(circle at 50% 50%, rgba(25, 90, 254, 0.25) 0%, rgba(168, 85, 247, 0.2) 35%, rgba(255, 109, 3, 0.12) 65%, transparent 80%);
  pointer-events: none;
  filter: blur(80px);
}

.cta-inner {
  max-width: 860px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.cta-badge {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: #F59E0B;
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid rgba(245, 158, 11, 0.3);
  padding: 0.3rem 0.9rem;
  border-radius: 9999px;
  margin-bottom: 1.5rem;
}

.cta-headline {
  font-size: 2.8rem;
  font-weight: 900;
  line-height: 1.25;
  letter-spacing: -0.6px;
  color: #ffffff;
  margin: 0 0 1.2rem 0;
}

.cta-sub {
  font-size: 1.05rem;
  color: #94A3B8;
  margin: 0 0 2.5rem 0;
}

.cta-action-box {
  max-width: 620px;
  margin: 0 auto 1.8rem auto;
}

.cta-input-wrap {
  display: flex;
  align-items: center;
  background: rgba(15, 22, 38, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 9999px;
  padding: 0.4rem 0.5rem 0.4rem 1.4rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
}

.cta-input-wrap input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: #ffffff;
  font-size: 0.98rem;
}

.btn-cta-submit {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: linear-gradient(135deg, #195AFE 0%, #3B82F6 50%, #8B5CF6 100%);
  border: none;
  border-radius: 9999px;
  padding: 0.8rem 1.6rem;
  color: #ffffff;
  font-size: 0.92rem;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  box-shadow: 0 0 20px rgba(25, 90, 254, 0.5);
  transition: all 0.2s;
}

.btn-cta-submit:hover {
  transform: scale(1.03);
  box-shadow: 0 0 30px rgba(25, 90, 254, 0.7);
}

.cta-footer-tags {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  font-size: 0.8rem;
  color: #64748B;
}

.cta-footer-tags .sep {
  color: #334155;
}

/* ================= 13. 暗黑品牌页脚 ================= */
.landing-footer {
  background: #04070D;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding: 4.5rem 1.5rem 2rem;
}

.footer-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 3.5rem;
  margin-bottom: 3.5rem;
}

.footer-brand-col {
  display: flex;
  flex-direction: column;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 1.2rem;
}

.f-logo-img {
  height: 34px;
  width: auto;
  object-fit: contain;
}

.footer-slogan {
  font-size: 0.85rem;
  color: #64748B;
  line-height: 1.6;
  margin: 0 0 1.5rem 0;
  max-width: 360px;
}

.footer-live-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.76rem;
  color: #6EE7B7;
}

.status-live-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 6px #10B981;
}

.col-title {
  font-size: 0.88rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 1.2rem 0;
  letter-spacing: 0.5px;
}

.footer-links-col {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}

.f-link {
  color: #64748B;
  text-decoration: none;
  font-size: 0.84rem;
  transition: color 0.2s;
}

.f-link:hover {
  color: #60A5FA;
}

.f-link.disabled {
  opacity: 0.5;
  cursor: default;
}

.footer-bottom-bar {
  max-width: 1280px;
  margin: 0 auto;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  font-size: 0.76rem;
  color: #475569;
}

/* ================= 响应式媒体查询 ================= */
@media (max-width: 1100px) {
  .hero-headline { font-size: 2.8rem; }
  .mockup-window-body { grid-template-columns: 1fr; }
  .slider-tabs-row { grid-template-columns: repeat(2, 1fr); }
  .slider-card-body { grid-template-columns: 1fr; gap: 2rem; padding: 2rem; }
  .industry-detail-card { grid-template-columns: 1fr; padding: 2rem; gap: 2rem; }
  .arch-cards-grid { grid-template-columns: repeat(2, 1fr); }
  .roadmap-timeline-grid { grid-template-columns: repeat(2, 1fr); }
  .footer-inner { grid-template-columns: 1fr 1fr; gap: 2rem; }
  .marquee-track { gap: 1.4rem; }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .hero-headline { font-size: 2.2rem; }
  .hero-subtext { font-size: 0.95rem; }
  .slider-tabs-row { grid-template-columns: 1fr; }
  .arch-cards-grid { grid-template-columns: 1fr; }
  .roadmap-timeline-grid { grid-template-columns: 1fr; }
  .roi-table-header, .roi-table-row { grid-template-columns: 1fr; gap: 0.5rem; }
  .footer-inner { grid-template-columns: 1fr; gap: 2rem; }
  .cta-headline { font-size: 1.85rem; }
  .cta-input-wrap { flex-direction: column; border-radius: 16px; padding: 0.8rem; gap: 0.8rem; }
  .btn-cta-submit { width: 100%; justify-content: center; }
  .search-input-box { flex-direction: column; border-radius: 20px; padding: 0.8rem; gap: 0.8rem; }
  .search-divider { display: none; }
  .btn-search-action { width: 100%; }
  .marquee-card { padding: 0.8rem 1.2rem; }
  .card-icon-halo { font-size: 1.6rem; width: 40px; height: 40px; }
  .card-main-name { font-size: 1.02rem; }
}
</style>
