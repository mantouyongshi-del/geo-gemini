<template>
  <div class="landing-container">
    <!-- 1. 绝对固定顶部导航栏 (Fixed Header) -->
    <header class="landing-header">
      <div class="header-inner">
        <!-- 品牌标识：无束缚、通透大气的自然 Logo 呈现 -->
        <router-link to="/" class="brand-link" title="蜉蝣小宝 · AI 营销智能大脑">
          <div class="logo-aura-wrap">
            <div class="logo-soft-glow"></div>
            <img src="/logo-white.png" alt="蜉蝣小宝" class="logo-unconstrained" />
          </div>
          <span class="brand-badge-tag">GEO 2.0</span>
        </router-link>

        <nav class="nav-links">
          <a href="#hero-search" class="nav-item">搜索透视</a>
          <a href="#market-shift" class="nav-item">流量趋势</a>
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
            <span class="btn-text">免费启动体检</span>
            <svg class="btn-svg-arrow" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </router-link>
        </div>
      </div>
    </header>

    <!-- 2. 首屏暗黑深空区 (Hero Section - 跑马灯首屏即可见) -->
    <section class="hero-section">
      <!-- 动态深空背景光晕 -->
      <div class="ambient-glow orb-blue"></div>
      <div class="ambient-glow orb-purple"></div>
      <div class="grid-overlay"></div>

      <div class="section-inner hero-inner">
        <!-- 顶部公告胶囊 -->
        <div class="hero-pill-badge">
          <span class="badge-dot-live"></span>
          <span class="badge-text">2026 生成式 AI 搜索优化 · GEO 认知工程中枢</span>
          <router-link to="/console" class="badge-link">
            <span>白皮书解读</span>
            <svg class="pill-arrow" viewBox="0 0 16 16" fill="currentColor">
              <path fill-rule="evenodd" d="M6.22 3.22a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06L9.94 8 6.22 4.28a.75.75 0 010-1.06z" clip-rule="evenodd" />
            </svg>
          </router-link>
        </div>

        <!-- 极简大气主标题 -->
        <h1 class="hero-headline">
          当 5 亿客户向 AI 提问<br />
          让您的品牌成为 <span class="text-gradient">第一推荐</span>
        </h1>

        <!-- 精炼副标题 -->
        <p class="hero-subtext">
          穿透豆包、DeepSeek、通义千问等主流大模型推荐决策层<br />
          测算潜在客源流失 · 构建专属于企业的权威知识资产护城河
        </p>

        <!-- Similarweb 风格交互式搜索框 -->
        <div id="hero-search" class="hero-search-wrapper">
          <div class="search-input-box">
            <div class="search-mode-select">
              <svg class="mode-svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4zm3 1h6v4H7V5zm8 8v2h1v-2h-1zm-2-2H7v4h6v-4zm2 0h1V9h-1v2zm1-4V5h-1v2h1zM5 5v2H4V5h1zm0 4h1v2H4V9zm1 4H4v2h1v-2z" clip-rule="evenodd" />
              </svg>
              <span class="mode-label">品牌全网诊断</span>
              <svg class="mode-caret-svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
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
                <svg class="action-svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" clip-rule="evenodd" />
                </svg>
                <span class="action-label">立即透视</span>
              </span>
            </button>
          </div>

          <!-- 精炼标杆 Chips (无 emoji，纯净轻奢) -->
          <div class="quick-chips-row">
            <span class="chips-label">标杆行业检索：</span>
            <button
              v-for="(chip, idx) in quickChips"
              :key="idx"
              class="chip-btn"
              @click="applyQuickChip(chip)"
            >
              <span class="chip-dot"></span>
              <span class="chip-text">{{ chip.label }}</span>
            </button>
          </div>
        </div>

        <!-- 首屏内置跑马灯：大模型与权威信源 (首屏即可见，专业无框 SVG 标，无任何低端 emoji) -->
        <div class="hero-trust-marquee-container">
          <div class="trust-marquee-header">
            <span class="trust-line"></span>
            <span class="trust-title-text">直连中国主流基座大模型 · 覆盖高权重权威信源生态</span>
            <span class="trust-line"></span>
          </div>

          <div class="trust-marquee-track-wrap">
            <div class="trust-marquee-track">
              <!-- 第一组品牌标 -->
              <div
                v-for="(brand, bIdx) in trustBrands"
                :key="'t1-' + bIdx"
                class="trust-brand-item"
              >
                <div class="brand-svg-symbol" v-html="brand.svg"></div>
                <div class="brand-meta">
                  <span class="brand-title">{{ brand.name }}</span>
                  <span class="brand-role">{{ brand.role }}</span>
                </div>
                <div class="brand-live-pulse" title="24/7 直连运行中"></div>
              </div>
              <!-- 第二组品牌标 (无缝平滑衔接) -->
              <div
                v-for="(brand, bIdx) in trustBrands"
                :key="'t2-' + bIdx"
                class="trust-brand-item"
              >
                <div class="brand-svg-symbol" v-html="brand.svg"></div>
                <div class="brand-meta">
                  <span class="brand-title">{{ brand.name }}</span>
                  <span class="brand-role">{{ brand.role }}</span>
                </div>
                <div class="brand-live-pulse" title="24/7 直连运行中"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. 白色/浅色清爽区域：流量转移趋势与简约数据图表 (切换为白底，消除疲劳) -->
    <section id="market-shift" class="light-section-contrast">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="light-badge">行业格局演进 · PARADIGM SHIFT</span>
          <h2 class="light-title">
            从“网页点击”到“AI 推荐答案”：<br />
            不可逆转的 <span class="text-gradient-blue">流量转移与认知洗牌</span>
          </h2>
          <p class="light-sub">
            传统搜索链接点击率下滑 34%，而大模型对话式采购决策咨询暴涨 420%。客户向 AI 要的是确凿的选型建议，而不是一页翻不完的广告链接。
          </p>
        </div>

        <!-- 简约数据图表 1：AI 对话推荐意图爆发 VS 传统搜索有效点击 (SVG 极简趋势图) -->
        <div class="data-chart-card">
          <div class="chart-card-header">
            <div class="chart-header-left">
              <h3 class="chart-title">2023 - 2026 全网采购决策与流量演化图谱</h3>
              <span class="chart-sub-note">基于 500+ 万次 B2B 制造、大宅定制、现代消费真实搜索与推荐样本测算</span>
            </div>
            <div class="chart-legend-group">
              <div class="legend-item">
                <span class="legend-line line-cyan"></span>
                <span>AI 大模型生成式推荐召回率 (+420%)</span>
              </div>
              <div class="legend-item">
                <span class="legend-line line-gray"></span>
                <span>传统搜索有效商机点击率 (-34%)</span>
              </div>
            </div>
          </div>

          <!-- SVG 简约折线/面积图表 -->
          <div class="svg-chart-container">
            <svg class="trend-chart-svg" viewBox="0 0 1000 320" preserveAspectRatio="none">
              <defs>
                <linearGradient id="cyanArea" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#0284C7" stop-opacity="0.25" />
                  <stop offset="100%" stop-color="#0284C7" stop-opacity="0.0" />
                </linearGradient>
                <linearGradient id="cyanLine" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#38BDF8" />
                  <stop offset="50%" stop-color="#2563EB" />
                  <stop offset="100%" stop-color="#7C3AED" />
                </linearGradient>
              </defs>

              <!-- 刻度参考背景线 -->
              <line x1="60" y1="50" x2="960" y2="50" stroke="#E2E8F0" stroke-dasharray="4 4" />
              <line x1="60" y1="120" x2="960" y2="120" stroke="#E2E8F0" stroke-dasharray="4 4" />
              <line x1="60" y1="190" x2="960" y2="190" stroke="#E2E8F0" stroke-dasharray="4 4" />
              <line x1="60" y1="260" x2="960" y2="260" stroke="#CBD5E1" stroke-width="1.5" />

              <!-- 面积渐变 -->
              <path d="M 60,240 C 260,230 460,190 660,105 C 800,45 960,30 960,30 L 960,260 L 60,260 Z" fill="url(#cyanArea)" />

              <!-- 传统搜索下跌线 (灰折线) -->
              <path d="M 60,70 C 260,85 460,120 660,175 C 800,215 960,245 960,245" fill="none" stroke="#94A3B8" stroke-width="2.5" stroke-dasharray="6 4" />

              <!-- AI 搜索暴涨曲线 (高饱和渐变实线) -->
              <path d="M 60,240 C 260,230 460,190 660,105 C 800,45 960,30 960,30" fill="none" stroke="url(#cyanLine)" stroke-width="4" />

              <!-- 数据标点 -->
              <circle cx="60" cy="240" r="5" fill="#0284C7" stroke="#ffffff" stroke-width="2.5" />
              <circle cx="660" cy="105" r="5" fill="#2563EB" stroke="#ffffff" stroke-width="2.5" />
              <circle cx="960" cy="30" r="7" fill="#7C3AED" stroke="#ffffff" stroke-width="3" />
            </svg>

            <!-- X 轴刻度文本 -->
            <div class="chart-x-axis">
              <span>2023 Q1 (传统搜索全盛)</span>
              <span>2024 Q2 (大模型多点开花)</span>
              <span>2025 Q3 (AI 对话成为主要决策入口)</span>
              <span class="highlight-axis">2026 当前 (GEO 全域知识确权节点)</span>
            </div>
          </div>
        </div>

        <!-- 范式转移 4 阶段对比滑块 (浅色高雅质感) -->
        <div class="light-shift-slider">
          <div class="light-slider-tabs">
            <button
              v-for="(slide, sIdx) in shiftSlides"
              :key="sIdx"
              class="light-tab-btn"
              :class="{ active: currentSlideIndex === sIdx }"
              @click="switchSlide(sIdx)"
            >
              <div class="light-tab-progress">
                <div
                  class="light-progress-bar"
                  :style="{ width: currentSlideIndex === sIdx ? `${slideProgress}%` : (currentSlideIndex > sIdx ? '100%' : '0%') }"
                ></div>
              </div>
              <div class="light-tab-meta">
                <span class="tab-idx">0{{ sIdx + 1 }}</span>
                <span class="tab-txt">{{ slide.shortTitle }}</span>
              </div>
            </button>
          </div>

          <div class="light-slider-content">
            <div class="slide-left">
              <span class="slide-tag-pill">{{ currentSlide.tag }}</span>
              <h3 class="slide-title-clean">{{ currentSlide.headline }}</h3>
              <p class="slide-desc-clean">{{ currentSlide.description }}</p>

              <div class="slide-bullets">
                <div class="bullet-row" v-for="(p, pIdx) in currentSlide.points" :key="pIdx">
                  <svg class="bullet-check-svg" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                  <span>{{ p }}</span>
                </div>
              </div>
            </div>

            <div class="slide-right">
              <div class="slide-stat-panel">
                <div class="stat-highlight-box">
                  <div class="stat-big-num">{{ currentSlide.metricNum }}</div>
                  <div class="stat-unit-text">{{ currentSlide.metricUnit }}</div>
                  <div class="stat-desc-label">{{ currentSlide.metricLabel }}</div>
                </div>

                <div class="contrast-flow-box">
                  <div class="contrast-row bad">
                    <span class="status-tag">优化前</span>
                    <span class="status-desc">{{ currentSlide.oldState }}</span>
                  </div>
                  <div class="contrast-row good">
                    <span class="status-tag">GEO优化后</span>
                    <span class="status-desc">{{ currentSlide.newState }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. 白色/浅色清爽区域：行业解决方案与实测数据 (Light Canvas 继续保持舒适阅读) -->
    <section id="solutions" class="light-section-solutions">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="light-badge">行业落地战法 · INDUSTRY SOLUTIONS</span>
          <h2 class="light-title">
            为实体产业定制的 <span class="text-gradient-blue">GEO 精准拦截方案</span>
          </h2>
          <p class="light-sub">
            针对工业制造、高端门窗、连锁招商、专科医疗、高端法律等重决策周期行业，穿透大模型推荐层。
          </p>
        </div>

        <!-- 行业胶囊切换器 (无 emoji，纯净高档) -->
        <div class="industry-pills-row">
          <button
            v-for="(ind, indIdx) in industries"
            :key="ind.id"
            class="ind-clean-pill"
            :class="{ active: activeIndustryIndex === indIdx }"
            @click="activeIndustryIndex = indIdx"
          >
            <div class="pill-svg-icon" v-html="ind.svg"></div>
            <span class="pill-text">{{ ind.name }}</span>
          </button>
        </div>

        <!-- 行业展示卡片 (浅色轻奢微阴影) -->
        <div class="industry-light-card">
          <div class="ind-card-left">
            <div class="ind-badge-category">{{ currentIndustry.category }}</div>
            <h3 class="ind-card-headline">{{ currentIndustry.headline }}</h3>

            <div class="ind-query-container">
              <div class="query-top-label">
                <svg class="query-icon-svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                </svg>
                <span>典型采购决策提问场景</span>
              </div>
              <div class="query-body-text">{{ currentIndustry.scenarioQuery }}</div>
            </div>

            <div class="ind-tactics-section">
              <h4 class="tactics-head">30 天核心落地工程动作：</h4>
              <div class="tactic-line" v-for="(t, tIdx) in currentIndustry.tactics" :key="tIdx">
                <span class="t-step-idx">{{ tIdx + 1 }}</span>
                <span class="t-step-text">{{ t }}</span>
              </div>
            </div>

            <router-link
              :to="{ path: '/console', query: { industry: currentIndustry.name, brand: currentIndustry.defaultBrand } }"
              class="btn-ind-clean"
            >
              <span>体验该行业体检方案</span>
              <svg class="arrow-svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </router-link>
          </div>

          <!-- 右侧：简约数据柱状对比与标杆企业证言 -->
          <div class="ind-card-right">
            <div class="stat-clean-card">
              <div class="stat-top-row">
                <span class="stat-title-label">月度挽回流失订单资产</span>
                <span class="stat-trend-tag">+340% 意向回流</span>
              </div>
              <div class="stat-number-display">{{ currentIndustry.statValue }}</div>
              
              <!-- 简约进度柱图 -->
              <div class="bar-compare-box">
                <div class="bar-row">
                  <span class="bar-name">优化前推荐提及率</span>
                  <span class="bar-val text-red">{{ currentIndustry.preRate }}</span>
                </div>
                <div class="bar-track-bg">
                  <div class="bar-fill red" :style="{ width: currentIndustry.preWidth }"></div>
                </div>

                <div class="bar-row mt-3">
                  <span class="bar-name">GEO 优化后首推率</span>
                  <span class="bar-val text-green">{{ currentIndustry.postRate }}</span>
                </div>
                <div class="bar-track-bg">
                  <div class="bar-fill green" :style="{ width: currentIndustry.postWidth }"></div>
                </div>
              </div>
            </div>

            <div class="testimonial-light-card">
              <div class="quote-text-clean">“{{ currentIndustry.clientQuote }}”</div>
              <div class="quote-author-row">
                <div class="author-avatar-badge">{{ currentIndustry.authorInitial }}</div>
                <div class="author-meta">
                  <div class="author-name">{{ currentIndustry.clientName }}</div>
                  <div class="author-title">{{ currentIndustry.clientTitle }}</div>
                </div>
                <div class="author-verified">
                  <svg class="v-check-svg" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                  <span>已核验标杆</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. 深色科技底座：四层认知工程架构 (Dark Technical Architecture) -->
    <section id="architecture" class="dark-tech-section">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="hero-pill-badge">底层技术 · ENGINE ARCHITECTURE</span>
          <h2 class="hero-headline font-reduced">
            穿透大模型决策的 <span class="text-gradient">四层认知工程体系</span>
          </h2>
          <p class="hero-subtext">
            专为 Transformer 深度推理与 RAG 向量检索召回设计的确定性工程。
          </p>
        </div>

        <div class="arch-clean-grid">
          <div
            v-for="(arch, aIdx) in archLayers"
            :key="aIdx"
            class="arch-clean-card"
          >
            <div class="arch-header-top">
              <div class="arch-svg-wrap" v-html="arch.svg"></div>
              <span class="arch-layer-code">LAYER 0{{ aIdx + 1 }}</span>
            </div>

            <h3 class="arch-card-title">{{ arch.name }}</h3>
            <div class="arch-en-code">{{ arch.enName }}</div>
            <p class="arch-card-summary">{{ arch.desc }}</p>

            <div class="arch-item-list">
              <div class="arch-item-row" v-for="(item, cIdx) in arch.items" :key="cIdx">
                <span class="item-square"></span>
                <span>{{ item }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. 白色清爽区域：30 天交付与商业账本 ROI (Light ROI Ledger) -->
    <section id="roadmap" class="light-section-roadmap">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="light-badge">交付保障 · 30-DAY DELIVERY</span>
          <h2 class="light-title">
            从完全隐形到全网首推：<br />
            <span class="text-gradient-blue">30 天闭环战役交付蓝图</span>
          </h2>
          <p class="light-sub">
            每一步皆有确权文档与权威索引链接核验，让投入落地为不可逆的数字资产。
          </p>
        </div>

        <!-- 30 天交付阶段卡片 -->
        <div class="roadmap-light-grid">
          <div
            v-for="(step, sIdx) in roadmapSteps"
            :key="sIdx"
            class="roadmap-step-card"
          >
            <div class="step-card-header">
              <span class="step-num-pill">PHASE {{ step.phase }}</span>
              <span class="step-days-tag">{{ step.days }}</span>
            </div>
            <h3 class="step-card-title">{{ step.title }}</h3>
            <p class="step-card-action">{{ step.action }}</p>
            <div class="step-deliverable-box">
              <div class="del-label">阶段交付物：</div>
              <div class="del-text">{{ step.deliverable }}</div>
            </div>
          </div>
        </div>

        <!-- 商业账本：极简对比表 -->
        <div id="roi" class="roi-ledger-wrap">
          <div class="section-header-center mt-5">
            <span class="light-badge">商业复利 · ECONOMIC VALUE</span>
            <h2 class="light-title">
              算清企业的商业账本：<br />
              为什么说 <span class="text-gradient-blue">GEO 是极高 ROI 的战略资产</span>？
            </h2>
          </div>

          <div class="roi-clean-table-card">
            <div class="roi-row table-head">
              <div class="col-1">对比维度</div>
              <div class="col-2">传统竞价广告 (SEM)</div>
              <div class="col-3">传统网页优化 (SEO)</div>
              <div class="col-4 head-highlight">蜉蝣小宝 GEO 认知工程</div>
            </div>

            <div class="roi-row" v-for="(row, rIdx) in roiRows" :key="rIdx">
              <div class="col-1 font-bold-dark">{{ row.dimension }}</div>
              <div class="col-2 text-muted">{{ row.sem }}</div>
              <div class="col-3 text-muted">{{ row.seo }}</div>
              <div class="col-4 cell-highlight">
                <svg class="check-svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>{{ row.geo }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. 常见问题解答 (FAQ) -->
    <section id="faq" class="light-section-faq">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="light-badge">疑问解答 · FAQ</span>
          <h2 class="light-title">企业管理者最关心的核心问题</h2>
        </div>

        <div class="faq-clean-list">
          <div
            v-for="(faq, fIdx) in faqs"
            :key="fIdx"
            class="faq-clean-item"
            :class="{ open: openFaqIndex === fIdx }"
            @click="toggleFaq(fIdx)"
          >
            <div class="faq-q-row">
              <span class="faq-q-symbol">Q</span>
              <span class="faq-q-title">{{ faq.question }}</span>
              <span class="faq-toggle-icon">{{ openFaqIndex === fIdx ? '−' : '+' }}</span>
            </div>
            <div v-show="openFaqIndex === fIdx" class="faq-a-body">
              <p>{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. 宇宙光晕高转化底栏 (Dark Closing CTA) -->
    <section class="bottom-cta-banner">
      <div class="cta-cosmic-glow"></div>
      <div class="cta-inner">
        <span class="badge-tag-orange">即刻行动 · 终结客源失血</span>
        <h2 class="cta-headline">
          准备好在 AI 搜索时代，彻底终结客源被同行截流的局面了吗？
        </h2>
        <p class="cta-sub">
          无需部署任何插件 · 现场直连 5 大主流基座大模型 · 10秒快速出具专属体检书
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
              <svg class="btn-arrow" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. 暗黑品牌页脚 (Dark Footer) -->
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
            <span>五大基座大模型接口：24/7 稳定直连在线</span>
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
          <a href="#solutions" class="f-link">工业装备制造</a>
          <a href="#solutions" class="f-link">高端大宅系统门窗</a>
          <a href="#solutions" class="f-link">连锁餐饮加盟</a>
          <a href="#solutions" class="f-link">专科医疗齿科</a>
          <a href="#solutions" class="f-link">商务法务与律所</a>
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
  '输入您的企业或品牌名（如：无锡恒瑞智能装备 / 激光切管机）',
  '输入大宅门窗品牌（如：佛山佳豪系统门窗 / 高端断桥铝）',
  '输入全国连锁餐饮品牌（如：老乡鸡 / 快餐招商加盟）',
  '输入专科医疗或门诊（如：数字化种植牙医院 / 齿科专科）',
  '输入企业常年法律顾问（如：商事合同争议解决律所）'
];
const currentPlaceholderIndex = ref(0);
const currentPlaceholder = computed(() => placeholders[currentPlaceholderIndex.value]);

let placeholderTimer = null;

onMounted(() => {
  placeholderTimer = setInterval(() => {
    currentPlaceholderIndex.value = (currentPlaceholderIndex.value + 1) % placeholders.length;
  }, 3500);

  startSlideLoop();
});

onUnmounted(() => {
  if (placeholderTimer) clearInterval(placeholderTimer);
  if (slideTimer) clearInterval(slideTimer);
  if (progressTimer) clearInterval(progressTimer);
});

// 标杆案例快速体验 Chips (纯净矢量质感，无 emoji)
const quickChips = [
  { label: '工业切管机制造', brand: '恒瑞智能装备', company: '无锡恒瑞智能装备科技有限公司', industry: '工业数控激光切管机制造', city: '无锡' },
  { label: '高端系统门窗', brand: '佳豪系统门窗', company: '佛山尚品佳豪智能家居系统有限公司', industry: '高端断桥铝系统门窗与阳光房', city: '佛山' },
  { label: '餐饮招商加盟', brand: '老乡鸡', company: '安徽老乡鸡餐饮股份有限公司', industry: '中式快餐连锁加盟与招商', city: '全国' },
  { label: '数字化齿科专科', brand: '恒伦口腔', company: '数字化种植牙与隐形正畸专科门诊', industry: '专科医疗与数字化齿科', city: '全国' },
  { label: '商事常年法务', brand: '金杜律所', company: '商事争议与常年法律顾问律所', industry: '企业商事争议解决与常年合规', city: '全国' }
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

// 首屏跑马灯品牌列表 (采用专业 SVG 矢量图形，绝无 emoji 符号与低端框框)
const trustBrands = [
  {
    name: '字节跳动 · 豆包',
    role: '火山引擎方舟直连',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>'
  },
  {
    name: '深度求索 · DeepSeek',
    role: 'R1 深度推理全量核验',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M12 3a9 9 0 0 1 9 9"></path><circle cx="12" cy="12" r="3"></circle></svg>'
  },
  {
    name: '阿里巴巴 · 通义千问',
    role: '百炼原生知识库召回',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>'
  },
  {
    name: '腾讯科技 · 元宝',
    role: '混元大模型商业决策',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>'
  },
  {
    name: '百度智能云 · 文心',
    role: '搜索语义穿透',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'
  },
  {
    name: '百度百科官方确权',
    role: '权威知识本体锚点',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#CBD5E1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>'
  },
  {
    name: '企查查企业资质',
    role: '官方专利与高新核验',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
  },
  {
    name: '搜狐科技产业研报',
    role: '权威第一梯队采信',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#FBBF24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>'
  },
  {
    name: '新浪财经门户',
    role: '国家级产业高权重',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#F87171" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>'
  },
  {
    name: '知乎专业问答矩阵',
    role: '深度决策信任背书',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'
  }
];

// 范式转移滑块
const currentSlideIndex = ref(0);
const slideProgress = ref(0);
let slideTimer = null;
let progressTimer = null;

const shiftSlides = [
  {
    shortTitle: '可见度隐形',
    tag: '可见度革命 · VISIBILITY',
    headline: '您的品牌在 AI 时代彻底隐形？在对话流中抢占第一提及率',
    description: '传统搜索用户翻阅 10 条链接，企业靠长尾词捡漏；AI 时代每次回答只推荐 1~3 个实体。若未注入知识图谱 Schema 结构化实体，您的品牌在 5 亿客户面前等同于“不存在”。',
    points: [
      '百科权威词条与知识图谱 Schema 唯一标识确权',
      '攻破主流大模型底层 RAG 知识检索库，确立企业法定知识锚点',
      '让每一次“哪家好”、“知名品牌”的提问，都稳居首选第一梯队'
    ],
    metricNum: '92%',
    metricUnit: '首推胜率',
    metricLabel: '行业权威首推提及率跃升',
    oldState: '仅有官网，公域知识库空白，提及率为 0%',
    newState: 'Schema本体确权，5大模型稳居首选推荐位 (92%)'
  },
  {
    shortTitle: '客源被截流',
    tag: '意图防御 · TRAFFIC & DEFENSE',
    headline: '搜索习惯转向 AI，您的潜在客源正被同行无声截流',
    description: '当企业采购决策者向大模型询问“选哪家靠谱”、“避坑指南”时，竞争对手早已通过权威研报公域投喂完成霸屏拦截，您的订单在决策第一步就被掠夺殆尽。',
    points: [
      '深度扫描 50+ 个行业高频采购拦截意图词库',
      '反制竞品恶意单向对比，扭转大模型偏见评价',
      '在买家产生意向的黄金 3 秒内，锁定专属品牌信任链路'
    ],
    metricNum: '+340%',
    metricUnit: '挽回订单',
    metricLabel: '高意向采购线索回流增长',
    oldState: '采购提问被同行竞品全量拦截，客户严重流失',
    newState: '构建高权重测评公域矩阵，将采购需求定向截流至贵司'
  },
  {
    shortTitle: '获客成本失控',
    tag: '效率飞跃 · EFFICIENCY & ROI',
    headline: '传统竞价单次点击翻倍，构建 0 持续边际成本的 GEO 护城河',
    description: '百度竞价单次点击费用暴涨，且停充即停流；GEO 沉淀的是公域中不可篡改的永久知识资产，一次建设，长效享受全网基座大模型的免费精准推荐。',
    points: [
      '摆脱无底洞式的关键词竞价点击扣费陷阱',
      '权威媒体研报与百科资产永久收录，不随时间被轻易稀释',
      '边际获客成本趋近于 0，构筑同行业极具抗周期的增长壁垒'
    ],
    metricNum: '￥0',
    metricUnit: '单次扣费',
    metricLabel: '永久知识资产复利沉淀',
    oldState: '每次点击扣费 30~80 元，停充流量瞬间归零',
    newState: '知识沉淀为大模型内生记忆，无需持续支付提问费'
  },
  {
    shortTitle: '三重飞轮',
    tag: '全域增长 · THE TRIPLE EFFECT',
    headline: '流量 · 声誉 · 成交：构建企业生成式推荐的全链路增长飞轮',
    description: 'GEO 不仅是简单的名词排位，更是企业在 AI 心智中的全方位声誉重塑。从知识本体的确立，到第三方权威公信力的背书，再到商业订单的水到渠成。',
    points: [
      '双端（移动端同城生活圈 + PC端权威知识库）双切面协同覆盖',
      '24/7 自动化雷达巡检，实时预警大模型知识漂移与竞品反扑',
      '30 天确定性闭环交付，以权威索引链接与体检报告作为铁证验收'
    ],
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

// 行业解决方案 (纯净专业 SVG 标识，无 emoji)
const activeIndustryIndex = ref(0);

const industries = [
  {
    id: 'b2b',
    name: '工业装备制造',
    category: '工业装备制造 · B2B高客单决策',
    defaultBrand: '恒瑞智能装备',
    headline: '打破工业装备行业龙头垄断，在 AI 采购选型横评中稳居前二推荐位',
    scenarioQuery: '“无锡光纤激光切管机生产厂家推荐哪家质量好性价比高？”',
    tactics: [
      '建立国家工信部专精特新认证与国家专利储备 Schema 实体标签',
      '在搜狐科技与机械行业垂直媒体定向发布 18 篇深度技术测评研报',
      '抢占“重管切割哪家好”、“激光切管机选型避坑”等 50+ 个采购拦截词'
    ],
    statValue: '￥240,000 / 月',
    preRate: '0%',
    preWidth: '5%',
    postRate: '92%',
    postWidth: '92%',
    clientQuote: '以前客户采购几十万的切管机在豆包搜横评，推荐的都是同行龙头。做完GEO后，豆包直接把我们列为华东重管首选推荐，当月就有两台意向客户主动加微信！',
    authorInitial: '张',
    clientName: '张总',
    clientTitle: '无锡恒瑞智能装备 · 市场副总裁',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 20h20M5 20V8l5 4V4l5 4V4l5 4v12"></path></svg>'
  },
  {
    id: 'window',
    name: '高端系统门窗',
    category: '大宅定制与高端建材',
    defaultBrand: '佳豪系统门窗',
    headline: '突破传统建材卖场客流瓶颈，在手机端同城生活圈截获大宅业主直接咨询',
    scenarioQuery: '“本地高端断桥铝系统门窗十大品牌实力排名与避坑指南”',
    tactics: [
      '双端切面协同：打通手机端生活圈同城实录与真实业主装修评价',
      'PC端沉淀门窗五金水密性、隔音国标参数与行业横评长文',
      '在豆包“本地线下机构/服务商对比”中稳居前二，打消小作坊质量顾虑'
    ],
    statValue: '￥180,000 / 月',
    preRate: '12%',
    preWidth: '12%',
    postRate: '89%',
    postWidth: '89%',
    clientQuote: '商场进店客流越来越少，年轻业主全部用大模型搜断桥铝避坑。把水密国标和本地案例喂给大模型后，现在客户进店就说“AI推荐你们做大宅封窗靠谱”！',
    authorInitial: '李',
    clientName: '李总',
    clientTitle: '佛山佳豪系统门窗 · 创始人',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="3" y1="12" x2="21" y2="12"></line><line x1="12" y1="3" x2="12" y2="21"></line></svg>'
  },
  {
    id: 'catering',
    name: '连锁餐饮加盟',
    category: '现代连锁消费与招商',
    defaultBrand: '老乡鸡',
    headline: '抢占全国快餐第一提及率，招商加盟与堂食口碑双爆发',
    scenarioQuery: '“全国中式快餐连锁加盟哪个品牌扶持政策好存活率高？”',
    tactics: [
      '在知乎专业问答与财经门户沉淀供应链支持、门店存活率客观研报',
      '打通大众点评店铺矩阵与高权重美食媒体权威背书实体',
      '在千问与元宝的商业决策对比矩阵中，被列为标准化成熟度最高推荐'
    ],
    statValue: '+180% 意向线索',
    preRate: '18%',
    preWidth: '18%',
    postRate: '94%',
    postWidth: '94%',
    clientQuote: '现在加盟商极为理智，先用千问把加盟政策和倒闭率扒个底朝天。帮我们建立公信力数据资产后，AI 回答全是中央厨房和冷链优势，谈单轻松太多了。',
    authorInitial: '陈',
    clientName: '陈总',
    clientTitle: '连锁餐饮总部 · 全国招商总监',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>'
  },
  {
    id: 'medical',
    name: '专科医疗齿科',
    category: '大健康与高净值专科',
    defaultBrand: '恒伦口腔',
    headline: '重塑种植牙权威声誉，化解公域负面疑虑，首诊预约提升 150%',
    scenarioQuery: '“本地种植牙哪家专科医院技术靠谱收费透明无隐形增项？”',
    tactics: [
      '深度覆盖企查查医疗合规公示与卫健委执业医师备案真实引用',
      '在知乎与权威健康门户发布种植牙集采避坑指南与数字化导板横评',
      '大模型回答中明确标识“资质合规、收费透明”，成为同城首诊推荐'
    ],
    statValue: '+150% 首诊率',
    preRate: '8%',
    preWidth: '8%',
    postRate: '86%',
    postWidth: '86%',
    clientQuote: '患者最怕过度消费。大模型把卫健委备案和明码标价直接引述出来，相当于权威机构替我们做了背书，转化率非常惊人！',
    authorInitial: '王',
    clientName: '王院长',
    clientTitle: '数字化口腔专科门诊 · 业务院长',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20"></path><circle cx="12" cy="12" r="9"></circle></svg>'
  },
  {
    id: 'legal',
    name: '商务咨询律所',
    category: '高端专业服务与合规',
    defaultBrand: '金杜律所',
    headline: '打破传统熟人介绍局限，在大模型企业采购决策流中直获常法委托',
    scenarioQuery: '“企业常年法律顾问与复杂商事纠纷解决律所哪家专业？”',
    tactics: [
      '定向发布行业重大商事经典判例研报，建立包含胜诉率的高权重词条',
      '沉淀专业委员会任职、知识产权与股权设计专家知识实体',
      '通义千问与 DeepSeek 商业评测中，以高响应度重点推介给企业'
    ],
    statValue: '新增 3 家常法',
    preRate: '5%',
    preWidth: '5%',
    postRate: '91%',
    postWidth: '91%',
    clientQuote: '许多拟上市企业的董秘和法务用通义千问寻找擅长股权合规的律所，AI 把胜诉案例列在第一位，直接为我们带来了两家优质企业客户！',
    authorInitial: '周',
    clientName: '周律师',
    clientTitle: '知名商事律所 · 高级合伙人',
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18M3 9l9-6 9 6M6 12l-3 6h6l-3-6zM18 12l-3 6h6l-3-6z"></path></svg>'
  }
];

const currentIndustry = computed(() => industries[activeIndustryIndex.value]);

// 四层认知工程架构
const archLayers = [
  {
    name: '知识本体确权工程',
    enName: 'Schema & Entity Ontology',
    desc: '在权威百科完成词条认证，注入 Schema.org 结构化元数据，确立大模型 RAG 召回的唯一法定身份。',
    items: [
      '企业本体词条全量认证过审',
      'Schema.org 知识图谱元数据注入',
      '排除歧义同名实体干扰'
    ],
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>'
  },
  {
    name: '权威信源公信力矩阵',
    enName: 'Authority Citation Feeder',
    desc: '穿透搜狐、新浪、网易、知乎等高权重门户，定向投喂 15~20 篇客观专业测评研报，建立可信证据链。',
    items: [
      '大模型高权重引爆炸点媒体矩阵',
      '第三方客观横评与真实案例背书',
      '权威索引长期保留与反稀释'
    ],
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#818CF8" stroke-width="2"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>'
  },
  {
    name: '采购意图精准拦截',
    enName: 'Intent Interception Grid',
    desc: '围绕“哪家好”、“选型对比”、“避坑评测”等 50+ 行业高频意向词，构建标准化问答库，抢占第一梯队。',
    items: [
      '50+ 行业采购决策意向词覆盖',
      '反制竞品恶意单向对比霸屏',
      '大模型首推胜率稳定 85% 以上'
    ],
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>'
  },
  {
    name: '双端攻防全天候雷达',
    enName: 'Dual-End Telemetry Radar',
    desc: '手机端生活圈 + PC 知识库切面 24/7 自动化巡检，实时预警大模型更新、知识漂移与竞品反扑。',
    items: [
      '覆盖 5 大基座大模型双端切面',
      '每周自动化巡检报表推送',
      '算法更新与模型漂移秒级预警'
    ],
    svg: '<svg viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
  }
];

// 30 天闭环交付体系
const roadmapSteps = [
  {
    phase: '01',
    days: 'Day 1 - Day 7',
    title: '品牌专有词确权与 Schema 结构化注入',
    action: '建立专属企业本体实体，完成百科词条认证及 Schema.org 结构化标记，建立大模型 RAG 召回根基。',
    deliverable: '《企业知识本体架构书》、官方百科词条过审、Schema 实体标签认证'
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
    deliverable: '《GEO 优化终审成果报表》、开通【交付期数据监控看板】账号'
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
/* ================= 全局容器与页面重置 ================= */
.landing-container {
  min-height: 100vh;
  background-color: #080C14;
  color: #1E293B;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  overflow-x: clip;
  padding-top: 68px; /* 为绝对固定顶部导航留出空间 */
}

/* ================= 1. 绝对固定顶部导航栏 (Fixed Header) ================= */
.landing-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 68px;
  z-index: 1000;
  background: rgba(8, 12, 20, 0.88);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
}

.header-inner {
  max-width: 1320px;
  height: 100%;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  text-decoration: none;
}

.logo-aura-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.logo-soft-glow {
  position: absolute;
  inset: -10px -18px;
  background: radial-gradient(ellipse at center, rgba(59, 130, 246, 0.45) 0%, rgba(168, 85, 247, 0.25) 50%, transparent 72%);
  filter: blur(14px);
  pointer-events: none;
  opacity: 0.75;
}

.logo-unconstrained {
  position: relative;
  height: 38px;
  width: auto;
  max-width: 155px;
  object-fit: contain;
  filter: drop-shadow(0 2px 10px rgba(25, 90, 254, 0.35));
}

.brand-badge-tag {
  background: linear-gradient(135deg, #195AFE, #7C3AED);
  color: #ffffff;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 0.15rem 0.5rem;
  border-radius: 6px;
  letter-spacing: 0.5px;
  box-shadow: 0 0 10px rgba(25, 90, 254, 0.4);
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
  transition: color 0.2s;
}

.nav-item:hover {
  color: #FFFFFF;
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
  padding: 0.42rem 0.85rem;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.03);
  transition: all 0.2s;
}

.btn-ghost-nav:hover {
  background: rgba(255, 255, 255, 0.08);
  color: #FFFFFF;
}

.btn-primary-nav {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  text-decoration: none;
  padding: 0.48rem 1.15rem;
  border-radius: 9999px;
  font-size: 0.88rem;
  font-weight: 700;
  color: #ffffff;
  overflow: hidden;
  background: linear-gradient(135deg, #195AFE 0%, #3B82F6 50%, #7C3AED 100%);
  box-shadow: 0 0 20px rgba(25, 90, 254, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary-nav:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 28px rgba(25, 90, 254, 0.65);
}

.btn-svg-arrow {
  width: 14px;
  height: 14px;
}

/* ================= 2. 首屏 Hero 区域 (含首屏可见跑马灯) ================= */
.hero-section {
  position: relative;
  padding: 4rem 1.5rem 4rem;
  background: #080C14;
  overflow: hidden;
  color: #F8FAFC;
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
  top: -80px;
  left: -80px;
  background: radial-gradient(circle, rgba(25, 90, 254, 0.22) 0%, transparent 70%);
}

.orb-purple {
  width: 600px;
  height: 600px;
  top: 10%;
  right: -100px;
  background: radial-gradient(circle, rgba(124, 58, 237, 0.18) 0%, transparent 70%);
}

.grid-overlay {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
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
  padding: 0.36rem 1.1rem;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 600;
  color: #93C5FD;
  margin-bottom: 1.8rem;
  backdrop-filter: blur(12px);
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

.badge-link {
  display: inline-flex;
  align-items: center;
  gap: 0.2rem;
  color: #FFFFFF;
  text-decoration: underline;
  text-underline-offset: 3px;
  margin-left: 0.4rem;
}

.pill-arrow {
  width: 12px;
  height: 12px;
}

.hero-headline {
  font-size: 3.8rem;
  font-weight: 900;
  line-height: 1.22;
  letter-spacing: -1.2px;
  color: #ffffff;
  margin: 0 0 1.2rem 0;
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
  margin: 0 0 2.6rem 0;
}

/* 搜索框 */
.hero-search-wrapper {
  width: 100%;
  max-width: 860px;
  margin-bottom: 2.8rem;
}

.search-input-box {
  position: relative;
  display: flex;
  align-items: center;
  background: rgba(15, 22, 38, 0.85);
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
  gap: 0.45rem;
  color: #CBD5E1;
  font-size: 0.88rem;
  font-weight: 600;
  white-space: nowrap;
}

.mode-svg {
  width: 16px;
  height: 16px;
  color: #60A5FA;
}

.mode-caret-svg {
  width: 14px;
  height: 14px;
  color: #64748B;
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
}

.btn-search-action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #195AFE 0%, #3B82F6 45%, #7C3AED 100%);
  border: none;
  border-radius: 9999px;
  padding: 0.82rem 1.8rem;
  color: #ffffff;
  font-size: 0.96rem;
  font-weight: 700;
  cursor: pointer;
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
  gap: 0.45rem;
}

.action-svg {
  width: 16px;
  height: 16px;
}

/* 标杆 Chips (极简无框微粒) */
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
}

.chip-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #CBD5E1;
  font-size: 0.82rem;
  font-weight: 500;
  padding: 0.28rem 0.8rem;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 0.2s;
}

.chip-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #38BDF8;
}

.chip-btn:hover {
  background: rgba(25, 90, 254, 0.15);
  border-color: rgba(25, 90, 254, 0.4);
  color: #93C5FD;
}

/* ================= 首屏跑马灯 (首屏可见，高端无框矢量标) ================= */
.hero-trust-marquee-container {
  width: 100%;
  margin-top: 1.5rem;
}

.trust-marquee-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1.4rem;
}

.trust-line {
  height: 1px;
  width: 60px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15));
}

.trust-line:last-child {
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.15), transparent);
}

