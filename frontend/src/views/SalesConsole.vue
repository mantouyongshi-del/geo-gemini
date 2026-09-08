<template>
  <div class="sales-console-wrapper">
    <!-- 顶部导航条 -->
    <header class="console-nav-header">
      <div class="nav-container">
        <div class="brand-group">
          <div class="brand-logo-wrap">
            <img src="/logo-white.png" alt="蜉蝣小宝" class="console-logo" />
          </div>
          <div class="brand-badge-col">
            <div class="brand-title-row">
              <span class="brand-sub-title">GEO SALES CLOUD</span>
              <span class="system-version-pill">v2.6 商务实测工作台</span>
            </div>
            <div class="system-status-indicator">
              <span class="status-dot-pulse"></span>
              <span class="status-label">官方五大基座大模型实时探针在线 (PC/移动全域穿透)</span>
            </div>
          </div>
        </div>

        <div class="nav-right-actions">
          <!-- 销售顾问身份展示 -->
          <div class="consultant-pill" @click="openConsultantModal">
            <svg class="pill-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <div class="consultant-info-text">
              <span class="c-name">{{ form.consultant_name || '数字化顾问' }}</span>
              <span class="c-agency">{{ form.agency_name || '服务中心' }}</span>
            </div>
            <svg class="pill-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </div>
        </div>
      </div>
    </header>

    <!-- 工作台主功能选项卡 -->
    <nav class="console-sub-bar">
      <div class="sub-bar-inner">
        <div class="tab-btn-group">
          <button 
            type="button" 
            class="console-tab-btn" 
            :class="{ active: currentTab === 'diagnostic' }"
            @click="switchTab('diagnostic')"
          >
            <svg class="tab-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <path d="m4.93 4.93 4.24 4.24"></path>
              <path d="m14.83 9.17 4.24-4.24"></path>
              <path d="m14.83 14.83 4.24 4.24"></path>
              <path d="m9.17 14.83-4.24 4.24"></path>
              <circle cx="12" cy="12" r="2"></circle>
            </svg>
            <span>准客户 AI 可见度现场实测</span>
          </button>

          <button 
            type="button" 
            class="console-tab-btn" 
            :class="{ active: currentTab === 'leads' }"
            @click="switchTab('leads')"
          >
            <svg class="tab-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
              <circle cx="9" cy="7" r="4"></circle>
              <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
            </svg>
            <span>官网预约线索池</span>
            <span class="tab-count-badge" v-if="leadsList.length">{{ leadsList.length }}</span>
          </button>

          <button 
            type="button" 
            class="console-tab-btn" 
            :class="{ active: currentTab === 'archive' }"
            @click="switchTab('archive')"
          >
            <svg class="tab-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="2" y="3" width="20" height="5" rx="1"></rect>
              <path d="M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8"></path>
              <path d="M10 12h4"></path>
            </svg>
            <span>历史体检报告归档</span>
            <span class="tab-count-badge subtle" v-if="recentHistory.length">{{ recentHistory.length }}</span>
          </button>
        </div>

        <div class="sub-bar-quick">
          <span class="quick-status-chip">
            <svg class="chip-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
            </svg>
            真机探针延迟: 1.2s · 穿透率 100%
          </span>
        </div>
      </div>
    </nav>

    <!-- 工作台主体内容 -->
    <main class="console-body">
      <!-- TAB 1: 准客户现场实测 -->
      <section v-show="currentTab === 'diagnostic'" class="tab-content-panel">
        <!-- 官方大模型五大矩阵徽章墙 (无 Emoji，纯矢量现代工业感) -->
        <div class="models-matrix-grid">
          <div class="model-engine-card doubao">
            <div class="engine-header">
              <div class="engine-icon-wrap">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                </svg>
              </div>
              <div class="engine-names">
                <span class="engine-brand">字节跳动 · 豆包</span>
                <span class="engine-tag">火山引擎方舟生态</span>
              </div>
            </div>
            <div class="engine-desc">抖音生活圈公域与移动端原生搜索第一入口</div>
            <div class="engine-status-row">
              <span class="engine-dot-active"></span>
              <span class="engine-status-text">已连通 120ms</span>
            </div>
          </div>

          <div class="model-engine-card deepseek">
            <div class="engine-header">
              <div class="engine-icon-wrap">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                  <rect x="9" y="9" width="6" height="6"></rect>
                  <line x1="9" y1="1" x2="9" y2="4"></line>
                  <line x1="15" y1="1" x2="15" y2="4"></line>
                  <line x1="9" y1="20" x2="9" y2="23"></line>
                  <line x1="15" y1="20" x2="15" y2="23"></line>
                  <line x1="20" y1="9" x2="23" y2="9"></line>
                  <line x1="20" y1="14" x2="23" y2="14"></line>
                  <line x1="1" y1="9" x2="4" y2="9"></line>
                  <line x1="1" y1="14" x2="4" y2="14"></line>
                </svg>
              </div>
              <div class="engine-names">
                <span class="engine-brand">深度求索 · DeepSeek</span>
                <span class="engine-tag">官方开放平台直连</span>
              </div>
            </div>
            <div class="engine-desc">全网公信力深度推理链与权威背书召回</div>
            <div class="engine-status-row">
              <span class="engine-dot-active"></span>
              <span class="engine-status-text">已连通 340ms</span>
            </div>
          </div>

          <div class="model-engine-card tongyi">
            <div class="engine-header">
              <div class="engine-icon-wrap">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
              </div>
              <div class="engine-names">
                <span class="engine-brand">阿里巴巴 · 通义千问</span>
                <span class="engine-tag">阿里云百炼全网引擎</span>
              </div>
            </div>
            <div class="engine-desc">B2B 企业级采购、供应链决策与商机撮合核心</div>
            <div class="engine-status-row">
              <span class="engine-dot-active"></span>
              <span class="engine-status-text">已连通 180ms</span>
            </div>
          </div>

          <div class="model-engine-card yuanbao">
            <div class="engine-header">
              <div class="engine-icon-wrap">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                </svg>
              </div>
              <div class="engine-names">
                <span class="engine-brand">腾讯科技 · 腾讯元宝</span>
                <span class="engine-tag">腾讯混元内核架构</span>
              </div>
            </div>
            <div class="engine-desc">微信公众号、搜一搜与微信朋友圈生态渗透</div>
            <div class="engine-status-row">
              <span class="engine-dot-active"></span>
              <span class="engine-status-text">已连通 210ms</span>
            </div>
          </div>

          <div class="model-engine-card baidu">
            <div class="engine-header">
              <div class="engine-icon-wrap">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
              </div>
              <div class="engine-names">
                <span class="engine-brand">百度智能 · 百度搜索</span>
                <span class="engine-tag">知识图谱词条矩阵</span>
              </div>
            </div>
            <div class="engine-desc">国内传统搜索引擎转型 AI 搜索首批权威信源收录</div>
            <div class="engine-status-row">
              <span class="engine-dot-active"></span>
              <span class="engine-status-text">已连通 150ms</span>
            </div>
          </div>
        </div>

        <div class="diagnostic-grid-layout">
          <!-- 左侧：输入表单与实测触发区 -->
          <div class="console-card form-box-card">
            <div class="card-header-flex">
              <div class="card-title-wrap">
                <h2 class="card-main-title">录入准客户实测参数</h2>
                <p class="card-sub-title">用于现场针对目标企业开展 5 大基座大模型实时真机穿透与竞品截流测评</p>
              </div>
              <button type="button" class="btn-clear-form" @click="resetForm">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path>
                  <path d="M3 3v5h5"></path>
                </svg>
                重置表单
              </button>
            </div>

            <!-- 行业案例快速填入 Pills -->
            <div class="industry-presets-bar">
              <span class="preset-label">现场实测模版快速带入:</span>
              <div class="preset-pill-group">
                <button 
                  type="button"
                  v-for="tpl in industryTemplates" 
                  :key="tpl.name" 
                  class="preset-chip"
                  @click="applyTemplate(tpl)"
                >
                  <span class="chip-name">{{ tpl.name }}</span>
                </button>
              </div>
            </div>

            <form @submit.prevent="handleStartDiagnostic" class="diagnostic-form">
              <div class="form-item">
                <label class="form-label">
                  <span>目标准客户工商全称</span>
                  <span class="badge-required">必填</span>
                </label>
                <div class="input-with-icon">
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="9" y1="3" x2="9" y2="21"></line>
                  </svg>
                  <input 
                    v-model="form.target_company" 
                    required 
                    placeholder="例如: 无锡恒瑞智能装备科技有限公司 / 佛山尚品佳豪智能家居系统有限公司" 
                    class="form-control" 
                  />
                </div>
              </div>

              <div class="form-row-three">
                <div class="form-item">
                  <label class="form-label">
                    <span>品牌简称 / 常用名</span>
                    <span class="badge-required">必填</span>
                  </label>
                  <input 
                    v-model="form.brand_name" 
                    required 
                    placeholder="例如: 恒瑞智能 / 佳豪门窗" 
                    class="form-control" 
                  />
                </div>

                <div class="form-item">
                  <label class="form-label">
                    <span>所属行业细分领域</span>
                    <span class="badge-required">必填</span>
                  </label>
                  <input 
                    v-model="form.industry" 
                    required 
                    placeholder="例如: 数控激光切管机 / 高端系统门窗" 
                    class="form-control" 
                  />
                </div>

                <div class="form-item">
                  <label class="form-label">
                    <span>展业核心城市 / 区域</span>
                  </label>
                  <input 
                    v-model="form.city" 
                    placeholder="例如: 无锡 / 佛山 / 全国" 
                    class="form-control" 
                  />
                </div>
              </div>

              <!-- 关键词输入与 AI 截流词生成 -->
              <div class="form-item">
                <div class="label-action-row">
                  <label class="form-label">
                    <span>实测截流关键词 (每行一条测试意图，支持 1~5 组)</span>
                    <span class="badge-required">必填</span>
                  </label>
                  <button 
                    type="button" 
                    class="btn-smart-keywords"
                    :disabled="isGeneratingKws"
                    @click="generateSmartKeywords"
                  >
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path>
                    </svg>
                    <span>{{ isGeneratingKws ? '正在根据 GEO 决策意图模型生成...' : '基于 GEO 意图模型一键生成高频词' }}</span>
                  </button>
                </div>
                <textarea 
                  v-model="keywordsStr" 
                  rows="4" 
                  required
                  placeholder="例如:&#10;无锡激光切管机生产厂家推荐哪家性价比高&#10;数控光纤激光切割机十大知名品牌实力排名&#10;工业激光切割设备采购避坑选型指南与真实评测"
                  class="form-textarea"
                ></textarea>
                <div class="form-hint-text">
                  提示：实测词应贴合 B 端或 C 端终端决策者在 AI 搜索中的真实自然语言提问习惯（含「哪家好」、「品牌排名」、「避坑指南」等金三角词型）。
                </div>
              </div>

              <!-- 提交按钮 -->
              <div class="form-submit-row">
                <button 
                  type="submit" 
                  class="btn-submit-diagnostic"
                  :disabled="isRunning"
                >
                  <svg class="submit-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                  </svg>
                  <span class="submit-text">启动 5 大基座大模型现场穿透探测 · 现场出具诊断书</span>
                </button>
              </div>
            </form>
          </div>

          <!-- 右侧：顾问工作指引与实操说明 -->
          <div class="console-sidebar-col">
            <!-- 顾问认证卡片 -->
            <div class="console-card consultant-card">
              <div class="c-card-top">
                <div class="c-avatar-wrap">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                  </svg>
                </div>
                <div class="c-detail">
                  <div class="c-name-row">
                    <span class="c-main-name">{{ form.consultant_name }}</span>
                    <span class="c-tag-badge">认证顾问</span>
                  </div>
                  <div class="c-sub">{{ form.agency_name }}</div>
                  <div class="c-tel">联系电话: {{ form.consultant_phone }}</div>
                </div>
              </div>
              <div class="c-card-actions">
                <button type="button" class="btn-config-c" @click="openConsultantModal">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                  </svg>
                  修改顾问署名与服务中心
                </button>
              </div>
            </div>

            <!-- 售前促单战术要点 (折叠式) -->
            <div class="console-card tactics-card">
              <div class="tactics-header">
                <div class="tactics-title-wrap">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                  </svg>
                  <span>售前攻防促单黄金策略</span>
                </div>
              </div>
              <div class="tactics-body">
                <div class="tactic-item">
                  <span class="t-badge">Step 1</span>
                  <div class="t-text">
                    <strong>铁证事实呈现：</strong> 
                    实测完成后第一时间带客户查看「同行实体霸屏」与「未提及/被截流」标注，让老板亲眼看到潜在客户正被谁抢走。
                  </div>
                </div>
                <div class="tactic-item">
                  <span class="t-badge">Step 2</span>
                  <div class="t-text">
                    <strong>穿透经济账流失模型：</strong> 
                    指引客户查看诊断书第四节的商业经济测算，说明企业每年在传统获客上花大钱，却在 AI 搜索端无形流失了数十万商机。
                  </div>
                </div>
                <div class="tactic-item">
                  <span class="t-badge">Step 3</span>
                  <div class="t-text">
                    <strong>一键生成微信分享链接：</strong> 
                    实测报告支持一键复制永久链接，直接发送给目标企业决策人微信，方便在企业高层内部快速传阅推动立项。
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- TAB 2: 官网预约线索池 -->
      <section v-show="currentTab === 'leads'" class="tab-content-panel">
        <div class="console-card leads-card">
          <div class="leads-header-row">
            <div class="leads-title-col">
              <h2 class="leads-title">官网访客 1v1 预约线索池</h2>
              <p class="leads-sub">
                公网访客在品牌官网提交的企业预约信息自动同步至此。点击「一键带入现场实测」即可直接调用 5 大基座大模型开展实测出单！
              </p>
            </div>
            <div class="leads-action-btns">
              <button type="button" class="btn-secondary" @click="refreshLeads">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="23 4 23 10 17 10"></polyline>
                  <polyline points="1 20 1 14 7 14"></polyline>
                  <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                </svg>
                刷新线索
              </button>
              <button type="button" class="btn-secondary" @click="mockAddLead">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
                模拟添加意向线索
              </button>
              <button 
                type="button" 
                class="btn-danger-outline" 
                :disabled="!leadsList.length"
                @click="clearAllLeads"
              >
                清空线索
              </button>
            </div>
          </div>

          <!-- 线索表格 -->
          <div class="leads-table-wrap" v-if="leadsList.length">
            <table class="leads-table">
              <thead>
                <tr>
                  <th>工单编号</th>
                  <th>准客户企业 / 品牌</th>
                  <th>所属行业领域</th>
                  <th>联系人姓名 / 职务</th>
                  <th>联系电话</th>
                  <th>意向演示类型</th>
                  <th>来源渠道</th>
                  <th>提交时间</th>
                  <th class="text-right">操作</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="lead in leadsList" :key="lead.id">
                  <td>
                    <span class="ticket-code">{{ lead.ticketId }}</span>
                  </td>
                  <td>
                    <div class="lead-brand-cell">
                      <span class="brand-text">{{ lead.brand }}</span>
                    </div>
                  </td>
                  <td>
                    <span class="industry-tag">{{ lead.industry || '未指定' }}</span>
                  </td>
                  <td>
                    <span class="contact-name">{{ lead.contact }}</span>
                  </td>
                  <td>
                    <span class="phone-num">{{ lead.phone }}</span>
                  </td>
                  <td>
                    <span class="demo-type-pill">{{ lead.demoType || '全域可见度' }}</span>
                  </td>
                  <td>
                    <span class="source-chip">{{ lead.source || '官网主动预约' }}</span>
                  </td>
                  <td>
                    <span class="time-text">{{ lead.createdAt }}</span>
                  </td>
                  <td class="text-right action-cells">
                    <button 
                      type="button" 
                      class="btn-lead-test"
                      @click="importLeadToDiagnostic(lead)"
                      title="将企业信息带入体检表单并启动实测"
                    >
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polygon points="5 3 19 12 5 21 5 3"></polygon>
                      </svg>
                      一键带入现场实测
                    </button>
                    <button 
                      type="button" 
                      class="btn-lead-copy" 
                      @click="copyPhone(lead.phone)"
                    >
                      {{ copiedPhone === lead.phone ? '已复制' : '复制电话' }}
                    </button>
                    <button 
                      type="button" 
                      class="btn-lead-del" 
                      @click="deleteLead(lead.id)"
                      title="删除该线索"
                    >
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="3 6 5 6 21 6"></polyline>
                        <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                      </svg>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 无线索空状态 -->
          <div class="empty-leads-state" v-else>
            <div class="empty-icon-wrap">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
              </svg>
            </div>
            <h3 class="empty-title">暂无新增官网预约线索</h3>
            <p class="empty-desc">
              当公网用户在品牌官网浏览并点击「预约 1v1 方案演示」弹窗提交表单后，数据将在此秒级同步展现。
            </p>
            <button type="button" class="btn-secondary" @click="mockAddLead">
              立即模拟生成一条官网预约线索
            </button>
          </div>
        </div>
      </section>

      <!-- TAB 3: 历史报告归档库 -->
      <section v-show="currentTab === 'archive'" class="tab-content-panel">
        <div class="console-card archive-card">
          <div class="archive-header-row">
            <div class="archive-title-col">
              <h2 class="archive-title">企业 AI 可见度体检报告历史归档</h2>
              <p class="archive-sub">
                记录销售团队已出具的准客户体检单。支持直接重新打开诊断体检书、复制永久分享链接向客户微信汇报。
              </p>
            </div>
            <div class="archive-actions">
              <button 
                type="button" 
                class="btn-secondary" 
                @click="loadHistory"
              >
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="23 4 23 10 17 10"></polyline>
                  <polyline points="1 20 1 14 7 14"></polyline>
                  <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                </svg>
                刷新列表
              </button>
              <button 
                type="button" 
                class="btn-danger-outline" 
                :disabled="!recentHistory.length"
                @click="handleClearHistory"
              >
                清空归档
              </button>
            </div>
          </div>

          <!-- 报告列表 -->
          <div class="archive-table-wrap" v-if="recentHistory.length">
            <table class="archive-table">
              <thead>
                <tr>
                  <th>报告单号</th>
                  <th>体检准客户工商全称</th>
                  <th>品牌简称</th>
                  <th>所属行业</th>
                  <th>展业城市</th>
                  <th>生成时间</th>
                  <th class="text-right">操作</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in recentHistory" :key="item.report_code">
                  <td>
                    <span class="report-code-badge">{{ item.report_code }}</span>
                  </td>
                  <td>
                    <span class="company-name-bold">{{ item.target_company }}</span>
                  </td>
                  <td>
                    <span class="brand-tag-simple">{{ item.brand_name }}</span>
                  </td>
                  <td>
                    <span class="industry-text">{{ item.industry }}</span>
                  </td>
                  <td>
                    <span class="city-text">{{ item.city || '全国' }}</span>
                  </td>
                  <td>
                    <span class="time-text">{{ formatTimestamp(item.created_at) }}</span>
                  </td>
                  <td class="text-right action-cells">
                    <button 
                      type="button" 
                      class="btn-open-report"
                      @click="openReport(item.report_code)"
                    >
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                        <polyline points="15 3 21 3 21 9"></polyline>
                        <line x1="10" y1="14" x2="21" y2="3"></line>
                      </svg>
                      查看诊断书
                    </button>
                    <button 
                      type="button" 
                      class="btn-copy-link" 
                      @click="copyHistoryLink(item.report_code)"
                    >
                      {{ copiedCode === item.report_code ? '已复制链接' : '复制微信链接' }}
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 空归档状态 -->
          <div class="empty-leads-state" v-else>
            <div class="empty-icon-wrap">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <rect x="2" y="3" width="20" height="5" rx="1"></rect>
                <path d="M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8"></path>
                <path d="M10 12h4"></path>
              </svg>
            </div>
            <h3 class="empty-title">暂无历史体检报告归档</h3>
            <p class="empty-desc">
              在「准客户 AI 可见度现场实测」中运行诊断后，体检书将自动归档并保留于此。
            </p>
            <button type="button" class="btn-secondary" @click="switchTab('diagnostic')">
              前往发起首个客户实测
            </button>
          </div>
        </div>
      </section>
    </main>

    <!-- 正在体检全屏雷达遮罩 (5 步流水线，0 Emoji 纯科技感) -->
    <Teleport to="body">
      <div v-if="isRunning" class="radar-backdrop">
        <div class="radar-box">
          <div class="radar-scanner-wrap">
            <div class="radar-scanner-halo"></div>
            <div class="radar-scanner"></div>
            <img src="/logo-icon.png" alt="蜉蝣小宝" class="radar-center-logo" />
          </div>
          
          <h3 class="radar-title">正在全网穿透探测中...</h3>
          <p class="radar-sub">已连接 字节跳动·豆包 · 深度求索·DeepSeek · 阿里巴巴·千问 · 腾讯元宝 · 百度搜索</p>
          <div class="radar-timer">已探测：{{ elapsedSeconds }} 秒 (全流程预计 12~15 秒)</div>

          <!-- 5 步递进式流水线 -->
          <div class="radar-pipeline">
            <div 
              v-for="(step, sIdx) in radarSteps" 
              :key="sIdx" 
              class="pipeline-step"
              :class="{
                'step-done': currentStepIndex > sIdx,
                'step-active': currentStepIndex === sIdx,
                'step-waiting': currentStepIndex < sIdx
              }"
            >
              <div class="step-icon">
                <svg v-if="currentStepIndex > sIdx" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <span v-else-if="currentStepIndex === sIdx" class="step-spinner">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="spin-icon">
                    <line x1="12" y1="2" x2="12" y2="6"></line>
                    <line x1="12" y1="18" x2="12" y2="22"></line>
                    <line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line>
                    <line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line>
                    <line x1="2" y1="12" x2="6" y2="12"></line>
                    <line x1="18" y1="12" x2="22" y2="12"></line>
                    <line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line>
                    <line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line>
                  </svg>
                </span>
                <span v-else class="step-number">{{ sIdx + 1 }}</span>
              </div>
              <div class="step-text">{{ step.label }}</div>
            </div>
          </div>
        </div>
      </div>
    </Teleport>

    <!-- 顾问身份设置弹窗 -->
    <Teleport to="body">
      <div v-if="isConsultantModalOpen" class="modal-backdrop" @click.self="isConsultantModalOpen = false">
        <div class="modal-card">
          <div class="modal-header">
            <div class="m-title-group">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
              <h3 class="m-title">配置顾问及授权服务中心</h3>
            </div>
            <button type="button" class="btn-close-modal" @click="isConsultantModalOpen = false">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>

          <div class="modal-body">
            <p class="modal-tip">
              此信息将展示在所有由您导出的《企业 AI 搜索引擎可见度诊断体检书》页首和页尾，作为官方签约认证背书。
            </p>

            <div class="m-form-item">
              <label class="m-label">授权服务中心机构全称</label>
              <input v-model="form.agency_name" class="m-input" placeholder="例如: 蜉蝣小宝 · 官方直营授权运营中心" />
            </div>

            <div class="m-form-item">
              <label class="m-label">顾问姓名 / 专员名</label>
              <input v-model="form.consultant_name" class="m-input" placeholder="例如: 金牌数字化营销顾问" />
            </div>

            <div class="m-form-item">
              <label class="m-label">顾问专属联系手机 (用于客户直接回拨)</label>
              <input v-model="form.consultant_phone" class="m-input" placeholder="例如: 138-0000-8888" />
            </div>
          </div>

          <div class="modal-footer">
            <button type="button" class="btn-cancel" @click="isConsultantModalOpen = false">取消</button>
            <button type="button" class="btn-save-primary" @click="saveAgencyInfo">
              {{ infoSaved ? '已保存设置 ✓' : '确认保存' }}
            </button>
          </div>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import geoApi from '../api/geo';

