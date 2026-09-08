<template>
  <div class="landing-container">
    <!-- 1. 极简磨砂导航栏 (Header) -->
    <header class="landing-header">
      <div class="header-inner">
        <router-link to="/" class="brand-link">
          <div class="logo-capsule">
            <img src="/logo-white.png" alt="蜉蝣小宝" class="logo-img" />
          </div>
          <div class="brand-text-wrap">
            <span class="brand-name">蜉蝣小宝</span>
            <span class="brand-en">MAYFLY GEO</span>
          </div>
        </router-link>

        <nav class="nav-links">
          <a href="#shift" class="nav-item">范式演进</a>
          <a href="#features" class="nav-item">核心能力</a>
          <a href="#solutions" class="nav-item">行业解决方案</a>
          <a href="#roadmap" class="nav-item">30天交付</a>
          <a href="#roi" class="nav-item">商业账本</a>
        </nav>

        <div class="header-actions">
          <router-link to="/console" class="btn-ghost-nav">进入诊断工作台</router-link>
          <router-link to="/console" class="btn-primary-nav">
            免费启动 AI 体检
            <span class="arrow">→</span>
          </router-link>
        </div>
      </div>
    </header>

    <!-- 2. 品牌首屏 (Hero Section) - 纯品牌展示，克制从容 -->
    <section class="hero-section">
      <div class="hero-ambient-glow"></div>
      <div class="section-inner hero-inner">
        <div class="hero-pill-badge">
          <span class="badge-dot"></span>
          <span class="badge-text">2026 新一代企业生成式引擎优化 · GEO 认知工程</span>
        </div>

        <h1 class="hero-headline">
          当 5 亿客户向 AI 提问时，<br />
          让您的品牌成为 <span class="text-gradient">第一推荐</span>
        </h1>

        <p class="hero-subtext">
          穿透字节跳动·豆包、深度求索·DeepSeek、阿里通义千问等主流大模型推荐决策层。<br />
          测算全网潜在客源流失，构建专属于企业的生成式引擎知识资产与权威信源护城河。
        </p>

        <div class="hero-cta-group">
          <router-link to="/console" class="btn-hero-primary">
            <span>免费启动企业 AI 体检</span>
            <span class="btn-arrow">→</span>
          </router-link>
          <router-link to="/diagnostic_report" class="btn-hero-secondary">
            <span>查阅标杆客户体检书</span>
          </router-link>
        </div>

        <!-- 首屏高精度静质感 UI 预览画报 (Apple / Similarweb 风格，无晃眼动效) -->
        <div class="hero-mockup-frame">
          <div class="mockup-header-bar">
            <div class="mockup-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-amber"></span>
              <span class="dot dot-green"></span>
            </div>
            <div class="mockup-search-sim">
              <span class="sim-icon">🔍</span>
              <span class="sim-query">“2026年 优质数控工业激光切割机厂家哪家口碑好？”</span>
            </div>
            <div class="mockup-status-tag">🟢 5 大基座大模型直连实测中</div>
          </div>

          <div class="mockup-body-content">
            <!-- 左侧：大模型生成式回答仿真 -->
            <div class="mockup-response-panel">
              <div class="panel-header">
                <span class="ai-avatar">🤖</span>
                <div class="ai-meta">
                  <div class="ai-title">字节跳动 · 豆包手机端与全网知识库聚合推荐</div>
                  <div class="ai-sub">基于全网 19 篇权威资讯、政务合规资质及同城生活圈实时检索召回</div>
                </div>
              </div>

              <div class="panel-body">
                <div class="ai-quote-lead">
                  “结合全网工业制造资质核验、国家专利储备及下游制造业客户实地走访，在激光切管机领域重点推荐：”
                </div>

                <div class="ai-recommend-card target-highlight">
                  <div class="rec-badge">🏆 首选第一推荐梯队 · 官方知识本体认证</div>
                  <div class="rec-title">恒瑞智能装备（企业主体：无锡恒瑞智能装备科技有限公司）</div>
                  <div class="rec-desc">
                    📍 辐射产业带：华东及全国装备基地 · 💡 核心优势：掌握重管激光切割核心工艺，企查查与知识产权资质完备，在各大工业评测中综合评分位列榜首。
                  </div>
                  <div class="rec-tags">
                    <span class="rtag tag-green">✓ 百度百科认证</span>
                    <span class="rtag tag-blue">✓ 搜狐/新浪权威研报收录</span>
                    <span class="rtag tag-indigo">✓ 0 被同行截流</span>
                  </div>
                </div>

                <div class="ai-competitor-faded">
                  <span class="comp-title">其他参考品牌：</span>
                  <span class="comp-name">大族激光</span> · 
                  <span class="comp-name">宏山激光</span> · 
                  <span class="comp-name">百超迪能</span>
                </div>
              </div>
            </div>

            <!-- 右侧：GEO 商业指标遥测看板 -->
            <div class="mockup-telemetry-panel">
              <div class="telemetry-card highlight-card">
                <div class="t-label">AI 搜索综合可见度</div>
                <div class="t-val-wrap">
                  <span class="t-val text-green">92</span>
                  <span class="t-unit">分 (行业首推)</span>
                </div>
                <div class="t-bar-wrap">
                  <div class="t-bar-fill" style="width: 92%"></div>
                </div>
              </div>

              <div class="telemetry-card">
                <div class="t-label">意图词穿透渗透率</div>
                <div class="t-val-wrap">
                  <span class="t-val text-blue">88.5%</span>
                  <span class="t-tag-growth">↑ 64%</span>
                </div>
                <div class="t-sub">50+ 高频采购搜索场景已全面建立防御</div>
              </div>

              <div class="telemetry-card">
                <div class="t-label">月度商业潜客挽回预估</div>
                <div class="t-val-wrap">
                  <span class="t-val text-slate">￥240,000</span>
                  <span class="t-unit">/月</span>
                </div>
                <div class="t-sub">规避因公域声量空白导致的客源被动流失</div>
              </div>

              <div class="telemetry-model-chips">
                <div class="m-chip chip-on">豆包 94%</div>
                <div class="m-chip chip-on">DeepSeek 91%</div>
                <div class="m-chip chip-on">千问 89%</div>
                <div class="m-chip chip-on">元宝 93%</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. 大模型生态原生穿透跑马区 (Model Ecosystem) -->
    <section class="ecosystem-strip">
      <div class="section-inner">
        <p class="ecosystem-title">原生穿透并深度适配中国主流生成式 AI 搜索推荐决策层</p>
        <div class="ecosystem-logos">
          <div class="logo-item"><span class="logo-circle">豆</span> 字节跳动 · 豆包</div>
          <div class="logo-item"><span class="logo-circle">DS</span> 深度求索 · DeepSeek</div>
          <div class="logo-item"><span class="logo-circle">千</span> 阿里巴巴 · 通义千问</div>
          <div class="logo-item"><span class="logo-circle">元</span> 腾讯混元 · 元宝</div>
          <div class="logo-item"><span class="logo-circle">文</span> 百度 · 文心一言</div>
          <div class="logo-item"><span class="logo-circle">Ki</span> 月之暗面 · Kimi</div>
        </div>
      </div>
    </section>

    <!-- 4. 搜索范式断代演进对比 (The Paradigm Shift) -->
    <section class="section shift-section" id="shift">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="sec-kicker">THE PARADIGM SHIFT</span>
          <h2 class="sec-title">为什么传统的 SEO 与竞价正在全面失效？</h2>
          <p class="sec-subtitle">
            从「被动点击网页」到「AI 直接提炼唯一决策」，企业的公域获客入口正在经历 20 年来最大的洗牌。
          </p>
        </div>

        <div class="shift-grid">
          <!-- 传统时代 -->
          <div class="shift-card card-old">
            <div class="card-status-badge badge-faded">过去 20 年 · 传统网页检索时代</div>
            <h3 class="shift-card-title">10 个蓝色链接与高企的竞价内卷</h3>
            <ul class="shift-points">
              <li>
                <span class="point-icon red">✕</span>
                <div class="point-desc">
                  <strong>用户需逐一点击翻页</strong>：注意力高度分散，第 2 页之后的链接点击率趋近于 0。
                </div>
              </li>
              <li>
                <span class="point-icon red">✕</span>
                <div class="point-desc">
                  <strong>竞价点击成本飞涨</strong>：按次付费竞争激烈，充斥大量无效点击与同行恶意消耗。
                </div>
              </li>
              <li>
                <span class="point-icon red">✕</span>
                <div class="point-desc">
                  <strong>年轻一代决策者全面迁徙</strong>：B2B 采购与高净值客户已习惯直接向 AI 要结论。
                </div>
              </li>
              <li>
                <span class="point-icon red">✕</span>
                <div class="point-desc">
                  <strong>官网缺乏 Schema 结构化元数据</strong>：大模型爬虫抓取后无法解析，直接过滤淘汰。
                </div>
              </li>
            </ul>
          </div>

          <!-- 生成式 AI 时代 -->
          <div class="shift-card card-new">
            <div class="card-status-badge badge-active">未来 10 年 · 生成式 AI (GEO) 时代</div>
            <h3 class="shift-card-title">AI 直接提炼结论，首推即垄断</h3>
            <ul class="shift-points">
              <li>
                <span class="point-icon green">✓</span>
                <div class="point-desc">
                  <strong>AI 输出唯一合成回答</strong>：首位推荐独占 85% 真实咨询决策，未被提及即彻底隐形。
                </div>
              </li>
              <li>
                <span class="point-icon green">✓</span>
                <div class="point-desc">
                  <strong>零单次点击成本</strong>：一次性构建知识本体与权威信源，形成长期复利的品牌自然护城河。
                </div>
              </li>
              <li>
                <span class="point-icon green">✓</span>
                <div class="point-desc">
                  <strong>全域决策流精准拦截</strong>：同时穿透手机端同城生活圈口碑与 PC 端 B2B 招投标决策。
                </div>
              </li>
              <li>
                <span class="point-icon green">✓</span>
                <div class="point-desc">
                  <strong>大模型算力深度信任</strong>：通过高权重信源矩阵与百科认证，让 AI 主动将贵司视为标杆。
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. 四维 GEO 核心工程架构 (Bento Grid) -->
    <section class="section features-section" id="features">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="sec-kicker">CORE PLATFORM ARCHITECTURE</span>
          <h2 class="sec-title">四维 GEO 认知工程：让大模型主动信服并推荐</h2>
          <p class="sec-subtitle">
            告别玄学黑盒，以大模型底层 RAG 检索与知识图谱算法为依据，提供全链路工程化解决方案。
          </p>
        </div>

        <div class="bento-grid">
          <!-- Bento 1 -->
          <div class="bento-card">
            <div class="bento-icon-wrap icon-blue">🏷️</div>
            <h3 class="bento-title">企业知识本体确权 (Schema & Entity)</h3>
            <p class="bento-desc">
              针对企业全称与核心品牌，在全网建立专属企业知识图谱，通过百度百科认证与 Schema.org 结构化元数据标记，建立大模型 RAG 召回索引根基。
            </p>
            <div class="bento-metric-tag">
              <span>基础召回层 (Recall)：</span><strong>提升至 100% 精准识别</strong>
            </div>
          </div>

          <!-- Bento 2 -->
          <div class="bento-card">
            <div class="bento-icon-wrap icon-green">📰</div>
            <h3 class="bento-title">高权重权威信源矩阵定向投喂</h3>
            <p class="bento-desc">
              针对 DeepSeek、豆包、通义千问优先采信的国家级门户（新浪、搜狐、网易）、知乎专栏长文与政务白名单，定向投喂深度专业测评研报与交付实录。
            </p>
            <div class="bento-metric-tag">
              <span>公信力权重：</span><strong>彻底消除“缺乏第三方背书”负向标签</strong>
            </div>
          </div>

          <!-- Bento 3 -->
          <div class="bento-card">
            <div class="bento-icon-wrap icon-indigo">📱</div>
            <h3 class="bento-title">双端全域切面监控 (Dual-Device Radar)</h3>
            <p class="bento-desc">
              深度适配手机端同城生活圈（抖音实拍探店、大众点评、本地口碑）与 PC 端企业采购（B2B黄页、招投标资质、工商信用），实现全天候立体布控。
            </p>
            <div class="bento-metric-tag">
              <span>监控切面：</span><strong>10 大主流模型双端切面秒级穿透</strong>
            </div>
          </div>

          <!-- Bento 4 -->
          <div class="bento-card">
            <div class="bento-icon-wrap icon-slate">💰</div>
            <h3 class="bento-title">商业潜客损失动态测算引擎</h3>
            <p class="bento-desc">
              拒绝抽象的分数游戏。系统基于目标城市常住人口产业画像、大模型渗透率及行业客单均价，将 AI 搜索盲区直接换算为每月流失的订单与真金白银。
            </p>
            <div class="bento-metric-tag">
              <span>商业透明度：</span><strong>流失客源与投资回报率 (ROI) 透明可验</strong>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. 多行业实测落地实践 (Industry Solutions) -->
    <section class="section solutions-section" id="solutions">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="sec-kicker">INDUSTRY USE CASES</span>
          <h2 class="sec-title">深耕实体经济，赋能高客单核心产业</h2>
          <p class="sec-subtitle">
            无论制造业、大宅家居，还是连锁餐饮与现代专业服务，GEO 均已展现极具说服力的商业增量。
          </p>
        </div>

        <!-- Similarweb 风格极简横向切换 Tab -->
        <div class="industry-tabs-bar">
          <button 
            v-for="(ind, index) in industryCases" 
            :key="ind.id" 
            class="tab-btn" 
            :class="{ active: activeTab === index }"
            @click="activeTab = index"
          >
            {{ ind.name }}
          </button>
        </div>

        <!-- 激活的行业详情卡片 -->
        <div class="industry-showcase-box">
          <div class="showcase-left">
            <div class="showcase-badge">{{ industryCases[activeTab].tag }}</div>
            <h3 class="showcase-title">{{ industryCases[activeTab].headline }}</h3>
            <p class="showcase-text">{{ industryCases[activeTab].summary }}</p>

            <div class="showcase-metrics-row">
              <div class="s-metric">
                <div class="sm-label">优化前行业推荐率</div>
                <div class="sm-val text-red">{{ industryCases[activeTab].preScore }}</div>
              </div>
              <div class="s-metric">
                <div class="sm-label">GEO 优化后推荐率</div>
                <div class="sm-val text-green">{{ industryCases[activeTab].postScore }}</div>
              </div>
              <div class="s-metric">
                <div class="sm-label">月均拦截挽回潜客</div>
                <div class="sm-val text-blue">{{ industryCases[activeTab].savedLeads }}</div>
              </div>
            </div>

            <div class="showcase-cta">
              <router-link to="/console" class="btn-tab-cta">
                体验该行业体检方案 →
              </router-link>
            </div>
          </div>

          <div class="showcase-right">
            <div class="snippet-header">
              <span class="snippet-pill">典型 AI 搜索提问场景</span>
              <span class="snippet-query">“{{ industryCases[activeTab].sampleQuery }}”</span>
            </div>
            <div class="snippet-body">
              <div class="snippet-verdict">
                <strong>💡 行业痛点破局：</strong>
                {{ industryCases[activeTab].solutionPoint }}
              </div>
              <div class="snippet-result">
                <strong>🎯 大模型首推表现：</strong>
                {{ industryCases[activeTab].resultDesc }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. 30 天标准化交付体系 (Roadmap) -->
    <section class="section roadmap-section" id="roadmap">
      <div class="section-inner">
        <div class="section-header-center">
          <span class="sec-kicker">STANDARDIZED DELIVERY BLUEPRINT</span>
          <h2 class="sec-title">30 天企业级标准交付路线图</h2>
          <p class="sec-subtitle">
            标准化工程实施与四阶递进闭环，确保每一步交付成果透明、可查、可复测。
          </p>
        </div>

        <div class="roadmap-timeline">
          <div class="timeline-step" v-for="step in roadmapSteps" :key="step.phase">
            <div class="step-num-bubble">{{ step.phase }}</div>
            <div class="step-days">{{ step.days }}</div>
            <h4 class="step-title">{{ step.title }}</h4>
            <p class="step-action">{{ step.action }}</p>
            <div class="step-deliverable">
              <span class="del-label">交付清单：</span>{{ step.deliverable }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. 商业账本与收尾 CTA (Bottom Banner) -->
    <section class="section cta-section" id="roi">
      <div class="section-inner">
        <div class="cta-banner-card">
          <div class="cta-content">
            <span class="cta-kicker">START YOUR GEO AUDIT TODAY</span>
            <h2 class="cta-headline">准备好让您的品牌在 AI 推荐流中独占鳌头了吗？</h2>
            <p class="cta-desc">
              只需输入企业全称与所属行业，系统即可在 30 秒内穿透 5 大基座大模型，出具包含公域信源溯源、竞品截流深度与商业损失账本的专业体检报告。
            </p>
            <div class="cta-actions">
              <router-link to="/console" class="btn-cta-primary">
                免费启动企业 AI 体检 →
              </router-link>
              <router-link to="/diagnostic_report" class="btn-cta-secondary">
                查阅标杆报告样例
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. 极简国际化企业页脚 (Footer) -->
    <footer class="landing-footer">
      <div class="section-inner footer-inner">
        <div class="footer-top">
          <div class="footer-brand">
            <div class="logo-capsule">
              <img src="/logo-white.png" alt="蜉蝣小宝" class="logo-img" />
            </div>
            <span class="brand-name">蜉蝣小宝 · MAYFLY GEO</span>
            <p class="brand-mission">
              致力于为中国制造业与现代服务业构筑生成式 AI（GEO）时代的品牌认知护城河与公域获客引擎。
            </p>
          </div>

          <div class="footer-nav-groups">
            <div class="footer-col">
              <h5 class="col-title">产品与引擎</h5>
              <router-link to="/console">AI 可见度体检工作台</router-link>
              <router-link to="/ai_report">客户日常优化看板</router-link>
              <router-link to="/diagnostic_report">标杆体检报告样本</router-link>
            </div>

            <div class="footer-col">
              <h5 class="col-title">核心生态穿透</h5>
              <a href="javascript:void(0)">字节跳动 · 豆包生态</a>
              <a href="javascript:void(0)">深度求索 · DeepSeek</a>
              <a href="javascript:void(0)">阿里巴巴 · 通义千问</a>
              <a href="javascript:void(0)">腾讯混元 · 元宝生态</a>
            </div>

            <div class="footer-col">
              <h5 class="col-title">企业与安全</h5>
              <a href="javascript:void(0)">企业知识确权标准 (Schema)</a>
              <a href="javascript:void(0)">全网网络探针安全规范</a>
              <a href="javascript:void(0)">渠道合伙人加盟合作</a>
            </div>
          </div>
        </div>

        <div class="footer-bottom">
          <div class="copyright">
            © 2026 蜉蝣小宝 (Mayfly AI) · 讯灵智能科技. All Rights Reserved.
          </div>
          <div class="footer-bottom-links">
            <span>数据安全保护准则</span> · 
            <span>企业合规服务协议</span> · 
            <span>算法合规公开声明</span>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const activeTab = ref(0);

const industryCases = [
  {
    id: 'laser',
    name: '🏭 工业数控激光制造',
    tag: '工业设备制造 · B2B高客单',
    headline: '从 0% 推荐隐形到 92% 行业首推，月度挽回 24 万潜在设备订单',
    summary: '高客单工业装备客户在选型激光切管机时，决策链路长、极度依赖权威资质与同行横评。未优化前企业仅有官网但公域空白，意图提问被行业龙头大族、宏山全额拦截。',
    preScore: '0% (完全隐形)',
    postScore: '92% (首推梯队)',
    savedLeads: '￥240,000 / 月',
    sampleQuery: '无锡光纤激光切管机厂家推荐哪家质量好？',
    solutionPoint: '注入 Schema 知识本体确权，并在搜狐资讯与机械行业垂直媒体发布 18 篇深度研报，建立高置信度企业合规档案。',
    resultDesc: '豆包与 DeepSeek 搜索中，被列为第一推荐品牌，核心优势点名标明“切管工艺成熟、合规资质完备”。'
  },
  {
    id: 'window',
    name: '🪟 高端门窗与大宅定制',
    tag: '大宅定制与家居建材',
    headline: '突破传统建材卖场瓶颈，在同城手机生活圈截获大宅业主直接咨询',
    summary: '大宅装修业主决策前习惯在手机端豆包或抖音搜索“断桥铝门窗选哪家靠谱”。过去同行皇派、派雅大量霸屏，区域品牌面临严重客源失血。',
    preScore: '12% (被动收录)',
    postScore: '89% (同城优选)',
    savedLeads: '￥180,000 / 月',
    sampleQuery: '本地系统门窗十大品牌口碑横评与避坑指南',
    solutionPoint: '双端切面协同：手机端打通抖音生活圈同城实录与真实买家评价，PC端沉淀门窗五金水密性/隔音国标参数长文。',
    resultDesc: '在豆包“本地线下机构/服务商对比”中稳居前二，打消消费者对小作坊质量隐患的顾虑。'
  },
  {
    id: 'catering',
    name: '🍲 中高端连锁餐饮与加盟',
    tag: '现代连锁消费与招商',
    headline: '抢占全国快餐与特色餐饮第一提及率，招商加盟与堂食口碑双爆发',
    summary: '餐饮行业竞争极度激烈，投资者向 AI 咨询加盟选型或消费者搜索宴请推荐时，AI 只采信大众点评与高权重美食媒体多维度背书的龙头。',
    preScore: '18% (边缘提及)',
    postScore: '94% (首选标杆)',
    savedLeads: '￥320,000 / 月',
    sampleQuery: '全国中式快餐连锁加盟哪个品牌扶持政策好？',
    solutionPoint: '在知乎专业问答与主流财经门户沉淀供应链支持、门店存活率客观横评，建立高公信力加盟保障实体。',
    resultDesc: '通义千问与元宝的商业决策对比矩阵中，被列为标准化成熟度最高的推荐品牌。'
  },
  {
    id: 'medical',
    name: '🦷 专科医疗与数字化齿科',
    tag: '大健康与高净值专科',
    headline: '重塑种植牙与数字化正畸声誉，化解公域负面疑虑，首诊预约提升 150%',
    summary: '医疗健康决策极度审慎，患者在选择机构时必定深挖合规资质、医生资历与价格透明度。公域资产单薄会导致患者直接流向公立或大型连锁。',
    preScore: '8% (信任缺失)',
    postScore: '86% (权威推荐)',
    savedLeads: '￥150,000 / 月',
    sampleQuery: '本地种植牙哪家医院技术靠谱收费透明？',
    solutionPoint: '深度覆盖企查查合规公示、卫健委执业备案引用，并在头条与知乎科普种植牙集采避坑指南。',
    resultDesc: '大模型回答中明确标识“资质合规、收费透明、无隐形增项”，成为患者同城首诊推荐机构。'
  },
  {
    id: 'legal',
    name: '⚖️ 商务咨询与大型律所',
    tag: '高端专业服务与合规',
    headline: '打破传统熟人介绍局限，在大模型企业采购决策流中直获常年法律顾问委托',
    summary: '中大型企业在遇到商事诉讼或常法选型时，法务与总经理常直接用 AI 快速检索律所胜诉率与团队背景。缺乏深度案例背书将被金杜、大成无情截流。',
    preScore: '5% (无实体背书)',
    postScore: '91% (专家首选)',
    savedLeads: '￥210,000 / 月',
    sampleQuery: '企业常年法律顾问与商事纠纷解决律所哪家专业？',
    solutionPoint: '定向发布行业重大商事案例研报，建立包含胜诉率、专业委员会任职的高权重权威知识词条。',
    resultDesc: '通义千问 B2B 评测中，以“商事争议解决专业度与高响应机制”被重点推介给企业决策层。'
  }
];

const roadmapSteps = [
  {
    phase: '01',
    days: 'Day 1 - Day 7',
    title: '品牌专有词确权与知识图谱 Schema 结构化注入',
    action: '建立专属企业本体实体，完成百度百科词条认证及 Schema.org 结构化元数据标记，建立大模型 RAG 召回根基。',
    deliverable: '《企业知识本体架构书》、官方百科词条过审上线、Schema 实体标签认证'
  },
  {
    phase: '02',
    days: 'Day 8 - Day 15',
    title: '主流高权重权威信源公信力矩阵定向投喂',
    action: '针对 DeepSeek、豆包、通义千问优先采信的新浪、搜狐、网易、知乎等核心门户，定向发布 15~20 篇深度专业测评研报与真实案例。',
    deliverable: '国家级/行业高权重媒体发稿收录链接清单、外链索引报告、第三方权威评测背书'
  },
  {
    phase: '03',
    days: 'Day 16 - Day 22',
    title: '行业高频采购意向词与长尾对比词精准拦截',
    action: '围绕“哪家好”、“口碑推荐”、“选型对比”等 50+ 个高频采购问答场景构建标准化 QA 意图问答库，抢占第一推荐位。',
    deliverable: '《行业采购意向拦截词库》、长尾多轮问答意图覆盖表、竞品对比优势反制策略库'
  },
  {
    phase: '04',
    days: 'Day 23 - Day 30',
    title: '双端多平台自动化复测、终审交付与长期雷达开通',
    action: '对豆包、DeepSeek、千问、元宝等 10 大双端切面执行全量自动化巡检，出具终审成果报表，并开通全天候防御大屏。',
    deliverable: '《GEO 优化终审成果报表》、开通【蜉蝣小宝 · 交付期实时数据监控看板】账号权限'
  }
];
</script>

<style scoped>
/* ================= 全局与容器 ================= */
.landing-container {
  min-height: 100vh;
  background-color: #ffffff;
  color: #0f172a;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  overflow-x: hidden;
}

.section-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section {
  padding: 5.5rem 0;
}

/* ================= 1. 顶栏 (Header) ================= */
.landing-header {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, 0.88);
  border-bottom: 1px solid rgba(226, 232, 240, 0.8);
  transition: all 0.2s ease;
}

.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0.85rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}