.trust-title-text {
  font-size: 0.84rem;
  font-weight: 600;
  color: #94A3B8;
  letter-spacing: 0.6px;
  text-transform: uppercase;
}

.trust-marquee-track-wrap {
  width: 100%;
  overflow: hidden;
  mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
}

.trust-marquee-track {
  display: flex;
  align-items: center;
  gap: 1.6rem;
  white-space: nowrap;
  animation: marqueeScroll 45s linear infinite;
}

.trust-marquee-track-wrap:hover .trust-marquee-track {
  animation-play-state: paused;
}

@keyframes marqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

.trust-brand-item {
  display: inline-flex;
  align-items: center;
  gap: 0.9rem;
  padding: 0.65rem 1.25rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  transition: all 0.2s ease;
}

.trust-brand-item:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(56, 189, 248, 0.35);
}

.brand-svg-symbol {
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.brand-svg-symbol svg {
  width: 100%;
  height: 100%;
}

.brand-meta {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.brand-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #F1F5F9;
}

.brand-role {
  font-size: 0.74rem;
  color: #64748B;
}

.brand-live-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 6px #10B981;
}

/* ================= 3. 浅色清爽区域：流量趋势与简约图表 ================= */
.light-section-contrast {
  background: #F8FAFC;
  padding: 6rem 1.5rem;
  color: #0F172A;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
}