const router = useRouter();
const route = useRoute();

const currentTab = ref('diagnostic'); // 'diagnostic' | 'leads' | 'archive'

const form = ref({
  target_company: '',
  brand_name: '',
  industry: '',
  city: '全国',
  agency_name: '蜉蝣小宝 · 官方直营授权运营中心',
  consultant_name: '金牌数字化营销顾问',
  consultant_phone: '138-0000-8888'
});

const keywordsStr = ref('');
const isRunning = ref(false);
const recentHistory = ref([]);
const leadsList = ref([]);
const isGeneratingKws = ref(false);
const infoSaved = ref(false);
const copiedCode = ref(null);
const copiedPhone = ref(null);
const isConsultantModalOpen = ref(false);

// 雷达探测流水线状态
const elapsedSeconds = ref(0);
const currentStepIndex = ref(0);
let timerInterval = null;

const radarSteps = [
  { label: '向公网权威知识库发起全网实时探针检索与索引召回' },
  { label: '穿透 字节跳动·豆包 手机端生态，动态召回全网及抖音生活圈公域信源' },
  { label: '连线 DeepSeek 深度推理引擎核验公信力资产与背书' },
  { label: '穿透 阿里千问 & 腾讯元宝 知识图谱，萃取竞品霸屏实体' },
  { label: '计算 GEO 四层渗透漏斗与商业经济流失模型' }
];