.logo-capsule {
  width: 36px;
  height: 36px;
  background: #0f172a;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(15, 23, 42, 0.15);
}

.logo-img {
  height: 22px;
  width: auto;
  object-fit: contain;
}

.brand-text-wrap {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-size: 1.05rem;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.02em;
}

.brand-en {
  font-size: 0.65rem;
  font-weight: 700;
  color: #2563eb;
  letter-spacing: 0.08em;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-item {
  color: #475569;
  font-size: 0.92rem;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.15s ease;
}

.nav-item:hover {
  color: #2563eb;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.btn-ghost-nav {
  color: #475569;
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  padding: 0.45rem 0.9rem;
  border-radius: 6px;
  transition: all 0.15s ease;
}

.btn-ghost-nav:hover {
  color: #0f172a;
  background: #f1f5f9;
}

.btn-primary-nav {
  background: #2563eb;
  color: #ffffff;
  font-size: 0.88rem;
  font-weight: 600;
  text-decoration: none;
  padding: 0.5rem 1.15rem;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 0.35rem;
  box-shadow: 0 1px 3px rgba(37, 99, 235, 0.25);
  transition: all 0.2s ease;
}

.btn-primary-nav:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(37, 99, 235, 0.35);
}

/* ================= 2. 品牌首屏 (Hero Section) ================= */
.hero-section {
  position: relative;
  padding: 4.5rem 0 5rem;
  background: radial-gradient(ellipse 90% 60% at 50% -10%, rgba(37, 99, 235, 0.07), transparent 75%);
  overflow: hidden;
}