.section-header-center {
  text-align: center;
  max-width: 840px;
  margin: 0 auto 3.5rem auto;
}

.light-badge {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 1.2px;
  color: #0284C7;
  background: #E0F2FE;
  border: 1px solid #BAE6FD;
  padding: 0.3rem 0.9rem;
  border-radius: 9999px;
  margin-bottom: 1.2rem;
}

.light-title {
  font-size: 2.75rem;
  font-weight: 900;
  line-height: 1.25;
  color: #0F172A;
  letter-spacing: -0.8px;
  margin: 0 0 1.2rem 0;
}

.text-gradient-blue {
  background: linear-gradient(135deg, #0284C7 0%, #2563EB 50%, #7C3AED 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.light-sub {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.7;
  margin: 0;
}

/* 简约数据图表 1 (SVG 折线图) */
.data-chart-card {
  max-width: 1140px;
  margin: 0 auto 4rem auto;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 20px;
  padding: 2.2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
}

.chart-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.8rem;
}

.chart-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: #0F172A;
  margin: 0 0 0.4rem 0;
}

.chart-sub-note {
  font-size: 0.84rem;
  color: #64748B;
}

.chart-legend-group {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  font-size: 0.84rem;
  font-weight: 600;
  color: #334155;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.legend-line {
  width: 24px;
  height: 3px;
  border-radius: 2px;
}