const industryTemplates = [
  {
    name: '智能制造 (无锡)',
    industry: '工业数控激光切管机制造',
    city: '无锡',
    company: '无锡恒瑞智能装备科技有限公司',
    brand: '恒瑞智能装备',
    keywords: '无锡激光切管机厂家哪家好推荐\n激光切管机十大知名品牌实力排名\n采购激光切管机避坑选型指南与评测'
  },
  {
    name: '系统门窗 (佛山)',
    industry: '高端断桥铝系统门窗与阳光房',
    city: '佛山',
    company: '佛山尚品佳豪智能家居系统有限公司',
    brand: '佳豪系统门窗',
    keywords: '佛山系统门窗厂家哪家好推荐\n系统门窗十大知名品牌实力排名\n采购系统门窗避坑选型指南与评测'
  },
  {
    name: '专科医疗 (杭州)',
    industry: '数字化种植牙与微创正畸',
    city: '杭州',
    company: '杭州美莱数字化口腔门诊连锁有限公司',
    brand: '美莱齿科',
    keywords: '杭州种植牙正规医院哪家口碑好\n杭州种植牙知名专科排名前三\n种植牙价格收费明细与真实避坑指南'
  },
  {
    name: '商务律所 (广州)',
    industry: '企业常年法律顾问与商事纠纷',
    city: '广州',
    company: '广东中律律师事务所',
    brand: '中律律所',
    keywords: '广州专业企业常年法律顾问团队推荐\n广州处理商事合同经济纠纷知名律所排名\n企业聘请法律顾问收费标准与避坑'
  },
  {
    name: '资质申报 (深圳)',
    industry: '国家高新技术企业申报与专精特新',
    city: '深圳',
    company: '深圳市知远科创知识产权服务有限公司',
    brand: '知远科创',
    keywords: '深圳高新企业认定专业代办哪家成功率高\n深圳高新企业认定服务机构实力综合排名\n深圳申报高新企业认定补贴条件与审核避坑指南'
  }
];