.hero-inner {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.hero-pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  padding: 0.3rem 0.85rem;
  border-radius: 999px;
  margin-bottom: 1.5rem;
}

.badge-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #2563eb;
}

.badge-text {
  font-size: 0.82rem;
  font-weight: 600;
  color: #1d4ed8;
}

.hero-headline {
  font-size: 3.4rem;
  font-weight: 850;
  color: #0f172a;
  letter-spacing: -0.03em;
  line-height: 1.2;
  margin-bottom: 1.25rem;
}

.text-gradient {
  background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 50%, #0284c7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtext {
  font-size: 1.15rem;
  color: #475569;
  max-width: 760px;
  margin: 0 auto 2.25rem;
  line-height: 1.7;
}

.hero-cta-group {
  display: flex;
  align-items: center;
  gap: 1.15rem;
  margin-bottom: 3.5rem;
}

.btn-hero-primary {
  background: #2563eb;
  color: #ffffff;
  font-size: 1.05rem;
  font-weight: 600;
  padding: 0.85rem 2rem;
  border-radius: 8px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
  transition: all 0.2s ease;
}

.btn-hero-primary:hover {
  background: #1d4ed8;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4);
}

.btn-hero-secondary {
  background: #ffffff;
  color: #334155;
  font-size: 1.05rem;
  font-weight: 600;
  padding: 0.85rem 1.85rem;
  border-radius: 8px;
  text-decoration: none;
  border: 1px solid #cbd5e1;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}

.btn-hero-secondary:hover {
  background: #f8fafc;
  border-color: #94a3b8;
  color: #0f172a;
}

/* 首屏静质感 UI 预览画报 (Similarweb 风格) */
.hero-mockup-frame {
  width: 100%;
  max-width: 1080px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  box-shadow: 0 20px 45px -15px rgba(15, 23, 42, 0.12), 0 0 0 1px rgba(15, 23, 42, 0.03);
  overflow: hidden;
  text-align: left;
}

.mockup-header-bar {
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  padding: 0.75rem 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.mockup-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.dot-red { background: #f87171; }
.dot-amber { background: #fbbf24; }
.dot-green { background: #34d399; }

.mockup-search-sim {
  flex: 1;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 0.35rem 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
}

.sim-query {
  color: #1e293b;
  font-weight: 500;
}

.mockup-status-tag {
  font-size: 0.78rem;
  color: #059669;
  font-weight: 600;
  background: #ecfdf5;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
}

.mockup-body-content {
  display: grid;
  grid-template-columns: 1.55fr 1fr;
  background: #ffffff;
}

.mockup-response-panel {
  padding: 1.5rem;
  border-right: 1px solid #f1f5f9;
}

.panel-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid #f1f5f9;
}

.ai-avatar {
  font-size: 1.4rem;
}

.ai-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #0f172a;
}

.ai-sub {
  font-size: 0.75rem;
  color: #64748b;
}

.ai-quote-lead {
  font-size: 0.88rem;
  color: #475569;
  margin-bottom: 0.85rem;
}

.ai-recommend-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
}

.target-highlight {
  background: #eff6ff;
  border-color: #bfdbfe;
}

.rec-badge {
  font-size: 0.75rem;
  font-weight: 700;
  color: #1d4ed8;
  margin-bottom: 0.35rem;
}

.rec-title {
  font-size: 0.95rem;
  font-weight: 750;
  color: #0f172a;
  margin-bottom: 0.4rem;
}

.rec-desc {
  font-size: 0.82rem;
  color: #334155;
  line-height: 1.5;
  margin-bottom: 0.75rem;
}

.rec-tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.rtag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}
.tag-green { background: #dcfce7; color: #15803d; }
.tag-blue { background: #dbeafe; color: #1d4ed8; }
.tag-indigo { background: #e0e7ff; color: #4338ca; }

.ai-competitor-faded {
  font-size: 0.82rem;
  color: #64748b;
  padding: 0.5rem;
}

.comp-name {
  font-weight: 600;
  color: #475569;
}

.mockup-telemetry-panel {
  padding: 1.5rem;
  background: #fafafa;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.telemetry-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 0.85rem;
}

.t-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #64748b;
  margin-bottom: 0.25rem;
}

.t-val-wrap {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
}

.t-val {
  font-size: 1.6rem;
  font-weight: 800;
  line-height: 1.1;
}
.text-green { color: #059669; }
.text-blue { color: #2563eb; }
.text-slate { color: #0f172a; }

.t-unit {
  font-size: 0.8rem;
  font-weight: 600;
  color: #64748b;
}

.t-tag-growth {
  font-size: 0.75rem;
  font-weight: 700;
  color: #059669;
  background: #dcfce7;
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
}

.t-bar-wrap {
  height: 6px;
  background: #e2e8f0;
  border-radius: 999px;
  margin-top: 0.6rem;
  overflow: hidden;
}

.t-bar-fill {
  height: 100%;
  background: #059669;
  border-radius: 999px;
}

.t-sub {
  font-size: 0.72rem;
  color: #64748b;
  margin-top: 0.35rem;
}

.telemetry-model-chips {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
  margin-top: auto;
}

.m-chip {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.4rem 0.5rem;
  border-radius: 6px;
  text-align: center;
  background: #f1f5f9;
  color: #334155;
}

.chip-on {
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  color: #065f46;
}

/* ================= 3. 大模型生态跑马区 ================= */
.ecosystem-strip {
  padding: 2.25rem 0;
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #e2e8f0;
  text-align: center;
}

.ecosystem-title {
  font-size: 0.82rem;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1.25rem;
}

.ecosystem-logos {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  flex-wrap: wrap;
}

.logo-item {
  font-size: 0.88rem;
  font-weight: 650;
  color: #334155;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.logo-circle {
  width: 24px;
  height: 24px;
  border-radius: 6px;
  background: #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 800;
  color: #0f172a;
}

/* ================= 4. 范式对比区 (The Shift) ================= */
.section-header-center {
  text-align: center;
  max-width: 780px;
  margin: 0 auto 3.5rem;
}

.sec-kicker {
  font-size: 0.78rem;
  font-weight: 750;
  color: #2563eb;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  display: block;
  margin-bottom: 0.5rem;
}

.sec-title {
  font-size: 2.25rem;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.02em;
  margin-bottom: 0.85rem;
}

.sec-subtitle {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.6;
}

.shift-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.shift-card {
  border-radius: 12px;
  padding: 2.25rem;
  transition: all 0.2s ease;
}

.card-old {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.card-new {
  background: #ffffff;
  border: 2px solid #2563eb;
  box-shadow: 0 15px 35px -10px rgba(37, 99, 235, 0.12);
}

.card-status-badge {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.badge-faded {
  background: #e2e8f0;
  color: #64748b;
}

.badge-active {
  background: #dbeafe;
  color: #1d4ed8;
}

.shift-card-title {
  font-size: 1.35rem;
  font-weight: 750;
  color: #0f172a;
  margin-bottom: 1.5rem;
}

.shift-points {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1.15rem;
}

.shift-points li {
  display: flex;
  gap: 0.85rem;
}

.point-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 800;
  flex-shrink: 0;
}

.point-icon.red { background: #fee2e2; color: #b91c1c; }
.point-icon.green { background: #dcfce7; color: #15803d; }

.point-desc {
  font-size: 0.92rem;
  color: #334155;
  line-height: 1.5;
}

/* ================= 5. 核心能力 (Bento Grid) ================= */
.features-section {
  background: #f8fafc;
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.bento-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
}

.bento-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 25px -10px rgba(0, 0, 0, 0.08);
  border-color: #cbd5e1;
}

.bento-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  margin-bottom: 1.25rem;
}

.icon-blue { background: #eff6ff; }
.icon-green { background: #ecfdf5; }
.icon-indigo { background: #eef2ff; }
.icon-slate { background: #f1f5f9; }

.bento-title {
  font-size: 1.25rem;
  font-weight: 750;
  color: #0f172a;
  margin-bottom: 0.75rem;
}

.bento-desc {
  font-size: 0.92rem;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  flex: 1;
}

.bento-metric-tag {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 0.5rem 0.85rem;
  border-radius: 6px;
  font-size: 0.82rem;
  color: #334155;
}

.bento-metric-tag strong {
  color: #1d4ed8;
}

/* ================= 6. 行业解决方案 (Solutions) ================= */
.industry-tabs-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  margin-bottom: 2.25rem;
  flex-wrap: wrap;
}

.tab-btn {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  color: #475569;
  font-size: 0.92rem;
  font-weight: 600;
  padding: 0.6rem 1.25rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.tab-btn:hover {
  background: #f1f5f9;
  color: #0f172a;
}

.tab-btn.active {
  background: #0f172a;
  border-color: #0f172a;
  color: #ffffff;
  box-shadow: 0 4px 10px rgba(15, 23, 42, 0.2);
}

.industry-showcase-box {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  padding: 2.5rem;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 2.5rem;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
}

.showcase-badge {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 700;
  color: #2563eb;
  background: #eff6ff;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
  margin-bottom: 0.85rem;
}

.showcase-title {
  font-size: 1.55rem;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.35;
  margin-bottom: 0.85rem;
}

.showcase-text {
  font-size: 0.95rem;
  color: #475569;
  line-height: 1.65;
  margin-bottom: 1.75rem;
}

.showcase-metrics-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1.75rem;
}

.sm-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #64748b;
  margin-bottom: 0.25rem;
}

.sm-val {
  font-size: 1.15rem;
  font-weight: 800;
}
.text-red { color: #dc2626; }

.btn-tab-cta {
  background: #2563eb;
  color: #ffffff;
  font-size: 0.92rem;
  font-weight: 600;
  text-decoration: none;
  padding: 0.65rem 1.4rem;
  border-radius: 6px;
  display: inline-block;
  transition: all 0.2s ease;
}

.btn-tab-cta:hover {
  background: #1d4ed8;
}

.showcase-right {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.snippet-header {
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 1rem;
}

.snippet-pill {
  font-size: 0.72rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  display: block;
  margin-bottom: 0.35rem;
}

.snippet-query {
  font-size: 0.95rem;
  font-weight: 750;
  color: #0f172a;
}

.snippet-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  font-size: 0.88rem;
  color: #334155;
  line-height: 1.55;
}

/* ================= 7. 30 天交付蓝图 ================= */
.roadmap-section {
  background: #f8fafc;
}

.roadmap-timeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.timeline-step {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  position: relative;
}

.step-num-bubble {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: #0f172a;
  color: #ffffff;
  font-size: 0.88rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.75rem;
}

.step-days {
  font-size: 0.78rem;
  font-weight: 700;
  color: #2563eb;
  margin-bottom: 0.5rem;
}

.step-title {
  font-size: 1.05rem;
  font-weight: 750;
  color: #0f172a;
  margin-bottom: 0.75rem;
  line-height: 1.35;
}

.step-action {
  font-size: 0.85rem;
  color: #475569;
  line-height: 1.55;
  margin-bottom: 1.25rem;
  flex: 1;
}

.step-deliverable {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  color: #334155;
  line-height: 1.45;
}

.del-label {
  font-weight: 700;
  color: #0f172a;
}

/* ================= 8. 商业账本与收尾 CTA ================= */
.cta-banner-card {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  border-radius: 16px;
  padding: 4.5rem 2.5rem;
  color: #ffffff;
  text-align: center;
  box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.25);
}

.cta-content {
  max-width: 780px;
  margin: 0 auto;
}

.cta-kicker {
  font-size: 0.78rem;
  font-weight: 750;
  color: #60a5fa;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  display: block;
  margin-bottom: 0.75rem;
}

.cta-headline {
  font-size: 2.35rem;
  font-weight: 850;
  line-height: 1.25;
  margin-bottom: 1rem;
}

.cta-desc {
  font-size: 1.05rem;
  color: #94a3b8;
  line-height: 1.65;
  margin-bottom: 2.25rem;
}

.cta-actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
}

.btn-cta-primary {
  background: #2563eb;
  color: #ffffff;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  padding: 0.85rem 2rem;
  border-radius: 8px;
  transition: all 0.2s ease;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
}

.btn-cta-primary:hover {
  background: #1d4ed8;
  transform: translateY(-2px);
}

.btn-cta-secondary {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  padding: 0.85rem 1.85rem;
  border-radius: 8px;
  transition: all 0.2s ease;
}

.btn-cta-secondary:hover {
  background: rgba(255, 255, 255, 0.18);
}

/* ================= 9. 页脚 (Footer) ================= */
.landing-footer {
  background: #ffffff;
  border-top: 1px solid #e2e8f0;
  padding: 4.5rem 0 2.5rem;
}

.footer-top {
  display: grid;
  grid-template-columns: 1.5fr 2fr;
  gap: 3.5rem;
  margin-bottom: 3.5rem;
}

.footer-brand .logo-capsule {
  margin-bottom: 0.85rem;
}

.footer-brand .brand-name {
  font-size: 1.15rem;
  font-weight: 800;
  color: #0f172a;
  display: block;
  margin-bottom: 0.65rem;
}

.brand-mission {
  font-size: 0.88rem;
  color: #64748b;
  max-width: 380px;
  line-height: 1.6;
}

.footer-nav-groups {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.col-title {
  font-size: 0.88rem;
  font-weight: 750;
  color: #0f172a;
  margin-bottom: 1.15rem;
}

.footer-col a {
  display: block;
  font-size: 0.85rem;
  color: #64748b;
  text-decoration: none;
  margin-bottom: 0.75rem;
  transition: color 0.15s ease;
}

.footer-col a:hover {
  color: #2563eb;
}

.footer-bottom {
  border-top: 1px solid #f1f5f9;
  padding-top: 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.82rem;
  color: #94a3b8;
  flex-wrap: wrap;
  gap: 1rem;
}

/* ================= 响应式适配 ================= */
@media (max-width: 1024px) {
  .hero-headline { font-size: 2.6rem; }
  .mockup-body-content { grid-template-columns: 1fr; }
  .shift-grid { grid-template-columns: 1fr; }
  .bento-grid { grid-template-columns: 1fr; }
  .industry-showcase-box { grid-template-columns: 1fr; }
  .roadmap-timeline { grid-template-columns: 1fr 1fr; }
  .footer-top { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  .nav-links { display: none; }
  .hero-headline { font-size: 2.1rem; }
  .hero-cta-group { flex-direction: column; width: 100%; }
  .btn-hero-primary, .btn-hero-secondary { width: 100%; justify-content: center; }
  .roadmap-timeline { grid-template-columns: 1fr; }
  .showcase-metrics-row { grid-template-columns: 1fr; }
  .footer-nav-groups { grid-template-columns: 1fr; }
}
</style>