.line-cyan {
  background: linear-gradient(90deg, #38BDF8, #2563EB);
}

.line-gray {
  background: #94A3B8;
  border-style: dashed;
}

.svg-chart-container {
  width: 100%;
}

.trend-chart-svg {
  width: 100%;
  height: 240px;
}

.chart-x-axis {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #64748B;
  font-weight: 500;
  margin-top: 0.8rem;
  padding: 0 1rem;
}

.highlight-axis {
  color: #2563EB;
  font-weight: 700;
}

/* 范式转移滑块 (浅色风格) */
.light-shift-slider {
  max-width: 1140px;
  margin: 0 auto;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
}

.light-slider-tabs {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  background: #F1F5F9;
  border-bottom: 1px solid #E2E8F0;
}

.light-tab-btn {
  background: transparent;
  border: none;
  padding: 1.2rem;
  text-align: left;
  cursor: pointer;
}

.light-tab-progress {
  width: 100%;
  height: 3px;
  background: #CBD5E1;
  border-radius: 9999px;
  margin-bottom: 0.8rem;
  overflow: hidden;
}

.light-progress-bar {
  height: 100%;
  background: #2563EB;
  transition: width 0.1s linear;
}

.light-tab-meta {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.tab-idx {
  font-size: 0.8rem;
  font-weight: 800;
  color: #64748B;
}

.light-tab-btn.active .tab-idx {
  color: #2563EB;
}

.tab-txt {
  font-size: 0.95rem;
  font-weight: 700;
  color: #475569;
}

.light-tab-btn.active .tab-txt {
  color: #0F172A;
}

.light-slider-content {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 3rem;
  padding: 3rem;
  align-items: center;
}

.slide-tag-pill {
  font-size: 0.78rem;
  font-weight: 800;
  color: #2563EB;
  letter-spacing: 0.8px;
  display: inline-block;
  margin-bottom: 0.8rem;
}

.slide-title-clean {
  font-size: 1.85rem;
  font-weight: 800;
  line-height: 1.35;
  color: #0F172A;
  margin: 0 0 1rem 0;
}

.slide-desc-clean {
  font-size: 0.96rem;
  color: #475569;
  line-height: 1.7;
  margin: 0 0 1.6rem 0;
}

.slide-bullets {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}

.bullet-row {
  display: flex;
  align-items: flex-start;
  gap: 0.6rem;
  font-size: 0.9rem;
  color: #334155;
}

.bullet-check-svg {
  width: 18px;
  height: 18px;
  color: #059669;
  flex-shrink: 0;
  margin-top: 2px;
}

.slide-stat-panel {
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 1.8rem;
}

.stat-highlight-box {
  text-align: center;
  margin-bottom: 1.5rem;
}

.stat-big-num {
  font-size: 3.2rem;
  font-weight: 900;
  color: #0F172A;
  line-height: 1;
}

.stat-unit-text {
  font-size: 1.1rem;
  font-weight: 700;
  color: #2563EB;
  margin-top: 0.2rem;
}

.stat-desc-label {
  font-size: 0.85rem;
  color: #64748B;
  margin-top: 0.4rem;
}

.contrast-flow-box {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.contrast-row {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  padding: 0.8rem 1rem;
  border-radius: 8px;
  font-size: 0.82rem;
}

.contrast-row.bad {
  background: #FEF2F2;
  border: 1px solid #FEE2E2;
}

.contrast-row.bad .status-tag {
  color: #DC2626;
  font-weight: 800;
}

.contrast-row.good {
  background: #ECFDF5;
  border: 1px solid #D1FAE5;
}

.contrast-row.good .status-tag {
  color: #059669;
  font-weight: 800;
}

/* ================= 4. 白色清爽区域：行业解决方案 ================= */
.light-section-solutions {
  background: #FFFFFF;
  padding: 5.5rem 1.5rem 6.5rem;
  border-bottom: 1px solid #E2E8F0;
}

.industry-pills-row {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 3rem;
}

.ind-clean-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  background: #F1F5F9;
  border: 1px solid #E2E8F0;
  padding: 0.65rem 1.3rem;
  border-radius: 9999px;
  color: #475569;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.ind-clean-pill:hover {
  background: #E2E8F0;
  color: #0F172A;
}

.ind-clean-pill.active {
  background: #0F172A;
  border-color: #0F172A;
  color: #FFFFFF;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.2);
}

.pill-svg-icon {
  width: 18px;
  height: 18px;
}

.pill-svg-icon svg {
  width: 100%;
  height: 100%;
}

.industry-light-card {
  max-width: 1180px;
  margin: 0 auto;
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 20px;
  padding: 3rem;
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 3.5rem;
}

.ind-badge-category {
  font-size: 0.8rem;
  font-weight: 800;
  color: #2563EB;
  letter-spacing: 0.8px;
  margin-bottom: 0.6rem;
}

.ind-card-headline {
  font-size: 1.7rem;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.35;
  margin: 0 0 1.4rem 0;
}

.ind-query-container {
  background: #FFFFFF;
  border-left: 3px solid #2563EB;
  border-radius: 0 8px 8px 0;
  padding: 0.9rem 1.2rem;
  margin-bottom: 1.4rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

.query-top-label {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.75rem;
  font-weight: 700;
  color: #64748B;
  margin-bottom: 0.3rem;
}

.query-icon-svg {
  width: 14px;
  height: 14px;
}

.query-body-text {
  font-size: 0.96rem;
  font-weight: 700;
  color: #0F172A;
}

.tactics-head {
  font-size: 0.88rem;
  font-weight: 800;
  color: #334155;
  margin: 0 0 0.8rem 0;
}

.tactic-line {
  display: flex;
  align-items: flex-start;
  gap: 0.6rem;
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}

.t-step-idx {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #E0F2FE;
  color: #0284C7;
  font-size: 0.72rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 3px;
}

.btn-ind-clean {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #0F172A;
  color: #ffffff;
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  font-size: 0.92rem;
  font-weight: 700;
  margin-top: 1.5rem;
  transition: all 0.2s;
}

.btn-ind-clean:hover {
  background: #1E293B;
  transform: translateY(-2px);
}

.arrow-svg {
  width: 16px;
  height: 16px;
}

.stat-clean-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 1.8rem;
  margin-bottom: 1.5rem;
}

.stat-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.6rem;
}

.stat-title-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: #64748B;
}

