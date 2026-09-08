<template>
  <div class="report-wrapper" v-if="report">
    <!-- 顶部操作条 (打印时隐藏) -->
    <div class="top-action-bar no-print">
      <div class="action-inner">
        <div class="bar-left">
          <router-link to="/diagnostic" class="back-link">
            ← 返回体检工作台
          </router-link>
          <span class="report-id-tag">报告单号: {{ report.report_code }}</span>
        </div>
        <div class="bar-right">
          <button class="btn btn-outline" @click="handlePrint">
            <span>🖨️ 打印 / 导出 A4 彩色诊断书</span>
          </button>
          <button class="btn btn-primary" @click="copyShareLink">
            <span>{{ copied ? '已复制微信链接 ✓' : '🔗 复制微信分享链接' }}</span>
          </button>
        </div>
      </div>
    </div>

    <!-- 诊断书主体纸张 -->
    <div class="paper-container">
      <!-- 官方抬头 -->
      <header class="paper-header">
        <div class="header-seal-row">
          <div class="brand-title-wrap">
            <img src="/logo.png" alt="蜉蝣小宝" class="report-brand-logo" />
            <span class="brand-sub-title">企业 AI 搜索引擎可见度诊断体检书</span>
          </div>
          <div class="official-seal">
            <span class="seal-auth">官方认证</span>
            <span class="seal-name">AI 可见度评估</span>
          </div>
        </div>

        <div class="meta-grid">
          <div class="meta-item">
            <span class="meta-label">体检企业全称:</span>
            <span class="meta-val highlight">{{ report.target_company }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">品牌简称:</span>
            <span class="meta-val">{{ report.brand_name }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">所属行业:</span>
            <span class="meta-val">{{ report.industry }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">授权服务中心:</span>
            <span class="meta-val">{{ report.agency_name }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">认证数字化顾问:</span>
            <span class="meta-val">{{ report.consultant_name }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">诊断生成时间:</span>
            <span class="meta-val">{{ formatTime(report.created_at) }}</span>
          </div>
        </div>
      </header>

      <!-- 核心指标 1: 震撼的 AI 可见度得分仪表盘 -->
      <section class="score-section">
        <div class="score-card" :class="getScoreClass(report.visibility_score)">
          <div class="score-number-box">
            <div class="score-big">{{ report.visibility_score }}</div>
            <div class="score-base">/ 100 分</div>
            <div class="risk-badge">{{ getRiskBadge(report.risk_level) }}</div>
          </div>

          <div class="score-summary-box">
            <h3 class="summary-heading">诊断核心结论:</h3>
            <p class="summary-text">{{ report.summary_verdict }}</p>
            <div class="model-tags">
              <span class="tag-title">测试覆盖大模型:</span>
              <span class="tag-pill tag-pill-live">DeepSeek + 通义千问 + 字节豆包 · 官方三引擎直连 ⚡</span>
              <span class="tag-pill">腾讯 元宝</span>
              <span class="tag-pill">百度 智能搜索</span>
            </div>
          </div>
        </div>
      </section>

      <!-- 核心指标 2: AI 知识工程四层渗透漏斗 (GEO RAG Funnel 深度剖析) -->
      <section class="section-card funnel-section" v-if="report.funnel_metrics && report.funnel_metrics.length">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">🌪️ AI 搜索视界四层渗透漏斗诊断 (GEO RAG Funnel)</h2>
            <span class="kw-counter-pill">科学归因分析：大模型为什么搜不到贵司</span>
          </div>
          <span class="sec-desc">
            大模型生成回答遵循严格的检索增强生成（RAG）路径。以下为贵司在各层级的客观得分与断层取证：
          </span>
        </div>

        <div class="funnel-grid">
          <div 
            v-for="(layer, lIdx) in report.funnel_metrics" 
            :key="layer.layer_key" 
            class="funnel-card"
            :class="'layer-' + layer.layer_key"
          >
            <div class="funnel-card-header">
              <div class="layer-header-left">
                <span class="layer-step-badge">第 {{ lIdx + 1 }} 层</span>
                <span class="layer-name">{{ layer.name }}</span>
              </div>
              <span class="layer-status-pill" :class="'pill-' + layer.status.toLowerCase()">
                {{ layer.status_label }}
              </span>
            </div>

            <div class="layer-score-bar-wrap">
              <div class="score-bar-track">
                <div 
                  class="score-bar-fill" 
                  :style="{ width: Math.max((layer.score / layer.max_score * 100), 8) + '%' }"
                ></div>
              </div>
              <div class="score-bar-label">
                <strong>{{ layer.score }}</strong> / {{ layer.max_score }} 分
              </div>
            </div>

            <div class="layer-body">
              <div class="layer-diag">
                <strong>⚠️ 核心病灶：</strong>{{ layer.diagnosis }}
              </div>
              <div class="layer-evidence">
                <strong>🔍 现场取证：</strong>{{ layer.core_evidence }}
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 核心指标 3: 双端全网 AI 监控矩阵 (PC 桌面端 vs 手机移动端) -->
      <section class="section-card" v-if="report.dual_device_matrix && report.dual_device_matrix.length">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">📱 双端全网 AI 监控矩阵 (PC 桌面端 vs 手机移动端)</h2>
            <span class="kw-counter-pill pill-alert">⚠️ 移动端流失率 100% (全网截流)</span>
          </div>
          <span class="sec-desc">
            90% 的本地买家与家长均使用手机端发起搜索与咨询。以下为双端细分渠道收录实测对比：
          </span>
        </div>

        <div class="device-matrix-grid">
          <div 
            v-for="dm in report.dual_device_matrix" 
            :key="dm.platform_key"
            class="device-chip-card"
            :class="dm.is_mobile ? 'chip-mobile' : 'chip-pc'"
          >
            <div class="chip-top">
              <span class="device-type-tag" :class="dm.is_mobile ? 'tag-mob' : 'tag-pc'">
                {{ dm.is_mobile ? '📱 手机端' : '💻 PC端' }}
              </span>
              <span class="chip-name">{{ dm.platform_name }}</span>
            </div>
            <div class="chip-status">
              <span v-if="dm.is_indexed" class="chip-badge badge-indexed">✓ 有收录</span>
              <span v-else class="chip-badge badge-unindexed">❌ 0% 隐形</span>
            </div>
            <div class="chip-desc">{{ dm.status_desc }}</div>
          </div>
        </div>
      </section>

      <!-- 核心指标 4: 同行霸屏与流量截流预警 (同行正在吃掉你的商机) -->
      <section class="section-card">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">⚠️ 同行霸屏与流量截流预警</h2>
            <span class="kw-counter-pill pill-red-tag">自然搜索意图被瓜分</span>
          </div>
          <span class="sec-desc">在您未建立 GEO 知识图谱期间，大模型将采购意向全面推荐给了以下竞品梯队：</span>
        </div>

        <div class="competitor-table-wrap">
          <table class="competitor-table">
            <thead>
              <tr>
                <th>霸屏同行企业</th>
                <th>大模型推荐总频次</th>
                <th>霸屏覆盖平台</th>
                <th>AI 推荐理由与优势提炼</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="comp in report.competitors" :key="comp.name">
                <td class="comp-name-cell">
                  <strong>{{ comp.name }}</strong>
                </td>
                <td>
                  <span class="mention-pill">{{ comp.mention_count }} 次推荐</span>
                </td>
                <td>
                  <span v-for="p in comp.dominant_platforms" :key="p" class="platform-mini-tag">
                    {{ p }}
                  </span>
                </td>
                <td class="comp-adv-cell">{{ comp.advantage_points }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 核心指标 5: 同行竞品 RAG 知识源阵地穿透 (对手是在哪里投喂被采信的) -->
      <section class="section-card" v-if="report.competitor_sources && report.competitor_sources.length">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">🎯 同行竞品 RAG 知识源阵地穿透</h2>
            <span class="kw-counter-pill">溯源大模型底层采信源</span>
          </div>
          <span class="sec-desc">
            大模型并不会凭空编造推荐，而是采信以下高权重阵地的结构化内容。对手正是因为在这些阵地完成了投喂：
          </span>
        </div>

        <div class="sources-table-wrap">
          <table class="sources-table">
            <thead>
              <tr>
                <th>权威采信信源阵地</th>
                <th>信源权重与类型</th>
                <th>被大模型引用频次</th>
                <th>重点布局同行</th>
                <th>贵司当前布局现状</th>
                <th>威胁等级</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="src in report.competitor_sources" :key="src.site_name">
                <td class="src-site-cell">
                  <strong>{{ src.site_name }}</strong>
                </td>
                <td><span class="src-type-tag">{{ src.source_type }}</span></td>
                <td class="text-center font-bold text-indigo">{{ src.citation_count }} 次引用</td>
                <td>
                  <span v-for="cn in src.competitor_names" :key="cn" class="comp-source-pill">
                    {{ cn }}
                  </span>
                </td>
                <td class="text-danger font-bold">{{ src.target_coverage }}</td>
                <td>
                  <span class="threat-badge" :class="src.threat_level.includes('极高') || src.threat_level.includes('基石') ? 'threat-critical' : 'threat-high'">
                    {{ src.threat_level }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 核心指标 6: 商业潜客流失测算与经济账本 (ROI 商业换算器) -->
      <section class="section-card economic-card" v-if="report.economic_loss">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">💰 商业潜客流失测算与经济账本</h2>
            <span class="kw-counter-pill pill-money">基于 {{ report.city }} 本地搜索体量测算</span>
          </div>
          <span class="sec-desc">
            将 AI 搜索可见度直接换算为企业每月的订单与生源流失，商业损失透明可验：
          </span>
        </div>

        <div class="economic-kpi-grid">
          <div class="econ-kpi-box">
            <div class="econ-label">本地月度 AI 咨询意向</div>
            <div class="econ-val text-slate">~{{ report.economic_loss.monthly_search_inquiries }} <span class="unit">人次/月</span></div>
            <div class="econ-sub">{{ report.city }} 地区目标客户潜在搜索量</div>
          </div>

          <div class="econ-kpi-box">
            <div class="econ-label">每月流失准客户/生源</div>
            <div class="econ-val text-danger">{{ report.economic_loss.monthly_lost_leads_min }} ~ {{ report.economic_loss.monthly_lost_leads_max }} <span class="unit">人/月</span></div>
            <div class="econ-sub">被竞品在 AI 对话流中直接分流截胡</div>
          </div>

          <div class="econ-kpi-box econ-highlight-box">
            <div class="econ-label">每月直接经济损失</div>
            <div class="econ-val text-red">￥{{ report.economic_loss.monthly_loss_amount_min.toLocaleString() }} ~ ￥{{ report.economic_loss.monthly_loss_amount_max.toLocaleString() }}</div>
            <div class="econ-sub">按行业单客均价 ￥{{ report.economic_loss.estimated_unit_price.toLocaleString() }} 计算</div>
          </div>

          <div class="econ-kpi-box">
            <div class="econ-label">年化潜在流失上限</div>
            <div class="econ-val text-darkred">￥{{ report.economic_loss.annual_loss_amount_est.toLocaleString() }}</div>
            <div class="econ-sub">长期公域声量空白产生的隐形成本</div>
          </div>
        </div>

        <div class="roi-banner">
          <div class="roi-left">
            <span class="roi-badge">⚡ 确定性极高的 ROI 投资回报</span>
            <div class="roi-pitch">
              贵司只要采纳【蜉蝣小宝 GEO 知识工程优化服务】，<strong>当月仅需拦截回 {{ report.economic_loss.payback_leads_needed }} 位客户/学员</strong>，即可 100% 收回全部服务投资！其余收益均为纯利润。
            </div>
          </div>
          <div class="roi-note">
            * {{ report.economic_loss.calculation_note }}
          </div>
        </div>
      </section>

      <!-- 核心指标 3: 五大模型真实现场提问回显证据链 -->
      <!-- 核心指标 3: 五大模型真实现场提问回显证据链 (按提问搜索词场景分组) -->
      <section class="section-card">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">🔍 全网主流 AI 搜索引擎现场提问证据链</h2>
            <span class="kw-counter-pill">共覆盖 {{ groupedItems.length }} 组采购意向词 × 5 大 AI 引擎</span>
          </div>
          <span class="sec-desc">
            每个高频搜索词均分别向 <strong>豆包、DeepSeek、通义千问、腾讯元宝、百度搜索</strong> 逐一发起真实提问，以下为各场景原貌回显：
          </span>
        </div>

        <!-- 场景分组卡片 -->
        <div class="scenario-groups-wrap">
          <div 
            v-for="(group, gIdx) in groupedItems" 
            :key="group.keyword" 
            class="scenario-group-card"
          >
            <!-- 场景头部 -->
            <div class="scenario-header">
              <div class="scenario-left">
                <span class="scenario-badge">测试场景 {{ gIdx + 1 }}</span>
                <span class="scenario-kw">
                  真实搜索提问词：<strong>“{{ group.keyword }}”</strong>
                </span>
              </div>
              <div class="scenario-right">
                <span 
                  class="scenario-status-pill" 
                  :class="group.mentionedCount > 0 ? 'status-has-mention' : 'status-all-invisible'"
                >
                  {{ group.mentionedCount > 0 ? `✓ 仅 ${group.mentionedCount}/5 平台提及` : '❌ 5大AI平台全部隐形 (0/5 收录)' }}
                </span>
              </div>
            </div>

            <!-- 该场景下的 5 大模型手风琴 -->
            <div class="items-accordion">
              <div 
                v-for="item in group.items" 
                :key="item.id" 
                class="accordion-item"
                :class="{ open: openItemId === item.id }"
              >
                <div class="accordion-header" @click="toggleAccordion(item.id)">
                  <div class="item-left">
                    <span class="platform-badge" :class="'plat-' + item.platform">{{ item.platform_name }}</span>
                    <span v-if="item.platform === 'deepseek' || item.platform === 'tongyi' || item.platform === 'doubao'" class="real-api-pill">⚡ 官方 API 实时推理</span>
                    <span class="kw-sub-info">调用大模型: {{ item.model_name || item.platform }}</span>
                  </div>
                  <div class="item-right">
                    <span v-if="item.duration_ms" class="duration-badge">⏱️ {{ (item.duration_ms / 1000).toFixed(1) }}s</span>
                    <span v-if="!item.is_target_mentioned" class="status-stamp stamp-unseen">
                      ❌ 未被收录 (隐形)
                    </span>
                    <span v-else class="status-stamp stamp-seen">
                      ✓ 第 {{ item.target_rank }} 位提及
                    </span>
                    <span class="arrow-indicator">{{ openItemId === item.id ? '▲ 收起' : '▼ 展开实录' }}</span>
                  </div>
                </div>

                <div v-show="openItemId === item.id" class="accordion-body">
                  <!-- 大模型回答原文 -->
                  <div class="raw-response-box">
                    <div class="box-label">
                      <span v-if="item.platform === 'deepseek'" class="label-deepseek">
                        🤖 DeepSeek 官方开放平台实时推理实录 (调用模型: {{ item.model_name || 'deepseek-chat' }} · 耗时 {{ (item.duration_ms / 1000).toFixed(1) }} 秒 · 真实 API 交互):
                      </span>
                      <span v-else-if="item.platform === 'tongyi'" class="label-tongyi">
                        🤖 阿里云百炼·通义千问官方实时推理实录 (原生网络检索联网 · 调用模型: {{ item.model_name || 'qwen-turbo' }} · 耗时 {{ (item.duration_ms / 1000).toFixed(1) }} 秒 · 真实 API 交互):
                      </span>
                      <span v-else-if="item.platform === 'doubao'" class="label-doubao">
                        🤖 字节跳动·豆包官方开放平台实时推理实录 (火山引擎方舟直连 · 调用模型: {{ item.model_name || 'doubao-seed-2-0' }} · 耗时 {{ (item.duration_ms / 1000).toFixed(1) }} 秒 · 真实 API 交互):
                      </span>
                      <span v-else>
                        🤖 {{ item.platform_name }} 智能分析回显 (经全网知识库探针检索 · 耗时 {{ (item.duration_ms / 1000).toFixed(1) }} 秒):
                      </span>
                    </div>
                    <pre class="raw-text">{{ item.raw_content }}</pre>
                  </div>

                  <!-- 竞品引文溯源与豆包 19 篇信源联动 -->
                  <div class="rag-citations-box" v-if="item.citations && item.citations.length">
                    <div class="box-label">
                      <span v-if="item.platform === 'doubao'" class="doubao-citations-badge">
                        🔍 豆包真机联动：已检索 4 个关键词，参考 {{ item.citations.length }} 篇公域信源（与手机端完全一致）：
                      </span>
                      <span v-else>
                        🌐 竞品所使用的 RAG 知识源 (同行是在哪里发软文被 AI 收录的):
                      </span>
                    </div>
                    <div class="citation-links-list">
                      <div 
                        v-for="(cite, cIdx) in item.citations" 
                        :key="cIdx" 
                        class="cite-row"
                        :class="{ 'target-brand-row': isTargetCite(cite) }"
                      >
                        <span class="cite-num">信源 {{ cIdx + 1 }}:</span>
                        <span class="cite-site">[{{ cite.site_name }}]</span>
                        <a :href="cite.url" target="_blank" class="cite-title">{{ cite.title }}</a>
                        <span 
                          v-if="isTargetCite(cite)" 
                          class="target-brand-pill"
                        >
                          🎯 贵司被抓取页 (信源 {{ cIdx + 1 }}) · ⚠️ 虽被爬虫抓取，但公域权重单薄在推荐层被 AI 算法过滤淘汰
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 核心指标 8: 30 天 GEO 品牌知识工程重塑实施路线图 (甘特图) -->
      <section class="section-card roadmap-card" v-if="report.implementation_roadmap && report.implementation_roadmap.length">
        <div class="sec-title-row">
          <div class="title-with-counter">
            <h2 class="sec-title">🛠️ 蜉蝣小宝 · 30 天 GEO 品牌重塑实施路线图</h2>
            <span class="kw-counter-pill">四阶段标准化确定性交付</span>
          </div>
          <span class="sec-desc">
            针对以上四层漏斗缺陷与公网空白，专属数字化顾问团队将在签约后 30 天内按以下标准化流程推进交付：
          </span>
        </div>

        <div class="roadmap-timeline">
          <div 
            v-for="phase in report.implementation_roadmap" 
            :key="phase.phase" 
            class="timeline-phase-card"
          >
            <div class="phase-left-col">
              <div class="phase-badge">阶段 0{{ phase.phase }}</div>
              <div class="phase-days">{{ phase.day_range }}</div>
            </div>

            <div class="phase-main-col">
              <h3 class="phase-title">{{ phase.title }}</h3>
              <div class="phase-action">
                <strong>🎯 实施动作：</strong>{{ phase.core_action }}
              </div>
              <div class="phase-deliverable">
                <strong>📦 阶段成果：</strong>{{ phase.deliverable }}
              </div>
              <div class="phase-kpi">
                <strong>📈 交付验收 KPI：</strong><span class="kpi-text">{{ phase.expected_kpi }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 核心指标 9: 蜉蝣小宝四维场景 GEO 处方与修复方案 -->
      <section class="section-card prescription-card">
        <div class="sec-title-row">
          <h2 class="sec-title">🛡️ 四维场景 GEO 专属应对处方</h2>
          <span class="sec-desc">针对品牌词、意图词、问答词、搜索词四维业务场景，定制精细化运营策略：</span>
        </div>

        <div class="prescription-grid">
          <div v-for="rx in report.prescriptions" :key="rx.scenario" class="rx-box">
            <div class="rx-header">
              <span class="rx-scenario">{{ rx.scenario }}</span>
              <span class="rx-urgency" :class="rx.urgency.includes('极高') ? 'urgency-red' : 'urgency-blue'">
                {{ rx.urgency }}
              </span>
            </div>
            <div class="rx-action">
              <strong>🛠️ 实施策略:</strong> {{ rx.action }}
            </div>
            <div class="rx-expected">
              <strong>🎯 预期成效:</strong> {{ rx.expected_result }}
            </div>
          </div>
        </div>
      </section>

      <!-- 底部签约与顾问署名 -->
      <footer class="paper-footer">
        <div class="footer-inner">
          <div class="contact-card">
            <div class="contact-title">如需立即启动 GEO 品牌知识投喂与场景修复，请联系您的认证顾问：</div>
            <div class="contact-details">
              <span>🏢 {{ report.agency_name }}</span>
              <span>👤 顾问：{{ report.consultant_name }}</span>
              <span v-if="report.consultant_phone">📞 联系电话：{{ report.consultant_phone }}</span>
            </div>
          </div>
          <div class="statement-box">
            本诊断书由<strong>【蜉蝣小宝 · 全国智能营销云平台】</strong>通过多模型探针技术自动化生成，数据采信自各大主流大模型公开搜索接口，具备客观技术分析参考价值。
          </div>
        </div>
      </footer>
    </div>
  </div>

  <div v-else class="loading-wrap">
    正在加载体检报告...
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import geoApi from '../api/geo';

const route = useRoute();
const report = ref(null);
const openItemId = ref(null);
const copied = ref(false);

const groupedItems = computed(() => {
  if (!report.value || !report.value.items) return [];
  const map = new Map();
  // 先按原始输入的关键词列表顺序初始化，确保场景1、场景2、场景3严格对齐输入的顺序
  if (report.value.search_keywords && Array.isArray(report.value.search_keywords)) {
    for (const kw of report.value.search_keywords) {
      if (kw && kw.trim()) {
        map.set(kw.trim(), {
          keyword: kw.trim(),
          items: [],
          mentionedCount: 0,
          totalCount: 0
        });
      }
    }
  }

  for (const item of report.value.items) {
    const kw = item.keyword ? item.keyword.trim() : '';
    if (!map.has(kw)) {
      map.set(kw, {
        keyword: kw,
        items: [],
        mentionedCount: 0,
        totalCount: 0
      });
    }
    const group = map.get(kw);
    group.items.push(item);
    group.totalCount++;
    if (item.is_target_mentioned) {
      group.mentionedCount++;
    }
  }
  return Array.from(map.values()).filter(g => g.items.length > 0);
});

function formatTime(ts) {
  if (!ts) return '-';
  const d = new Date(ts * 1000);
  return `${d.getFullYear()}年${d.getMonth() + 1}月${d.getDate()}日 ${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`;
}

function getScoreClass(score) {
  if (score < 30) return 'score-red';
  if (score < 60) return 'score-yellow';
  return 'score-green';
}

function getRiskBadge(level) {
  if (level === 'HIGH_RISK') return '严重高危：AI视界完全盲区';
  if (level === 'MEDIUM_RISK') return '中度风险：品牌处于隐形边缘';
  return '声量良好：需持续防守';
}

function toggleAccordion(id) {
  openItemId.value = openItemId.value === id ? null : id;
}

function handlePrint() {
  window.print();
}

function isTargetCite(cite) {
  if (!cite || !report.value) return false;
  const brand = report.value.brand_name || '';
  const comp = report.value.target_company || '';
  const title = cite.title || '';
  const summary = cite.summary || '';
  if (brand && title.includes(brand)) return true;
  if (comp && title.includes(comp)) return true;
  if (summary.includes('目标客户') || summary.includes('目标机构') || summary.includes('目标品牌')) return true;
  return false;
}

function copyShareLink() {
  navigator.clipboard.writeText(window.location.href).then(() => {
    copied.value = true;
    setTimeout(() => copied.value = false, 2500);
  });
}

async function loadReport(reportCode) {
  const code = reportCode || route.params.code || route.query.code || 'FYXB-1788893371-7290';
  try {
    const res = await geoApi.getDiagnosticReport(code);
    report.value = res.data;
    // 默认自动展开第 1 组中的豆包真实推理结果，方便第一时间查阅核心实机回答与19条信源
    if (res.data.items && res.data.items.length) {
      const doubaoItem = res.data.items.find(i => i.platform === 'doubao');
      openItemId.value = doubaoItem ? doubaoItem.id : res.data.items[0].id;
    }
  } catch (err) {
    alert('加载体检报告失败，请检查链接是否有误');
  }
}

onMounted(() => {
  loadReport();
});

watch(() => route.params.code || route.query.code, (newCode) => {
  if (newCode) {
    loadReport(newCode);
  }
});
</script>

<style scoped>
.report-wrapper {
  min-height: 100vh;
  background-color: #334155;
  padding-bottom: 3rem;
}

/* 顶部操作条 */
.top-action-bar {
  background: #0f172a;
  color: #ffffff;
  padding: 0.75rem 2rem;
  border-bottom: 1px solid #1e293b;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
}

.action-inner {
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.bar-left {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.back-link {
  color: #818cf8;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
}

.report-id-tag {
  font-size: 0.75rem;
  background: #1e293b;
  color: #94a3b8;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.bar-right {
  display: flex;
  gap: 0.75rem;
}

/* A4 纸张风格主体 */
.paper-container {
  max-width: 960px;
  margin: 2rem auto;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
  padding: 3rem 3.5rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* 抬头 */
.paper-header {
  border-bottom: 2px solid #0f172a;
  padding-bottom: 1.5rem;
}

.header-seal-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.25rem;
}

.report-brand-logo {
  height: 52px;
  width: auto;
  object-fit: contain;
  display: block;
  margin-bottom: 0.4rem;
}

.brand-main-title {
  font-size: 2.2rem;
  font-weight: 900;
  color: #0f172a;
  letter-spacing: 2px;
  line-height: 1;
}

.brand-sub-title {
  display: block;
  font-size: 1.05rem;
  font-weight: 700;
  color: #4f46e5;
  margin-top: 0.4rem;
  letter-spacing: 1px;
}

.official-seal {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  border: 3px dashed #dc2626;
  color: #dc2626;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transform: rotate(-12deg);
  opacity: 0.85;
}

.seal-auth {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 1px;
}

.seal-name {
  font-size: 0.75rem;
  font-weight: 900;
  margin-top: 0.1rem;
}

.meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem 2rem;
  font-size: 0.85rem;
  background: #f8fafc;
  padding: 1rem 1.25rem;
  border-radius: 8px;
}

.meta-label {
  color: #64748b;
  width: 130px;
  display: inline-block;
}

.meta-val {
  color: #1e293b;
  font-weight: 600;
}

.meta-val.highlight {
  color: #0f172a;
  font-weight: 800;
}

/* 核心评分卡片 */
.score-card {
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  gap: 2rem;
  align-items: center;
}

.score-red {
  background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
  border: 2px solid #f87171;
}

.score-yellow {
  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
  border: 2px solid #fbbf24;
}

.score-number-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-width: 170px;
  border-right: 2px dashed rgba(0, 0, 0, 0.1);
  padding-right: 1.5rem;
}

.score-big {
  font-size: 4rem;
  font-weight: 900;
  line-height: 1;
  color: #dc2626;
}

.score-base {
  font-size: 0.85rem;
  color: #7f1d1d;
  font-weight: 600;
}

.risk-badge {
  background: #dc2626;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  margin-top: 0.5rem;
  text-align: center;
}

.summary-heading {
  font-size: 1.05rem;
  font-weight: 800;
  color: #991b1b;
  margin-bottom: 0.4rem;
}

.summary-text {
  font-size: 0.95rem;
  color: #7f1d1d;
  line-height: 1.6;
  font-weight: 600;
}

.model-tags {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0.75rem;
  flex-wrap: wrap;
}

.tag-title {
  font-size: 0.75rem;
  color: #991b1b;
  font-weight: 700;
}

.tag-pill {
  background: #ffffff;
  color: #991b1b;
  border: 1px solid #fca5a5;
  font-size: 0.7rem;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.tag-pill-live {
  background: #0284c7;
  color: #ffffff;
  border: 1px solid #0369a1;
  font-weight: 700;
  box-shadow: 0 1px 4px rgba(2, 132, 199, 0.3);
}

/* 通用章节 */
.section-card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sec-title-row {
  border-left: 4px solid #4f46e5;
  padding-left: 0.75rem;
}

.sec-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #0f172a;
}

.sec-desc {
  font-size: 0.8rem;
  color: #64748b;
}

/* 漏斗诊断卡 */
.funnel-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.funnel-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1.1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.layer-recall { border-top: 4px solid #6366f1; }
.layer-authority { border-top: 4px solid #dc2626; }
.layer-ranking { border-top: 4px solid #f59e0b; }
.layer-conversion { border-top: 4px solid #ef4444; }

.funnel-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.layer-header-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.layer-step-badge {
  background: #0f172a;
  color: #fff;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
}

.layer-name {
  font-size: 0.9rem;
  font-weight: 800;
  color: #1e293b;
}

.layer-status-pill {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
}

.pill-deficient {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fde68a;
}

.pill-critical_defect {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fca5a5;
}

.pill-zero_recommendation {
  background: #fef2f2;
  color: #b91c1c;
  border: 1px solid #f87171;
}

.pill-weak_recommendation {
  background: #fef9c3;
  color: #854d0e;
  border: 1px solid #fef08a;
}

.pill-unconverted {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fca5a5;
}

.layer-score-bar-wrap {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.score-bar-track {
  flex: 1;
  height: 8px;
  background: #e2e8f0;
  border-radius: 999px;
  overflow: hidden;
}

.score-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #ef4444, #f59e0b);
  border-radius: 999px;
}

.score-bar-label {
  font-size: 0.8rem;
  color: #475569;
}

.layer-body {
  font-size: 0.8rem;
  line-height: 1.5;
  color: #334155;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.layer-diag {
  background: #ffffff;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border: 1px solid #e2e8f0;
}

.layer-evidence {
  background: #f1f5f9;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  color: #475569;
}

/* 双端矩阵 */
.pill-alert {
  background: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fca5a5;
}

.device-matrix-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0.75rem;
}

.device-chip-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.chip-mobile {
  border-left: 3px solid #0284c7;
}

.chip-pc {
  border-left: 3px solid #64748b;
}

.chip-top {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.device-type-tag {
  font-size: 0.68rem;
  font-weight: 700;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  width: fit-content;
}

.tag-mob { background: #e0f2fe; color: #0369a1; }
.tag-pc { background: #f1f5f9; color: #475569; }

.chip-name {
  font-size: 0.82rem;
  font-weight: 700;
  color: #0f172a;
}

.chip-status {
  margin-top: 0.2rem;
}

.chip-badge {
  font-size: 0.72rem;
  font-weight: 800;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.badge-unindexed {
  background: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fca5a5;
}

.badge-indexed {
  background: #ecfdf5;
  color: #047857;
  border: 1px solid #6ee7b7;
}

.chip-desc {
  font-size: 0.72rem;
  color: #64748b;
  line-height: 1.35;
}

/* 竞品信源穿透表 */
.sources-table-wrap {
  overflow-x: auto;
}

.sources-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
}

.sources-table th {
  background: #f8fafc;
  padding: 0.75rem 0.85rem;
  text-align: left;
  border-bottom: 2px solid #cbd5e1;
  color: #475569;
}

.sources-table td {
  padding: 0.75rem 0.85rem;
  border-bottom: 1px solid #f1f5f9;
}

.src-type-tag {
  background: #f1f5f9;
  color: #475569;
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  font-size: 0.72rem;
}

.comp-source-pill {
  background: #fee2e2;
  color: #991b1b;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  font-size: 0.72rem;
  margin-right: 0.3rem;
  font-weight: 600;
}

.threat-badge {
  font-size: 0.72rem;
  font-weight: 800;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
}

.threat-critical {
  background: #dc2626;
  color: #ffffff;
}

.threat-high {
  background: #ea580c;
  color: #ffffff;
}

.text-danger { color: #dc2626; }
.font-bold { font-weight: 700; }
.text-center { text-align: center; }
.text-indigo { color: #4f46e5; }

/* 经济账本 */
.economic-card {
  background: linear-gradient(180deg, #ffffff, #fffbeb);
  border: 1px solid #fef3c7;
  border-radius: 12px;
  padding: 1.5rem;
}

.pill-money {
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
}

.pill-red-tag {
  background: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fca5a5;
}

.economic-kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.econ-kpi-box {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1.1rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.econ-highlight-box {
  background: #fff1f2;
  border: 2px solid #f87171;
}

.econ-label {
  font-size: 0.78rem;
  color: #64748b;
  font-weight: 700;
}

.econ-val {
  font-size: 1.35rem;
  font-weight: 900;
  line-height: 1.2;
}

.econ-val .unit {
  font-size: 0.75rem;
  font-weight: 600;
  color: #94a3b8;
}

.econ-sub {
  font-size: 0.72rem;
  color: #94a3b8;
}

.text-slate { color: #334155; }
.text-red { color: #b91c1c; }
.text-darkred { color: #7f1d1d; }

.roi-banner {
  background: #0f172a;
  color: #ffffff;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  margin-top: 0.5rem;
}

.roi-badge {
  background: #22c55e;
  color: #0f172a;
  font-size: 0.75rem;
  font-weight: 900;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  display: inline-block;
  margin-bottom: 0.4rem;
}

.roi-pitch {
  font-size: 0.95rem;
  line-height: 1.6;
}

.roi-pitch strong {
  color: #4ade80;
}

.roi-note {
  font-size: 0.72rem;
  color: #94a3b8;
  max-width: 280px;
  line-height: 1.4;
}

/* 实施甘特图 */
.roadmap-timeline {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.timeline-phase-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 1.1rem 1.25rem;
  display: grid;
  grid-template-columns: 140px 1fr;
  gap: 1.5rem;
  align-items: center;
}

.phase-left-col {
  border-right: 2px dashed #e2e8f0;
  padding-right: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.phase-badge {
  background: #4f46e5;
  color: #ffffff;
  font-size: 0.8rem;
  font-weight: 800;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  width: fit-content;
}

.phase-days {
  font-size: 0.95rem;
  font-weight: 800;
  color: #0f172a;
}

.phase-main-col {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.82rem;
  line-height: 1.5;
  color: #334155;
}

.phase-title {
  font-size: 0.98rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 0.2rem;
}

.kpi-text {
  color: #047857;
  font-weight: 700;
}

/* 竞品表 */
.competitor-table-wrap {
  overflow-x: auto;
}

.competitor-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
}

.competitor-table th {
  background: #f8fafc;
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 2px solid #e2e8f0;
  color: #475569;
}

.competitor-table td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #f1f5f9;
}

.comp-name-cell {
  color: #b91c1c;
}

.mention-pill {
  background: #fee2e2;
  color: #991b1b;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  font-weight: 700;
  font-size: 0.75rem;
}

.platform-mini-tag {
  background: #f1f5f9;
  color: #475569;
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  font-size: 0.7rem;
  margin-right: 0.3rem;
}

.comp-adv-cell {
  font-size: 0.8rem;
  color: #64748b;
  line-height: 1.4;
}

.title-with-counter {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.kw-counter-pill {
  background: #ede9fe;
  color: #6366f1;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
  border: 1px solid #c7d2fe;
}

.scenario-groups-wrap {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.scenario-group-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.scenario-header {
  background: linear-gradient(90deg, #f8fafc, #f1f5f9);
  padding: 0.9rem 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #e2e8f0;
}

.scenario-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.scenario-badge {
  background: #0f172a;
  color: #ffffff;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  letter-spacing: 0.03em;
}

.scenario-kw {
  font-size: 0.95rem;
  color: #1e293b;
}

.scenario-kw strong {
  color: #4f46e5;
}

.scenario-status-pill {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 9999px;
}

.status-has-mention {
  background: #ecfdf5;
  color: #047857;
  border: 1px solid #a7f3d0;
}

.status-all-invisible {
  background: #fef2f2;
  color: #b91c1c;
  border: 1px solid #fecaca;
}

.kw-sub-info {
  font-size: 0.75rem;
  color: #64748b;
  margin-left: 0.25rem;
}

/* 折叠手风琴回显 */
.items-accordion {
  padding: 1rem 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.accordion-item {
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  overflow: hidden;
}

.accordion-header {
  background: #f8fafc;
  padding: 0.85rem 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}

.accordion-header:hover {
  background: #f1f5f9;
}

.item-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.platform-badge {
  background: #4f46e5;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.real-api-pill {
  background: linear-gradient(135deg, #0284c7, #2563eb);
  color: #ffffff;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 9999px;
  display: inline-flex;
  align-items: center;
  box-shadow: 0 1px 3px rgba(37, 99, 235, 0.25);
  letter-spacing: 0.02em;
}

.duration-badge {
  font-size: 0.75rem;
  font-weight: 600;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  border: 1px solid #e2e8f0;
}

.plat-deepseek {
  background: #0284c7 !important;
}

.plat-tongyi {
  background: #6366f1 !important;
}

.plat-doubao {
  background: #0ea5e9 !important;
}

.label-deepseek {
  color: #0369a1;
  font-weight: 800;
}

.label-tongyi {
  color: #4f46e5;
  font-weight: 800;
}

.label-doubao {
  color: #0284c7;
  font-weight: 800;
}

.kw-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: #0f172a;
}

.item-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.status-stamp {
  font-size: 0.75rem;
  font-weight: 800;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.stamp-unseen {
  background: #fef2f2;
  border: 1px solid #f87171;
  color: #b91c1c;
}

.stamp-seen {
  background: #ecfdf5;
  border: 1px solid #34d399;
  color: #047857;
}

.arrow-indicator {
  color: #94a3b8;
  font-size: 0.75rem;
}

.accordion-body {
  padding: 1.25rem;
  background: #ffffff;
  border-top: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.box-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: #475569;
  margin-bottom: 0.4rem;
}

.raw-text {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 1rem;
  font-size: 0.82rem;
  line-height: 1.7;
  white-space: pre-wrap;
  color: #334155;
  max-height: 420px;
  overflow-y: auto;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}

.citation-links-list {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  background: #f8fafc;
  padding: 0.75rem;
  border-radius: 6px;
}

.cite-row {
  font-size: 0.75rem;
  display: flex;
  gap: 0.4rem;
  align-items: center;
}

.cite-num { color: #64748b; font-weight: 700; }
.cite-site { color: #4f46e5; font-weight: 600; }
.cite-title { color: #2563eb; text-decoration: none; }

.doubao-citations-badge {
  color: #0284c7;
  font-weight: 800;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.target-brand-row {
  background: #fef2f2 !important;
  border: 1px solid #fca5a5 !important;
  border-radius: 4px;
  padding: 0.35rem 0.6rem !important;
  margin: 0.25rem 0;
}

.target-brand-pill {
  background: #dc2626;
  color: #ffffff;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  margin-left: 0.5rem;
  white-space: nowrap;
}

/* 处方区 */
.prescription-card {
  background: #fdf4ff;
  border: 1px solid #f5d0fe;
  border-radius: 12px;
  padding: 1.5rem;
}

.prescription-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 768px) {
  .prescription-grid {
    grid-template-columns: 1fr;
  }
}

.rx-box {
  background: #ffffff;
  border: 1px solid #f0abfc;
  border-radius: 8px;
  padding: 1rem;
  font-size: 0.8rem;
  line-height: 1.5;
}

.rx-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.rx-scenario {
  font-weight: 800;
  color: #86198f;
  font-size: 0.85rem;
}

.rx-urgency {
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
}

.urgency-red { background: #fee2e2; color: #b91c1c; }
.urgency-blue { background: #e0f2fe; color: #0369a1; }

.rx-action {
  color: #374151;
  margin-bottom: 0.35rem;
}

.rx-expected {
  color: #047857;
}

/* Footer */
.paper-footer {
  border-top: 2px solid #0f172a;
  padding-top: 1.5rem;
}

.contact-card {
  background: #0f172a;
  color: #ffffff;
  border-radius: 8px;
  padding: 1.25rem;
  margin-bottom: 1rem;
}

.contact-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: #a5b4fc;
  margin-bottom: 0.5rem;
}

.contact-details {
  display: flex;
  gap: 1.5rem;
  font-size: 0.85rem;
  flex-wrap: wrap;
}

.statement-box {
  font-size: 0.7rem;
  color: #94a3b8;
  text-align: center;
  line-height: 1.5;
}

.loading-wrap {
  color: #ffffff;
  text-align: center;
  padding: 5rem 0;
  font-size: 1.2rem;
}

/* 打印 A4 媒体样式适配 */
@media print {
  body {
    background: #ffffff !important;
  }
  .no-print {
    display: none !important;
  }
  .report-wrapper {
    background: #ffffff !important;
    padding: 0 !important;
  }
  .paper-container {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 1.2cm 1.5cm !important;
    box-shadow: none !important;
    border-radius: 0 !important;
  }
  .section-card, .timeline-phase-card, .scenario-group-card, .economic-card {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .accordion-body {
    display: block !important;
  }
  .arrow-indicator {
    display: none !important;
  }
}
</style>