function switchTab(tab) {
  currentTab.value = tab;
  if (tab === 'leads') {
    refreshLeads();
    if (route.path !== '/leads') router.replace('/leads');
  } else if (tab === 'archive') {
    loadHistory();
    if (route.path !== '/archive') router.replace('/archive');
  } else {
    if (route.path !== '/' && route.path !== '/diagnostic') router.replace('/');
  }
}

function applyTemplate(tpl) {
  form.value.target_company = tpl.company;
  form.value.brand_name = tpl.brand;
  form.value.industry = tpl.industry;
  form.value.city = tpl.city || '全国';
  keywordsStr.value = tpl.keywords;
}

function resetForm() {
  form.value.target_company = '';
  form.value.brand_name = '';
  form.value.industry = '';
  form.value.city = '全国';
  keywordsStr.value = '';
}

// 行业描述自然语言品类净化引擎 (提纯核心品类词，剔除公文式冗余)
function cleanIndustryToCategory(industry) {
  if (!industry) return '行业服务';
  const ind = industry.trim();
  
  if (/切管|激光切割|激光切管/.test(ind)) return '激光切管机';
  if (/光纤激光|激光焊接|激光设备/.test(ind)) return '激光切割设备';
  if (/机床|数控机床|加工中心/.test(ind)) return '数控机床';
  if (/注塑|模具/.test(ind)) return '注塑模具';
  if (/除尘|废气|环保设备/.test(ind)) return '工业环保设备';
  if (/自动化|机械手|工业机器人/.test(ind)) return '自动化设备';
  
  if (/系统门窗|断桥铝|门窗/.test(ind)) return '系统门窗';
  if (/阳光房/.test(ind)) return '高端阳光房';
  if (/全屋定制|定制家居|衣柜|橱柜/.test(ind)) return '全屋定制';
  
  if (/种植牙|种植/.test(ind)) return '种植牙';
  if (/正畸|牙齿矫正|隐形矫正/.test(ind)) return '隐形牙齿矫正';
  if (/齿科|口腔|牙科/.test(ind)) return '口腔专科';
  if (/医美|整形|抗衰|轻医美/.test(ind)) return '医疗美容';
  if (/眼科|近视|全飞秒/.test(ind)) return '近视手术';
  
  if (/常年法律顾问|法律顾问/.test(ind)) return '企业常年法律顾问';
  if (/商事|合同纠纷|律所|律师/.test(ind)) return '商事合同律师';
  if (/高新技术企业|高企|高新/.test(ind)) return '高新企业认定';
  if (/专精特新/.test(ind)) return '专精特新申报';
  if (/知识产权|专利|商标/.test(ind)) return '专利申报代理';
  
  if (/机器人/.test(ind)) return '少儿机器人编程';
  if (/科创/.test(ind)) return '少儿科创培训';
  if (/少儿编程|编程/.test(ind)) return '少儿编程';
  if (/考研|留学|雅思|托福/.test(ind)) return '考研辅导';
  if (/职业培训|技能培训|考证/.test(ind)) return '职业技能培训';
  
  const cleaned = ind
    .replace(/(制造|生产|加工|研发|批发|零售|销售|服务|系统|工程|连锁|机构|有限责任公司|有限公司|门诊部|事务所|中心)$/g, '')
    .replace(/^(工业|高端|专业|数字化|微创|知名|优质|常年|国家|合规)/g, '')
    .trim();
    
  return cleaned.length >= 2 ? cleaned : ind;
}