.stat-trend-tag {
  font-size: 0.75rem;
  font-weight: 700;
  color: #059669;
  background: #D1FAE5;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.stat-number-display {
  font-size: 2.2rem;
  font-weight: 900;
  color: #0F172A;
  margin-bottom: 1.4rem;
}

.bar-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.78rem;
  color: #475569;
  font-weight: 600;
  margin-bottom: 0.3rem;
}

.mt-3 {
  margin-top: 0.8rem;
}

.text-red { color: #DC2626; }
.text-green { color: #059669; }

.bar-track-bg {
  height: 7px;
  background: #F1F5F9;
  border-radius: 9999px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  border-radius: 9999px;
}

.bar-fill.red { background: #EF4444; }
.bar-fill.green { background: #10B981; }

.testimonial-light-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 1.5rem;
}

.quote-text-clean {
  font-size: 0.88rem;
  color: #334155;
  line-height: 1.65;
  font-style: italic;
  margin-bottom: 1rem;
}

.quote-author-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.author-avatar-badge {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #E2E8F0;
  color: #0F172A;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.88rem;
}

.author-name {
  font-size: 0.85rem;
  font-weight: 700;
  color: #0F172A;
}

.author-title {
  font-size: 0.74rem;
  color: #64748B;
}

.author-verified {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.72rem;
  font-weight: 700;
  color: #059669;
}

.v-check-svg {
  width: 14px;
  height: 14px;
}

/* ================= 5. 深色科技底座：四层认知工程架构 ================= */
.dark-tech-section {
  background: #080C14;
  padding: 6rem 1.5rem;
  color: #F8FAFC;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.font-reduced {
  font-size: 2.8rem;
}

.arch-clean-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

.arch-clean-card {
  background: #0E1526;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 18px;
  padding: 2rem 1.5rem;
  transition: transform 0.3s, border-color 0.3s;
}

.arch-clean-card:hover {
  transform: translateY(-4px);
  border-color: rgba(56, 189, 248, 0.45);
}

.arch-header-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.4rem;
}

.arch-svg-wrap {
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.arch-svg-wrap svg {
  width: 100%;
  height: 100%;
}

.arch-layer-code {
  font-size: 0.72rem;
  font-weight: 800;
  color: #64748B;
  letter-spacing: 1px;
}

.arch-card-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: #FFFFFF;
  margin: 0 0 0.25rem 0;
}

.arch-en-code {
  font-size: 0.75rem;
  color: #64748B;
  margin-bottom: 1rem;
}

.arch-card-summary {
  font-size: 0.84rem;
  color: #94A3B8;
  line-height: 1.6;
  margin-bottom: 1.4rem;
}

.arch-item-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 1rem;
}

.arch-item-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  color: #CBD5E1;
}

.item-square {
  width: 5px;
  height: 5px;
  border-radius: 1px;
  background: #38BDF8;
}

/* ================= 6. 白色清爽区域：30天交付与商业账本 ================= */
.light-section-roadmap {
  background: #F8FAFC;
  padding: 6rem 1.5rem;
  color: #0F172A;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
}

.roadmap-light-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  max-width: 1180px;
  margin: 0 auto;
}

.roadmap-step-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 1.8rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
}

.step-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.step-num-pill {
  font-size: 0.75rem;
  font-weight: 800;
  color: #2563EB;
}

.step-days-tag {
  font-size: 0.75rem;
  color: #64748B;
  background: #F1F5F9;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.step-card-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: #0F172A;
  margin: 0 0 0.65rem 0;
  line-height: 1.4;
}

.step-card-action {
  font-size: 0.84rem;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 1.2rem;
}

.step-deliverable-box {
  background: #F8FAFC;
  border-radius: 8px;
  padding: 0.75rem;
}

.del-label {
  font-size: 0.72rem;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 0.2rem;
}

.del-text {
  font-size: 0.76rem;
  color: #64748B;
  line-height: 1.45;
}

/* 商业账本表格 */
.roi-ledger-wrap {
  margin-top: 3rem;
}

.mt-5 {
  margin-top: 4rem;
}