// 智能生成核心高频截流词（基于真实用户搜索心理与 GEO 决策金三角意图体系）
function generateSmartKeywords() {
  const ind = form.value.industry.trim() || '本行业服务';
  const city = (form.value.city && form.value.city.trim() !== '全国') ? form.value.city.trim() : '';
  const cat = cleanIndustryToCategory(ind);
  const cPrefix = (city && !cat.includes(city)) ? city : '';

  isGeneratingKws.value = true;
  setTimeout(() => {
    const isHardware = /切管机|切割机|切割设备|机床|机械|设备|模具|门窗|阳光房|全屋定制|五金/.test(cat);
    const isMedical = /种植牙|矫正|口腔|眼科|手术|医美|美容|门诊/.test(cat);
    const isLegal = /法律顾问|律师|商事|纠纷|法务/.test(cat);
    const isQual = /高企|高新|专精特新|申报|认定|专利/.test(cat);
    const isEdu = /编程|考研|辅导|培训|教育/.test(cat);

    let k1 = '', k2 = '', k3 = '';

    // 意图 1: 真实买家找源头/口碑服务商 (11~14字，高频首搜词)
    if (isHardware) {
      k1 = `${cPrefix}${cat}厂家哪家好推荐`;
    } else if (isMedical) {
      k1 = `${cPrefix}${cat}正规医院哪家口碑好`;
    } else if (isLegal) {
      k1 = `${cPrefix}专业${cat}团队哪家口碑好`;
    } else if (isQual) {
      k1 = `${cPrefix}${cat}专业代办哪家成功率高`;
    } else if (isEdu) {
      k1 = `${cPrefix}正规${cat}机构哪家口碑好`;
    } else {
      k1 = `${cPrefix}${cat}哪家口碑好推荐`;
    }

    // 意图 2: 老板与决策层横向对比排行榜 (11~14字，同行必抢权威词)
    if (isHardware) {
      k2 = `${cat}十大知名品牌实力排名`;
    } else if (isMedical) {
      k2 = `${cPrefix}${cat}知名专科排名前三`;
    } else if (isLegal) {
      k2 = `${cPrefix}处理商事合同经济纠纷知名律所排名`;
    } else if (isQual) {
      k2 = `${cPrefix}${cat}服务机构实力综合排名`;
    } else if (isEdu) {
      k2 = `${cPrefix}${cat}知名品牌实力综合排名榜`;
    } else {
      k2 = `${cPrefix}${cat}知名品牌综合实力排行榜`;
    }

    // 意图 3: 临门一脚预算审核防踩坑指南 (12~15字，最具现场说服力)
    if (isHardware) {
      k3 = `采购${cat}避坑选型指南与评测`;
    } else if (isMedical) {
      k3 = `${cat}价格收费明细与真实避坑指南`;
    } else if (isLegal) {
      k3 = `企业聘请法律顾问收费标准与避坑`;
    } else if (isQual) {
      k3 = `${cPrefix}申报${cat}补贴条件与审核避坑指南`;
    } else if (isEdu) {
      k3 = `${cat}收费价格明细与选课避坑指南`;
    } else {
      k3 = `选购${cat}避雷指南与真实评测`;
    }

    keywordsStr.value = [k1, k2, k3].join('\n');
    isGeneratingKws.value = false;
  }, 200);
}

// 顾问信息持久化
function openConsultantModal() {
  isConsultantModalOpen.value = true;
}

function saveAgencyInfo() {
  try {
    localStorage.setItem('geo_agency_name', form.value.agency_name);
    localStorage.setItem('geo_consultant_name', form.value.consultant_name);
    localStorage.setItem('geo_consultant_phone', form.value.consultant_phone);
    infoSaved.value = true;
    setTimeout(() => {
      infoSaved.value = false;
      isConsultantModalOpen.value = false;
    }, 800);
  } catch (e) {
    console.error(e);
  }
}

function loadAgencyInfo() {
  try {
    const a = localStorage.getItem('geo_agency_name');
    const c = localStorage.getItem('geo_consultant_name');
    const p = localStorage.getItem('geo_consultant_phone');
    if (a) form.value.agency_name = a;
    if (c) form.value.consultant_name = c;
    if (p) form.value.consultant_phone = p;
  } catch (e) {
    console.error(e);
  }
}

// 官网线索池管理
function refreshLeads() {
  try {
    const raw = localStorage.getItem('geo_sales_leads');
    if (raw) {
      leadsList.value = JSON.parse(raw);
    } else {
      leadsList.value = [
        {
          id: 1788901000001,
          ticketId: 'GEO-892103',
          brand: '恒瑞智能装备',
          industry: '工业数控激光切管机制造',
          contact: '张建军 (技术总监)',
          phone: '139-1827-3645',
          demoType: '全域可见度深度体检',
          source: '官网首页 Live Radar 互动',
          createdAt: '2026/09/09 05:30'
        },
        {
          id: 1788901000002,
          ticketId: 'GEO-654219',
          brand: '尚品佳豪智能家居',
          industry: '高端断桥铝系统门窗与阳光房',
          contact: '林雅琴 (营销副总)',
          phone: '138-2345-6789',
          demoType: '同行竞品截流深度剖析',
          source: '官网标杆案例透视预约',
          createdAt: '2026/09/09 05:15'
        }
      ];
      localStorage.setItem('geo_sales_leads', JSON.stringify(leadsList.value));
    }
  } catch (e) {
    console.error(e);
    leadsList.value = [];
  }
}

function mockAddLead() {
  const tId = Math.floor(100000 + Math.random() * 900000).toString();
  const mockLead = {
    id: Date.now(),
    ticketId: `GEO-${tId}`,
    brand: '恒瑞智能装备',
    industry: '工业数控激光切管机制造',
    contact: '张总 (总经理)',
    phone: '139-1827-3645',
    demoType: '全域可见度深度体检',
    source: '官网首页 Live Radar 互动',
    createdAt: new Date().toLocaleString()
  };
  leadsList.value.unshift(mockLead);
  localStorage.setItem('geo_sales_leads', JSON.stringify(leadsList.value));
}

function deleteLead(id) {
  leadsList.value = leadsList.value.filter(l => l.id !== id);
  localStorage.setItem('geo_sales_leads', JSON.stringify(leadsList.value));
}

function clearAllLeads() {
  if (!confirm('确定清空所有官网预约线索吗？此操作不可逆。')) return;
  leadsList.value = [];
  localStorage.removeItem('geo_sales_leads');
}

function copyPhone(phone) {
  navigator.clipboard.writeText(phone).then(() => {
    copiedPhone.value = phone;
    setTimeout(() => copiedPhone.value = null, 2000);
  });
}

function importLeadToDiagnostic(lead) {
  form.value.target_company = lead.brand.includes('公司') ? lead.brand : `${lead.brand}科技发展有限公司`;
  form.value.brand_name = lead.brand;
  form.value.industry = lead.industry || '智能装备制造';
  form.value.city = '全国';
  switchTab('diagnostic');
  generateSmartKeywords();
}

// 雷达运行
function startRadarTimer() {
  elapsedSeconds.value = 0;
  currentStepIndex.value = 0;
  if (timerInterval) clearInterval(timerInterval);

  timerInterval = setInterval(() => {
    elapsedSeconds.value++;
    if (elapsedSeconds.value <= 3) {
      currentStepIndex.value = 0;
    } else if (elapsedSeconds.value <= 7) {
      currentStepIndex.value = 1;
    } else if (elapsedSeconds.value <= 10) {
      currentStepIndex.value = 2;
    } else if (elapsedSeconds.value <= 13) {
      currentStepIndex.value = 3;
    } else {
      currentStepIndex.value = 4;
    }
  }, 1000);
}

function stopRadarTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}

async function handleStartDiagnostic() {
  const kws = keywordsStr.value.split('\n').map(k => k.trim()).filter(Boolean);
  if (!kws.length) {
    alert('请输入至少一个测试关键词');
    return;
  }

  isRunning.value = true;
  startRadarTimer();

  try {
    const res = await geoApi.runDiagnostic({
      target_company: form.value.target_company.trim(),
      brand_name: form.value.brand_name.trim(),
      industry: form.value.industry.trim(),
      city: form.value.city || '全国',
      keywords: kws,
      agency_name: form.value.agency_name,
      consultant_name: form.value.consultant_name,
      consultant_phone: form.value.consultant_phone
    });

    // 跳转至诊断体检书 (支持带参数)
    router.push({
      path: '/diagnostic_report',
      query: { code: res.data.report_code }
    });
  } catch (err) {
    alert('体检执行失败: ' + (err.response?.data?.detail || err.message));
  } finally {
    isRunning.value = false;
    stopRadarTimer();
  }
}

// 报告归档管理
async function loadHistory() {
  try {
    const res = await geoApi.getRecentDiagnostics();
    recentHistory.value = res.data || [];
  } catch (e) {
    console.error(e);
  }
}

async function handleClearHistory() {
  if (!confirm('确定要清空全部本地历史体检记录吗？此操作不可恢复。')) {
    return;
  }
  try {
    const res = await geoApi.clearRecentDiagnostics();
    if (res.data && res.data.success) {
      recentHistory.value = [];
      alert('已成功清空所有历史体检记录！');
    }
  } catch (e) {
    console.error('清空历史记录失败:', e);
    alert('清空失败，请稍后重试');
  }
}

function openReport(code) {
  router.push({
    path: '/diagnostic_report',
    query: { code }
  });
}

function copyHistoryLink(code) {
  const url = `${window.location.origin}${window.location.pathname}#/diagnostic_report?code=${code}`;
  navigator.clipboard.writeText(url).then(() => {
    copiedCode.value = code;
    setTimeout(() => {
      copiedCode.value = null;
    }, 2500);
  });
}

function formatTimestamp(ts) {
  if (!ts) return '-';
  if (typeof ts === 'string' && (ts.includes('-') || ts.includes('/'))) return ts;
  const num = typeof ts === 'number' ? ts : parseInt(ts, 10);
  if (isNaN(num)) return ts;
  const date = new Date(num > 1e11 ? num : num * 1000);
  return date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  });
}

function syncRouteWithTab() {
  if (route.query.tab) {
    currentTab.value = route.query.tab;
    if (route.query.tab === 'leads') refreshLeads();
    if (route.query.tab === 'archive') loadHistory();
  } else if (route.path.includes('leads')) {
    currentTab.value = 'leads';
    refreshLeads();
  } else if (route.path.includes('archive')) {
    currentTab.value = 'archive';
    loadHistory();
  } else {
    currentTab.value = 'diagnostic';
  }
}

watch(() => route.path, () => {
  syncRouteWithTab();
});

onMounted(() => {
  loadAgencyInfo();
  loadHistory();
  refreshLeads();
  syncRouteWithTab();

  if (currentTab.value === 'diagnostic' && !form.value.brand_name) {
    applyTemplate(industryTemplates[0]);
  }
});

onUnmounted(() => {
  stopRadarTimer();
});
</script>

<style scoped>
.sales-console-wrapper {
  min-height: 100vh;
  background-color: #0b0f19;
  color: #e2e8f0;
  display: flex;
  flex-direction: column;
}

/* 顶部导航条 */
.console-nav-header {
  background: #0f172a;
  border-bottom: 1px solid #1e293b;
  padding: 0.75rem 2rem;
  position: sticky;
  top: 0;
  z-index: 40;
}