.roi-clean-table-card {
  max-width: 1140px;
  margin: 0 auto;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.04);
}

.roi-row {
  display: grid;
  grid-template-columns: 1fr 1.3fr 1.3fr 1.5fr;
  padding: 1.2rem 1.5rem;
  font-size: 0.86rem;
  border-bottom: 1px solid #F1F5F9;
  align-items: center;
}

.roi-row:last-child {
  border-bottom: none;
}

.roi-row.table-head {
  background: #F8FAFC;
  font-weight: 800;
  color: #334155;
  border-bottom: 1px solid #E2E8F0;
}

.head-highlight {
  color: #2563EB;
}

.font-bold-dark {
  font-weight: 700;
  color: #0F172A;
}

.text-muted {
  color: #64748B;
}

.cell-highlight {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  color: #0F172A;
  font-weight: 600;
  background: #EFF6FF;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border-left: 2px solid #2563EB;
}

.check-svg {
  width: 16px;
  height: 16px;
  color: #059669;
  flex-shrink: 0;
}

/* ================= 7. FAQ 常见问题 ================= */
.light-section-faq {
  background: #FFFFFF;
  padding: 5rem 1.5rem 6rem;
  border-bottom: 1px solid #E2E8F0;
}

.faq-clean-list {
  max-width: 860px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.faq-clean-item {
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 1.25rem 1.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.faq-clean-item:hover {
  border-color: #CBD5E1;
}

.faq-clean-item.open {
  background: #FFFFFF;
  border-color: #2563EB;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.08);
}

.faq-q-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.faq-q-symbol {
  font-size: 0.88rem;
  font-weight: 800;
  color: #2563EB;
}

.faq-q-title {
  flex: 1;
  font-size: 1.02rem;
  font-weight: 700;
  color: #0F172A;
}

.faq-toggle-icon {
  font-size: 1.3rem;
  font-weight: 600;
  color: #64748B;
}

.faq-a-body {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #E2E8F0;
}

.faq-a-body p {
  font-size: 0.92rem;
  color: #475569;
  line-height: 1.7;
  margin: 0;
}

/* ================= 8. 转化底栏 ================= */
.bottom-cta-banner {
  position: relative;
  padding: 6.5rem 1.5rem;
  background: #080C14;
  overflow: hidden;
  text-align: center;
  color: #FFFFFF;
}

.cta-cosmic-glow {
  position: absolute;
  inset: -100px;
  background: radial-gradient(circle at 50% 50%, rgba(25, 90, 254, 0.25) 0%, rgba(124, 58, 237, 0.2) 35%, rgba(255, 109, 3, 0.12) 65%, transparent 80%);
  pointer-events: none;
  filter: blur(80px);
}

.cta-inner {
  max-width: 860px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.badge-tag-orange {
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
  margin: 0 0 1.2rem 0;
}

.cta-sub {
  font-size: 1.05rem;
  color: #94A3B8;
  margin: 0 0 2.5rem 0;
}

.cta-action-box {
  max-width: 620px;
  margin: 0 auto;
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
  background: linear-gradient(135deg, #195AFE 0%, #3B82F6 50%, #7C3AED 100%);
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
}

.btn-arrow {
  width: 14px;
  height: 14px;
}

/* ================= 9. 页脚 ================= */
.landing-footer {
  background: #04070D;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding: 4.5rem 1.5rem 2rem;
  color: #64748B;
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
  margin-bottom: 1.2rem;
}

.f-logo-img {
  height: 34px;
  width: auto;
  object-fit: contain;
}

.footer-slogan {
  font-size: 0.85rem;
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
  .light-slider-tabs { grid-template-columns: repeat(2, 1fr); }
  .light-slider-content { grid-template-columns: 1fr; gap: 2rem; padding: 2rem; }
  .industry-light-card { grid-template-columns: 1fr; padding: 2rem; gap: 2rem; }
  .arch-clean-grid { grid-template-columns: repeat(2, 1fr); }
  .roadmap-light-grid { grid-template-columns: repeat(2, 1fr); }
  .footer-inner { grid-template-columns: 1fr 1fr; gap: 2rem; }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .hero-headline { font-size: 2.2rem; }
  .hero-subtext { font-size: 0.95rem; }
  .light-slider-tabs { grid-template-columns: 1fr; }
  .arch-clean-grid { grid-template-columns: 1fr; }
  .roadmap-light-grid { grid-template-columns: 1fr; }
  .roi-row { grid-template-columns: 1fr; gap: 0.5rem; }
  .footer-inner { grid-template-columns: 1fr; gap: 2rem; }
  .cta-headline { font-size: 1.85rem; }
  .cta-input-wrap { flex-direction: column; border-radius: 16px; padding: 0.8rem; gap: 0.8rem; }
  .btn-cta-submit { width: 100%; justify-content: center; }
  .search-input-box { flex-direction: column; border-radius: 20px; padding: 0.8rem; gap: 0.8rem; }
  .search-divider { display: none; }
  .btn-search-action { width: 100%; }
}
</style>