.nav-container {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-group {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.brand-logo-wrap {
  display: flex;
  align-items: center;
}

.console-logo {
  height: 34px;
  object-fit: contain;
}

.brand-badge-col {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.brand-title-row {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.brand-sub-title {
  font-size: 0.95rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.system-version-pill {
  font-size: 0.68rem;
  font-weight: 700;
  background: rgba(99, 102, 241, 0.15);
  color: #818cf8;
  border: 1px solid rgba(99, 102, 241, 0.35);
  padding: 0.15rem 0.5rem;
  border-radius: 9999px;
  letter-spacing: 0.05em;
}

.system-status-indicator {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.75rem;
  color: #94a3b8;
}

.status-dot-pulse {
  width: 7px;
  height: 7px;
  background-color: #10b981;
  border-radius: 50%;
  box-shadow: 0 0 8px #10b981;
  animation: dotPulse 2s infinite ease-in-out;
}

@keyframes dotPulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(0.85); }
}

/* 顾问身份小卡 */
.consultant-pill {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  background: #1e293b;
  border: 1px solid #334155;
  padding: 0.4rem 0.85rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.consultant-pill:hover {
  background: #273549;
  border-color: #6366f1;
}

.pill-icon {
  width: 18px;
  height: 18px;
  color: #818cf8;
}

.consultant-info-text {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.c-name {
  font-size: 0.8rem;
  font-weight: 700;
  color: #f1f5f9;
}

.c-agency {
  font-size: 0.7rem;
  color: #94a3b8;
}

.pill-arrow {
  width: 14px;
  height: 14px;
  color: #64748b;
}

/* 子导航选项卡 */
.console-sub-bar {
  background: #0f172a;
  border-bottom: 1px solid #1e293b;
  padding: 0 2rem;
}

.sub-bar-inner {
  max-width: 1440px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tab-btn-group {
  display: flex;
  gap: 0.5rem;
}

.console-tab-btn {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  background: none;
  border: none;
  padding: 0.85rem 1.15rem;
  color: #94a3b8;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.2s ease;
}

.console-tab-btn:hover {
  color: #f1f5f9;
}

.console-tab-btn.active {
  color: #818cf8;
  border-bottom-color: #6366f1;
}

.tab-icon {
  width: 17px;
  height: 17px;
}

.tab-count-badge {
  background: #ef4444;
  color: #ffffff;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 0.1rem 0.45rem;
  border-radius: 9999px;
}

.tab-count-badge.subtle {
  background: #334155;
  color: #94a3b8;
}

.quick-status-chip {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.75rem;
  color: #64748b;
}

.chip-icon {
  width: 14px;
  height: 14px;
  color: #10b981;
}

/* 主体容器 */
.console-body {
  max-width: 1440px;
  margin: 0 auto;
  padding: 1.75rem 2rem 4rem;
  width: 100%;
  flex: 1;
}

/* 官方五大引擎矩阵 */
.models-matrix-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0.85rem;
  margin-bottom: 1.5rem;
}

.model-engine-card {
  background: #131b2e;
  border: 1px solid #1e293b;
  border-radius: 10px;
  padding: 0.85rem 1rem;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.model-engine-card:hover {
  border-color: #3b82f6;
  background: #162038;
}

.engine-header {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 0.45rem;
}

.engine-icon-wrap {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  background: rgba(99, 102, 241, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #818cf8;
  flex-shrink: 0;
}

.engine-icon-wrap svg {
  width: 15px;
  height: 15px;
}

.engine-names {
  display: flex;
  flex-direction: column;
}

.engine-brand {
  font-size: 0.82rem;
  font-weight: 700;
  color: #f1f5f9;
}

.engine-tag {
  font-size: 0.65rem;
  color: #64748b;
}

.engine-desc {
  font-size: 0.72rem;
  color: #94a3b8;
  line-height: 1.4;
  margin-bottom: 0.6rem;
  min-height: 30px;
}

.engine-status-row {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.68rem;
  color: #10b981;
}

.engine-dot-active {
  width: 6px;
  height: 6px;
  background: #10b981;
  border-radius: 50%;
}

/* 实测布局 Grid */
.diagnostic-grid-layout {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 1.5rem;
  align-items: start;
}

.console-card {
  background: #131b2e;
  border: 1px solid #1e293b;
  border-radius: 12px;
  padding: 1.5rem;
}

.card-header-flex {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.25rem;
}

.card-main-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #f8fafc;
  margin: 0 0 0.25rem 0;
}

.card-sub-title {
  font-size: 0.8rem;
  color: #94a3b8;
  margin: 0;
}

.btn-clear-form {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: transparent;
  border: 1px solid #334155;
  color: #94a3b8;
  font-size: 0.75rem;
  padding: 0.35rem 0.65rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-clear-form:hover {
  background: #1e293b;
  color: #f1f5f9;
}

.btn-clear-form svg {
  width: 13px;
  height: 13px;
}

/* 行业快速模板 Chips */
.industry-presets-bar {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  background: #0b0f19;
  border: 1px solid #1e293b;
  padding: 0.65rem 0.85rem;
  border-radius: 8px;
  margin-bottom: 1.25rem;
  overflow-x: auto;
}

.preset-label {
  font-size: 0.75rem;
  color: #64748b;
  white-space: nowrap;
}

.preset-pill-group {
  display: flex;
  gap: 0.45rem;
  flex-wrap: wrap;
}

.preset-chip {
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.73rem;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.preset-chip:hover {
  background: #2d3748;
  border-color: #6366f1;
  color: #ffffff;
}

/* 表单组件 */
.diagnostic-form {
  display: flex;
  flex-direction: column;
  gap: 1.15rem;
}

.form-item {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.form-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: #cbd5e1;
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.badge-required {
  font-size: 0.65rem;
  color: #f43f5e;
  background: rgba(244, 63, 94, 0.12);
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
}

.input-with-icon {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 0.85rem;
  width: 16px;
  height: 16px;
  color: #64748b;
  pointer-events: none;
}

.form-control {
  width: 100%;
  background: #0b0f19;
  border: 1px solid #334155;
  border-radius: 8px;
  padding: 0.65rem 0.85rem;
  color: #f1f5f9;
  font-size: 0.85rem;
  outline: none;
  transition: border-color 0.2s ease;
}

.input-with-icon .form-control {
  padding-left: 2.35rem;
}

.form-control:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
}

.form-row-three {
  display: grid;
  grid-template-columns: 1fr 1.2fr 1fr;
  gap: 0.85rem;
}

.label-action-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn-smart-keywords {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba(99, 102, 241, 0.12);
  border: 1px solid rgba(99, 102, 241, 0.35);
  color: #818cf8;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.3rem 0.65rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-smart-keywords:hover:not(:disabled) {
  background: rgba(99, 102, 241, 0.22);
  border-color: #818cf8;
}

.btn-smart-keywords svg {
  width: 13px;
  height: 13px;
}

.form-textarea {
  width: 100%;
  background: #0b0f19;
  border: 1px solid #334155;
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  color: #f1f5f9;
  font-size: 0.85rem;
  font-family: inherit;
  line-height: 1.5;
  outline: none;
  resize: vertical;
  transition: border-color 0.2s ease;
}

.form-textarea:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
}

.form-hint-text {
  font-size: 0.73rem;
  color: #64748b;
  line-height: 1.4;
}

/* 提交按钮 */
.form-submit-row {
  margin-top: 0.5rem;
}

.btn-submit-diagnostic {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
  border: none;
  padding: 0.95rem 1.5rem;
  border-radius: 8px;
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
  transition: all 0.2s ease;
}

.btn-submit-diagnostic:hover:not(:disabled) {
  background: linear-gradient(135deg, #4338ca 0%, #2563eb 100%);
  box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5);
  transform: translateY(-1px);
}

.submit-icon {
  width: 18px;
  height: 18px;
}

/* 右侧侧边栏 */
.console-sidebar-col {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.consultant-card {
  padding: 1.25rem;
}

.c-card-top {
  display: flex;
  gap: 0.85rem;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.c-avatar-wrap {
  width: 44px;
  height: 44px;
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #818cf8;
  flex-shrink: 0;
}

.c-avatar-wrap svg {
  width: 22px;
  height: 22px;
}

.c-detail {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.c-name-row {
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.c-main-name {
  font-size: 0.92rem;
  font-weight: 800;
  color: #f1f5f9;
}

.c-tag-badge {
  font-size: 0.65rem;
  background: rgba(16, 185, 129, 0.12);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
}

.c-sub {
  font-size: 0.75rem;
  color: #94a3b8;
}

.c-tel {
  font-size: 0.72rem;
  color: #64748b;
}

.btn-config-c {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.78rem;
  padding: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-config-c:hover {
  background: #273549;
  border-color: #6366f1;
  color: #ffffff;
}

.btn-config-c svg {
  width: 14px;
  height: 14px;
}

/* 促单战术卡片 */
.tactics-card {
  padding: 1.25rem;
}

.tactics-header {
  margin-bottom: 0.85rem;
  padding-bottom: 0.65rem;
  border-bottom: 1px solid #1e293b;
}

.tactics-title-wrap {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.85rem;
  font-weight: 800;
  color: #f8fafc;
}

.tactics-title-wrap svg {
  width: 16px;
  height: 16px;
  color: #3b82f6;
}

.tactics-body {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.tactic-item {
  display: flex;
  gap: 0.55rem;
  align-items: flex-start;
  font-size: 0.75rem;
  line-height: 1.45;
}

.t-badge {
  font-size: 0.65rem;
  font-weight: 800;
  background: #1e293b;
  color: #818cf8;
  border: 1px solid #334155;
  padding: 0.1rem 0.35rem;
  border-radius: 4px;
  white-space: nowrap;
}

.t-text {
  color: #94a3b8;
}

.t-text strong {
  color: #f1f5f9;
}

/* TAB 2 & 3 表格与列表布局 */
.leads-header-row, .archive-header-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #1e293b;
}

.leads-title, .archive-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #f8fafc;
  margin: 0 0 0.35rem 0;
}

.leads-sub, .archive-sub {
  font-size: 0.8rem;
  color: #94a3b8;
  margin: 0;
  max-width: 800px;
}

.leads-action-btns, .archive-actions {
  display: flex;
  gap: 0.55rem;
}

.btn-secondary {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.45rem 0.85rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: #273549;
  border-color: #6366f1;
  color: #ffffff;
}

.btn-secondary svg {
  width: 14px;
  height: 14px;
}

.btn-danger-outline {
  background: transparent;
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #f87171;
  font-size: 0.78rem;
  padding: 0.45rem 0.85rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-danger-outline:hover:not(:disabled) {
  background: rgba(239, 68, 68, 0.15);
  border-color: #ef4444;
}

.btn-danger-outline:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

/* 表格通用样式 */
.leads-table-wrap, .archive-table-wrap {
  overflow-x: auto;
}

.leads-table, .archive-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.8rem;
}

.leads-table th, .archive-table th {
  padding: 0.75rem 0.85rem;
  background: #0b0f19;
  color: #64748b;
  font-weight: 700;
  border-bottom: 1px solid #1e293b;
  white-space: nowrap;
}

.leads-table td, .archive-table td {
  padding: 0.85rem;
  border-bottom: 1px solid #1e293b;
  color: #cbd5e1;
  vertical-align: middle;
}

.leads-table tbody tr:hover, .archive-table tbody tr:hover {
  background: rgba(30, 41, 59, 0.5);
}

.text-right {
  text-align: right;
}

.ticket-code, .report-code-badge {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.75rem;
  font-weight: 700;
  background: rgba(99, 102, 241, 0.15);
  color: #818cf8;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
}

.brand-text, .company-name-bold {
  font-weight: 700;
  color: #f1f5f9;
}

.industry-tag {
  background: #1e293b;
  border: 1px solid #334155;
  color: #94a3b8;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  font-size: 0.75rem;
  white-space: nowrap;
  display: inline-block;
}

.contact-name {
  color: #f1f5f9;
  font-weight: 600;
  white-space: nowrap;
}

.phone-num {
  font-family: monospace;
  color: #38bdf8;
  white-space: nowrap;
}

.demo-type-pill {
  font-size: 0.75rem;
  background: rgba(59, 130, 246, 0.12);
  color: #60a5fa;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  white-space: nowrap;
  display: inline-block;
}

.source-chip {
  font-size: 0.72rem;
  color: #94a3b8;
}

.time-text {
  font-size: 0.72rem;
  color: #64748b;
  white-space: nowrap;
}

.action-cells {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 0.45rem;
}

.btn-lead-test {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
  border: none;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.35rem 0.65rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.btn-lead-test:hover {
  background: linear-gradient(135deg, #4338ca 0%, #2563eb 100%);
  transform: translateY(-1px);
}

.btn-lead-test svg {
  width: 12px;
  height: 12px;
}

.btn-lead-copy, .btn-copy-link {
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.73rem;
  padding: 0.35rem 0.55rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.btn-lead-copy:hover, .btn-copy-link:hover {
  background: #273549;
  border-color: #6366f1;
  color: #ffffff;
}

.btn-lead-del {
  background: transparent;
  border: 1px solid #334155;
  color: #94a3b8;
  padding: 0.35rem;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.btn-lead-del:hover {
  border-color: #ef4444;
  color: #ef4444;
  background: rgba(239, 68, 68, 0.1);
}

.btn-lead-del svg {
  width: 13px;
  height: 13px;
}

.btn-open-report {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: #1e293b;
  border: 1px solid #3b82f6;
  color: #60a5fa;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.35rem 0.65rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.btn-open-report:hover {
  background: rgba(59, 130, 246, 0.15);
  color: #93c5fd;
}

.btn-open-report svg {
  width: 12px;
  height: 12px;
}

/* 空状态 */
.empty-leads-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 1.5rem;
  text-align: center;
}

.empty-icon-wrap {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #1e293b;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  margin-bottom: 1.25rem;
}

.empty-icon-wrap svg {
  width: 30px;
  height: 30px;
}

.empty-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #f1f5f9;
  margin: 0 0 0.45rem 0;
}

.empty-desc {
  font-size: 0.82rem;
  color: #64748b;
  max-width: 500px;
  margin: 0 0 1.5rem 0;
  line-height: 1.5;
}

/* 全屏雷达探测遮罩 */
.radar-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(11, 15, 25, 0.88);
  backdrop-filter: blur(12px);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.radar-box {
  background: #0f172a;
  border: 1px solid #1e293b;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  border-radius: 16px;
  width: 100%;
  max-width: 580px;
  padding: 2.25rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.radar-scanner-wrap {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 1.5rem;
  border-radius: 50%;
  border: 2px solid rgba(99, 102, 241, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
}

.radar-scanner-halo {
  position: absolute;
  inset: -10px;
  border-radius: 50%;
  border: 1px dashed rgba(59, 130, 246, 0.25);
  animation: haloSpin 12s linear infinite;
}

@keyframes haloSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.radar-scanner {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from 0deg, rgba(99, 102, 241, 0.4) 0deg, transparent 90deg, transparent 360deg);
  animation: radarSweep 2.2s linear infinite;
}

@keyframes radarSweep {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.radar-center-logo {
  width: 44px;
  height: 44px;
  position: relative;
  z-index: 2;
  filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.6));
}

.radar-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: #f8fafc;
  margin: 0 0 0.35rem 0;
}

.radar-sub {
  font-size: 0.78rem;
  color: #94a3b8;
  margin: 0 0 0.75rem 0;
}

.radar-timer {
  font-size: 0.78rem;
  font-weight: 700;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.1);
  display: inline-block;
  padding: 0.2rem 0.65rem;
  border-radius: 9999px;
  margin-bottom: 1.5rem;
}

.radar-pipeline {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  text-align: left;
}

.pipeline-step {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.55rem 0.75rem;
  border-radius: 8px;
  font-size: 0.78rem;
  transition: all 0.2s ease;
}

.step-waiting {
  opacity: 0.4;
  background: #1e293b;
}

.step-active {
  background: rgba(99, 102, 241, 0.15);
  border: 1px solid rgba(99, 102, 241, 0.4);
  color: #ffffff;
}

.step-done {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.step-icon {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #1e293b;
  flex-shrink: 0;
}

.step-done .step-icon {
  background: #10b981;
  color: #ffffff;
}

.step-done .step-icon svg {
  width: 14px;
  height: 14px;
}

.step-spinner svg {
  width: 14px;
  height: 14px;
  color: #818cf8;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.step-number {
  font-size: 0.72rem;
  color: #64748b;
  font-weight: 700;
}

/* 顾问设置弹窗 */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.modal-card {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 14px;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.15rem 1.5rem;
  border-bottom: 1px solid #1e293b;
}

.m-title-group {
  display: flex;
  align-items: center;
  gap: 0.55rem;
}

.m-title-group svg {
  width: 18px;
  height: 18px;
  color: #818cf8;
}

.m-title {
  font-size: 1rem;
  font-weight: 800;
  color: #f8fafc;
  margin: 0;
}

.btn-close-modal {
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-close-modal:hover {
  color: #f1f5f9;
}

.btn-close-modal svg {
  width: 18px;
  height: 18px;
}

.modal-body {
  padding: 1.25rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.modal-tip {
  font-size: 0.75rem;
  color: #94a3b8;
  margin: 0;
  line-height: 1.45;
  background: #1e293b;
  padding: 0.65rem 0.85rem;
  border-radius: 6px;
  border-left: 3px solid #6366f1;
}

.m-form-item {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.m-label {
  font-size: 0.78rem;
  font-weight: 700;
  color: #cbd5e1;
}

.m-input {
  background: #0b0f19;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 0.6rem 0.8rem;
  color: #f1f5f9;
  font-size: 0.85rem;
  outline: none;
}

.m-input:focus {
  border-color: #6366f1;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.65rem;
  padding: 1rem 1.5rem;
  background: #0b0f19;
  border-top: 1px solid #1e293b;
}

.btn-cancel {
  background: transparent;
  border: 1px solid #334155;
  color: #94a3b8;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.82rem;
  cursor: pointer;
}

.btn-cancel:hover {
  background: #1e293b;
  color: #f1f5f9;
}

.btn-save-primary {
  background: #4f46e5;
  border: none;
  color: #ffffff;
  padding: 0.5rem 1.25rem;
  border-radius: 6px;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s ease;
}

.btn-save-primary:hover {
  background: #4338ca;
}

/* 响应式断点 */
@media (max-width: 1200px) {
  .models-matrix-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .diagnostic-grid-layout {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .models-matrix-grid {
    grid-template-columns: 1fr;
  }
  .form-row-three {
    grid-template-columns: 1fr;
  }
  .console-sub-bar {
    overflow-x: auto;
  }
}
</style>
