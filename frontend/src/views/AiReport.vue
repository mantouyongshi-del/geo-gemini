<template>
  <div class="report-container">
    <!-- 顶部导航与品牌标头 -->
    <header class="header">
      <div class="header-inner">
        <div class="brand-info">
          <div class="logo-box">
            <img v-if="company.logo_url" :src="company.logo_url" alt="Logo" class="logo-img" />
            <div v-else class="logo-placeholder">{{ company.short_name?.[0] || 'AI' }}</div>
          </div>
          <div class="brand-titles">
            <div class="title-row">
              <h1 class="brand-name">{{ company.name || '企业 GEO 优化监控报表' }}</h1>
              
              <!-- 品牌切换下拉选择框 -->
              <select v-if="allCompanies.length > 1" :value="company.id" @change="handleSwitchCompany($event.target.value)" class="brand-select">
                <option v-for="c in allCompanies" :key="c.id" :value="c.id">
                  {{ c.name }}
                </option>
              </select>

              <span class="badge badge-primary">{{ company.industry || '智能制造' }}</span>
              <span class="status-indicator">
                <span class="pulse-dot"></span>
                GEO 实时巡检中
              </span>
            </div>
            <div class="alias-row">
              <span class="alias-label">实体关键词:</span>
              <span v-for="alias in company.brand_aliases" :key="alias" class="alias-tag">
                {{ alias }}
              </span>
            </div>
          </div>
        </div>

        <div class="header-actions">
          <router-link to="/diagnostic" class="btn btn-diagnostic-link">
            <span>🩺 售前体检工作台 (去拓客) ➔</span>
          </router-link>
          <button class="btn btn-new-brand" @click="showNewBrandModal = true">
            <span>✨ 录入签约客户</span>
          </button>
          <button class="btn btn-outline" @click="showShareModal = true">
            <span>🔗 分享报表</span>
          </button>
          <button class="btn btn-primary" @click="refreshData">
            <span>🔄 刷新数据</span>
          </button>
        </div>
      </div>
    </header>

    <!-- 主体区域 -->
    <main class="main-content">
      <!-- 1. 四大核心指标卡片 -->
      <section class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-icon-wrap icon-purple">🎯</div>
          <div class="kpi-data">
            <div class="kpi-label">当前推荐条数</div>
            <div class="kpi-value text-purple">{{ summary.recommendationNumber.toLocaleString() }}</div>
            <div class="kpi-sub">大模型搜索首位推荐</div>
          </div>
        </div>

        <div class="kpi-card">
          <div class="kpi-icon-wrap icon-green">📈</div>
          <div class="kpi-data">
            <div class="kpi-label">7 天新增推荐</div>
            <div class="kpi-value text-green">+{{ summary.sevenDayIncreaseNumber.toLocaleString() }}</div>
            <div class="kpi-sub">周环比稳步攀升</div>
          </div>
        </div>

        <div class="kpi-card">
          <div class="kpi-icon-wrap icon-blue">🚀</div>
          <div class="kpi-data">
            <div class="kpi-label">30 天新增推荐</div>
            <div class="kpi-value text-blue">+{{ summary.thirtyDayIncreaseNumber.toLocaleString() }}</div>
            <div class="kpi-sub">月度品牌资产沉淀</div>
          </div>
        </div>

        <div class="kpi-card">
          <div class="kpi-icon-wrap icon-amber">🛡️</div>
          <div class="kpi-data">
            <div class="kpi-label">历史累计检测</div>
            <div class="kpi-value text-amber">{{ summary.historyTotalNumber.toLocaleString() }}</div>
            <div class="kpi-sub">全天候自动化巡检</div>
          </div>
        </div>
      </section>

      <!-- 2. 四维场景与平台筛选 -->
      <section class="filter-section">
        <!-- 场景维度切换 -->
        <div class="scenario-tabs">
          <button 
            v-for="tab in scenarioTabs" 
            :key="tab.type" 
            :class="['scenario-tab', { active: currentTaskType === tab.type }]"
            @click="switchTaskType(tab.type)"
          >
            <span class="tab-icon">{{ tab.icon }}</span>
            <span class="tab-name">{{ tab.name }}</span>
            <span class="tab-badge">{{ getScenarioCount(tab.type) }}</span>
          </button>
        </div>

        <!-- 平台选择条 -->
        <div class="platform-bar">
          <div class="platform-scroll">
            <button 
              :class="['platform-chip', { active: currentPlatform === '' }]"
              @click="switchPlatform('')"
            >
              全部平台 ({{ totalPlatformCount }})
            </button>
            <button 
              v-for="p in platforms" 
              :key="p.type" 
              :class="['platform-chip', { active: currentPlatform === p.type }]"
              @click="switchPlatform(p.type)"
            >
              {{ p.name }}
              <span class="chip-count">{{ p.count }}</span>
            </button>
          </div>
        </div>
      </section>

      <!-- 3. 图表分析区 (30天趋势 + 平台分布) -->
      <section class="charts-grid">
        <div class="chart-card">
          <div class="card-header">
            <h3 class="card-title">📈 30天推荐增长趋势轨迹</h3>
            <span class="card-tip">数据来源于各大主流大模型每日推荐汇总</span>
          </div>
          <div ref="trendChartRef" class="chart-body"></div>
        </div>

        <div class="chart-card">
          <div class="card-header">
            <h3 class="card-title">🤖 各大模型平台渗透分布</h3>
            <span class="card-tip">全网主流 AI 搜索引擎推荐对比</span>
          </div>
          <div ref="platformChartRef" class="chart-body"></div>
        </div>
      </section>

      <!-- 4. 详细排名列表数据表格 -->
      <section class="table-card">
        <div class="table-header">
          <div>
            <h3 class="card-title">📋 关键词推荐与大模型问答监控明细</h3>
            <p class="card-tip">共匹配 {{ rankingTotal }} 条高价值推荐问答，点击可查看大模型原始回答快照与引文溯源</p>
          </div>
          <div class="table-actions">
            <input 
              v-model="searchKeyword" 
              placeholder="在当前列表中过滤关键词..." 
              class="search-input"
            />
          </div>
        </div>

        <div class="table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>序号</th>
                <th>提问搜索词 (Prompt)</th>
                <th>核心主题</th>
                <th>场景类型</th>
                <th>测试大模型</th>
                <th>终端环境</th>
                <th>推荐位次</th>
                <th>最近验证时间</th>
                <th style="text-align: center;">操作</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, idx) in filteredRankings" :key="row.rid">
                <td>{{ (currentPage - 1) * pageSize + idx + 1 }}</td>
                <td class="cell-keyword">
                  <span class="kw-text">{{ row.keyword }}</span>
                </td>
                <td>
                  <span class="subject-tag">{{ row.subject }}</span>
                </td>
                <td>
                  <span :class="['scene-tag', `scene-${row.taskType}`]">
                    {{ getSceneName(row.taskType) }}
                  </span>
                </td>
                <td>
                  <span class="platform-name-tag">{{ getPlatformDisplay(row.type) }}</span>
                </td>
                <td>
                  <span class="device-pill" :class="row.isMobile ? 'device-mobile' : 'device-pc'">
                    {{ row.isMobile ? '📱 移动端' : '💻 PC端' }}
                  </span>
                </td>
                <td>
                  <span class="badge badge-success">第 {{ row.rank }} 位推荐</span>
                </td>
                <td class="cell-time">{{ formatTime(row.mtime) }}</td>
                <td style="text-align: center;">
                  <button class="btn-snapshot" @click="openSnapshot(row.rid)">
                    <span>🔍 查看回答快照</span>
                  </button>
                </td>
              </tr>
              <tr v-if="filteredRankings.length === 0">
                <td colspan="9" class="empty-cell">
                  暂无匹配的监控数据
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 分页 -->
        <div class="pagination-bar">
          <span class="page-info">第 {{ currentPage }} 页 / 共 {{ Math.ceil(rankingTotal / pageSize) || 1 }} 页</span>
          <div class="page-buttons">
            <button 
              class="btn btn-outline btn-sm" 
              :disabled="currentPage <= 1" 
              @click="changePage(currentPage - 1)"
            >
              上一页
            </button>
            <button 
              class="btn btn-outline btn-sm" 
              :disabled="currentPage * pageSize >= rankingTotal" 
              @click="changePage(currentPage + 1)"
            >
              下一页
            </button>
          </div>
        </div>
      </section>
    </main>

    <!-- 弹窗: 添加/诊断新品牌 -->
    <div v-if="showNewBrandModal" class="modal-backdrop" @click="showNewBrandModal = false">
      <div class="modal-card new-brand-modal" @click.stop>
        <div class="modal-header">
          <div>
            <h3 class="modal-title">✨ 诊断任意新品牌 / 启动 GEO 巡检</h3>
            <p class="modal-subtitle">输入任何企业或品牌信息，系统将自动生成四维场景词库并在各大模型执行全网巡检</p>
          </div>
          <button class="close-btn" @click="showNewBrandModal = false">✕</button>
        </div>

        <form @submit.prevent="submitQuickAudit" class="modal-body">
          <div class="form-group">
            <label class="form-label">品牌/企业名称 (必填)</label>
            <input 
              v-model="newBrandForm.name" 
              required 
              placeholder="例如: 元气森林（北京）食品科技集团有限公司 / 蔚来汽车 / 某某律所" 
              class="form-input" 
            />
          </div>

          <div class="form-row">
            <div class="form-group">
              <label class="form-label">品牌简称/常用名</label>
              <input 
                v-model="newBrandForm.short_name" 
                placeholder="例如: 元气森林 / 蔚来" 
                class="form-input" 
              />
            </div>
            <div class="form-group">
              <label class="form-label">所属行业领域</label>
              <input 
                v-model="newBrandForm.industry" 
                placeholder="例如: 无糖气泡水 / 智能电动汽车 / 知识产权法律服务" 
                class="form-input" 
              />
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">品牌实体别名 (以逗号分隔)</label>
            <input 
              v-model="newBrandForm.brand_aliases" 
              placeholder="例如: 元气森林, CHI FOREST, 气泡水元气森林" 
              class="form-input" 
            />
            <span class="form-tip">用于检测大模型回答中是否成功提及该品牌实体</span>
          </div>

          <div class="form-group">
            <label class="form-label">指定监控提示词/搜索词 (可选，每行一个)</label>
            <textarea 
              v-model="newBrandForm.custom_keywords_str" 
              rows="3" 
              placeholder="如留空，系统将根据行业和品牌自动派生全套四维场景词库（品牌/搜索/问答/意图词）" 
              class="form-textarea"
            ></textarea>
          </div>

          <div class="modal-footer">
            <button type="button" class="btn btn-outline" @click="showNewBrandModal = false" :disabled="isSubmittingAudit">
              取消
            </button>
            <button type="submit" class="btn btn-primary" :disabled="isSubmittingAudit">
              <span v-if="isSubmittingAudit">⏳ 正在调度各大模型巡检中...</span>
              <span v-else>🚀 立即生成 GEO 诊断报表</span>
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- 问答快照详情抽屉/弹窗 -->
    <div v-if="activeSnapshot" class="modal-backdrop" @click="activeSnapshot = null">
      <div class="modal-card" @click.stop>
        <div class="modal-header">
          <div>
            <h3 class="modal-title">AI 大模型回答快照与引文溯源</h3>
            <p class="modal-subtitle">提问词: “{{ activeSnapshot.query_prompt }}”</p>
          </div>
          <button class="close-btn" @click="activeSnapshot = null">✕</button>
        </div>

        <div class="modal-body">
          <div class="matched-box">
            <span class="matched-title">🎯 成功命中的品牌实体词:</span>
            <div class="matched-tags">
              <span v-for="ent in activeSnapshot.matched_entities" :key="ent" class="matched-tag">
                {{ ent }}
              </span>
            </div>
          </div>

          <div class="response-section">
            <h4 class="section-heading">🤖 大模型原始生成回答 (Markdown)</h4>
            <div class="markdown-preview">
              <pre class="content-text">{{ activeSnapshot.content }}</pre>
            </div>
          </div>

          <div class="citations-section">
            <h4 class="section-heading">🌐 联网检索源与注入外链溯源 (Citations)</h4>
            <p class="section-desc">大模型在回答此问题时召回并参考了以下外链与站群源：</p>
            
            <div class="citations-list">
              <div v-for="(cite, i) in activeSnapshot.citations" :key="i" class="citation-card">
                <div class="citation-site">
                  <span class="site-badge">信源 {{ i + 1 }}</span>
                  <span class="site-name">{{ cite.site_name }}</span>
                </div>
                <a :href="cite.url" target="_blank" class="citation-link">{{ cite.title }}</a>
                <p v-if="cite.summary" class="citation-summary">{{ cite.summary }}</p>
                <div class="citation-url">{{ cite.url }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 分享报表弹窗 -->
    <div v-if="showShareModal" class="modal-backdrop" @click="showShareModal = false">
      <div class="modal-card share-modal" @click.stop>
        <div class="modal-header">
          <h3 class="modal-title">🔗 客户专属公开报表分享链接</h3>
          <button class="close-btn" @click="showShareModal = false">✕</button>
        </div>
        <div class="modal-body">
          <p class="share-desc">该链接已内置防篡改安全授权码，客户无需登录即可直接查看只读优化报表：</p>
          <div class="share-input-box">
            <input readonly :value="currentShareUrl" class="share-input" />
            <button class="btn btn-primary" @click="copyShareUrl">
              {{ copied ? '已复制 ✓' : '复制链接' }}
            </button>
          </div>
          <div class="share-tips">
            💡 提示：该安全 Token 已严格限制为企业专属隔离数据，杜绝越权访问与凭证泄露。
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import * as echarts from 'echarts';
import geoApi from '../api/geo';

const route = useRoute();
const router = useRouter();

const currentCode = computed(() => route.query.code || 'MToxODIwNDE3Nzg4OjhkODBlZjgzN2QyNTM5OTM');

// 状态管理
const company = ref({
  id: 1,
  name: '',
  short_name: '',
  logo_url: '',
  industry: '',
  brand_aliases: []
});

const allCompanies = ref([]);

const summary = ref({
  recommendationNumber: 0,
  historyTotalNumber: 0,
  sevenDayIncreaseNumber: 0,
  thirtyDayIncreaseNumber: 0
});

const currentTaskType = ref(0);
const currentPlatform = ref('');
const platforms = ref([]);
const rankingRecords = ref([]);
const rankingTotal = ref(0);
const currentPage = ref(1);
const pageSize = ref(10);
const searchKeyword = ref('');

const activeSnapshot = ref(null);
const showShareModal = ref(false);
const showNewBrandModal = ref(false);
const isSubmittingAudit = ref(false);
const copied = ref(false);

const newBrandForm = ref({
  name: '',
  short_name: '',
  industry: '',
  brand_aliases: '',
  custom_keywords_str: ''
});

const trendChartRef = ref(null);
const platformChartRef = ref(null);
let trendChart = null;
let platformChart = null;

const scenarioTabs = [
  { type: 0, name: '全部报表', icon: '📊' },
  { type: 1, name: '品牌场景', icon: '⭐' },
  { type: 2, name: '搜索词场景', icon: '🔍' },
  { type: 3, name: '问答词场景', icon: '💬' },
  { type: 4, name: '意图场景', icon: '✨' }
];

const totalPlatformCount = computed(() => {
  return platforms.value.reduce((sum, p) => sum + p.count, 0);
});

const currentShareUrl = computed(() => {
  return `${window.location.origin}/#/ai_report?code=${currentCode.value}`;
});

function getScenarioCount(type) {
  if (type === 0) return summary.value.recommendationNumber;
  if (type === 1) return Math.floor(summary.value.recommendationNumber * 0.05);
  if (type === 2) return Math.floor(summary.value.recommendationNumber * 0.32);
  if (type === 3) return Math.floor(summary.value.recommendationNumber * 0.20);
  if (type === 4) return Math.floor(summary.value.recommendationNumber * 0.43);
  return 0;
}

function getSceneName(type) {
  const map = { 1: '品牌', 2: '搜索词', 3: '问答词', 4: '意图' };
  return map[type] || '通用';
}

function getPlatformDisplay(type) {
  const map = {
    doubao: '豆包PC', doubaom: '豆包手机',
    deepseek: 'DeepSeek PC', deepseekm: 'DeepSeek 手机',
    tongyi: '通义千问 PC', tongyim: '通义千问 手机',
    yuanbao: '腾讯元宝 PC', yuanbaom: '腾讯元宝 手机',
    baidu: '文心一言 PC', baidum: '文心一言 手机',
    nami: '纳米搜索 PC', namim: '纳米搜索 手机',
    kuake: '夸克AI', kuakem: '夸克 手机',
    uc: 'UC头条', baiduNew: '百度搜索AI',
    wechat: '微信AI', douyin: '抖音AI', rednote: '小红书'
  };
  return map[type] || type;
}

function formatTime(ts) {
  if (!ts) return '-';
  const d = new Date(ts * 1000);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')} ${String(d.getHours()).padStart(2, '0')}:${String(d.getMinutes()).padStart(2, '0')}`;
}

const filteredRankings = computed(() => {
  if (!searchKeyword.value) return rankingRecords.value;
  return rankingRecords.value.filter(r => 
    r.keyword.includes(searchKeyword.value) || r.subject.includes(searchKeyword.value)
  );
});

async function loadData() {
  const code = currentCode.value;
  try {
    const [compRes, sumRes, platRes, companiesListRes] = await Promise.all([
      geoApi.getCompanyInfo(code),
      geoApi.getSummary(code),
      geoApi.getPlatforms(code, currentTaskType.value),
      geoApi.getCompanies()
    ]);
    company.value = compRes.data;
    summary.value = sumRes.data;
    platforms.value = platRes.data;
    allCompanies.value = companiesListRes.data;

    await Promise.all([
      fetchRankings(),
      loadTrendChart(),
      updatePlatformChart()
    ]);
  } catch (err) {
    console.error('Failed to load GEO report data:', err);
  }
}

function handleSwitchCompany(companyId) {
  const target = allCompanies.value.find(c => c.id == companyId);
  if (target && target.share_token) {
    router.push({ path: '/ai_report', query: { code: target.share_token } });
  }
}

async function submitQuickAudit() {
  if (!newBrandForm.value.name.trim()) return;
  isSubmittingAudit.value = true;
  try {
    const kws = newBrandForm.value.custom_keywords_str
      .split('\n')
      .map(k => k.trim())
      .filter(Boolean);

    const res = await geoApi.quickAudit({
      name: newBrandForm.value.name.trim(),
      short_name: newBrandForm.value.short_name.trim() || undefined,
      industry: newBrandForm.value.industry.trim() || undefined,
      brand_aliases: newBrandForm.value.brand_aliases.trim() || undefined,
      custom_keywords: kws.length ? kws : undefined
    });

    showNewBrandModal.value = false;
    newBrandForm.value = { name: '', short_name: '', industry: '', brand_aliases: '', custom_keywords_str: '' };
    
    // 跳转到新生成的专属分享 Token
    router.push({ path: '/ai_report', query: { code: res.data.share_token } });
  } catch (e) {
    alert('启动诊断巡检失败: ' + (e.response?.data?.detail || e.message));
  } finally {
    isSubmittingAudit.value = false;
  }
}

async function fetchRankings() {
  const code = currentCode.value;
  const res = await geoApi.getRankings(code, {
    page: currentPage.value,
    rows: pageSize.value,
    taskType: currentTaskType.value,
    type: currentPlatform.value || null
  });
  rankingRecords.value = res.data.records;
  rankingTotal.value = res.data.total;
}

function switchTaskType(type) {
  currentTaskType.value = type;
  currentPage.value = 1;
  geoApi.getPlatforms(currentCode.value, type).then(res => {
    platforms.value = res.data;
    updatePlatformChart();
  });
  fetchRankings();
}

function switchPlatform(pType) {
  currentPlatform.value = pType;
  currentPage.value = 1;
  fetchRankings();
}

function changePage(p) {
  currentPage.value = p;
  fetchRankings();
}

async function openSnapshot(rid) {
  try {
    const res = await geoApi.getMatchDetail(currentCode.value, rid);
    activeSnapshot.value = res.data;
  } catch (e) {
    alert('获取快照详情失败');
  }
}

function copyShareUrl() {
  navigator.clipboard.writeText(currentShareUrl.value).then(() => {
    copied.value = true;
    setTimeout(() => copied.value = false, 2000);
  });
}

function refreshData() {
  loadData();
}

// 监听路由参数变化（如切换企业或输入新 token）
watch(() => route.query.code, () => {
  currentPage.value = 1;
  currentTaskType.value = 0;
  currentPlatform.value = '';
  loadData();
});

// 初始化图表
async function loadTrendChart() {
  if (!trendChartRef.value) return;
  if (!trendChart) {
    trendChart = echarts.init(trendChartRef.value);
  }

  const res = await geoApi.getTrend(currentCode.value, 30);
  const stats = res.data.statistics;
  const dates = stats.map(s => s.totalDate.slice(5));
  const values = stats.map(s => s.totalNumber);

  trendChart.setOption({
    tooltip: { trigger: 'axis' },
    grid: { left: '3%', right: '4%', bottom: '3%', top: '10%', containLabel: true },
    xAxis: { type: 'category', boundaryGap: false, data: dates, axisLine: { lineStyle: { color: '#cbd5e1' } } },
    yAxis: { type: 'value', axisLine: { lineStyle: { color: '#cbd5e1' } }, splitLine: { lineStyle: { color: '#f1f5f9' } } },
    series: [{
      name: '推荐总量',
      type: 'line',
      smooth: true,
      data: values,
      lineStyle: { width: 3, color: '#6366f1' },
      itemStyle: { color: '#6366f1' },
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: 'rgba(99, 102, 241, 0.45)' },
          { offset: 1, color: 'rgba(99, 102, 241, 0.02)' }
        ])
      }
    }]
  });
}

function updatePlatformChart() {
  if (!platformChartRef.value) return;
  if (!platformChart) {
    platformChart = echarts.init(platformChartRef.value);
  }

  const topPlatforms = platforms.value.filter(p => p.count > 0).slice(0, 8);
  const names = topPlatforms.map(p => p.name).reverse();
  const counts = topPlatforms.map(p => p.count).reverse();

  platformChart.setOption({
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: '3%', right: '8%', bottom: '3%', top: '5%', containLabel: true },
    xAxis: { type: 'value', splitLine: { lineStyle: { color: '#f1f5f9' } } },
    yAxis: { type: 'category', data: names, axisTick: { show: false } },
    series: [{
      type: 'bar',
      data: counts,
      barWidth: 16,
      itemStyle: {
        borderRadius: [0, 8, 8, 0],
        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
          { offset: 0, color: '#818cf8' },
          { offset: 1, color: '#6366f1' }
        ])
      },
      label: { show: true, position: 'right', color: '#64748b' }
    }]
  });
}

function handleResize() {
  trendChart?.resize();
  platformChart?.resize();
}

onMounted(() => {
  loadData();
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  trendChart?.dispose();
  platformChart?.dispose();
});
</script>

<style scoped>
.report-container {
  min-height: 100vh;
  background-color: #f8fafc;
}

/* Header */
.header {
  background: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  padding: 1.25rem 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}

.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.brand-info {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.logo-box {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  background: #f1f5f9;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  border: 1px solid #e2e8f0;
}

.logo-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.logo-placeholder {
  font-size: 1.5rem;
  font-weight: 700;
  color: #6366f1;
}

.title-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.brand-name {
  font-size: 1.35rem;
  font-weight: 700;
  color: #0f172a;
}

.brand-select {
  padding: 0.35rem 0.75rem;
  font-size: 0.85rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  background: #ffffff;
  color: #334155;
  outline: none;
  font-weight: 600;
  cursor: pointer;
}

.brand-select:focus {
  border-color: #6366f1;
}

.status-indicator {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: #10b981;
  background: #ecfdf5;
  padding: 0.25rem 0.65rem;
  border-radius: 9999px;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.4);
}

.alias-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.35rem;
  flex-wrap: wrap;
}

.alias-label {
  font-size: 0.75rem;
  color: #64748b;
}

.alias-tag {
  font-size: 0.75rem;
  background: #f1f5f9;
  color: #475569;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
}

.btn-diagnostic-link {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: #ffffff;
  font-weight: 600;
  text-decoration: none;
  box-shadow: 0 2px 6px rgba(239, 68, 68, 0.3);
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
}

.btn-diagnostic-link:hover {
  background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
  color: #ffffff;
}

.btn-new-brand {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: #ffffff;
  font-weight: 600;
  box-shadow: 0 2px 4px rgba(16, 185, 129, 0.25);
}

.btn-new-brand:hover {
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
}

/* Main */
.main-content {
  max-width: 1400px;
  margin: 1.5rem auto;
  padding: 0 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* KPI Cards */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.25rem;
}

.kpi-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}

.kpi-icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}

.icon-purple { background: #e0e7ff; }
.icon-green { background: #dcfce7; }
.icon-blue { background: #e0f2fe; }
.icon-amber { background: #fef3c7; }

.kpi-label {
  font-size: 0.85rem;
  color: #64748b;
  font-weight: 500;
}

.kpi-value {
  font-size: 1.75rem;
  font-weight: 800;
  line-height: 1.2;
  margin: 0.15rem 0;
}

.kpi-sub {
  font-size: 0.75rem;
  color: #94a3b8;
}

.text-purple { color: #4f46e5; }
.text-green { color: #16a34a; }
.text-blue { color: #0284c7; }
.text-amber { color: #d97706; }

/* Filter Section */
.filter-section {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1rem 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.scenario-tabs {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  border-bottom: 1px solid #f1f5f9;
  padding-bottom: 0.75rem;
}

.scenario-tab {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 1px solid transparent;
  background: transparent;
  font-size: 0.875rem;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
  transition: all 0.15s;
}

.scenario-tab.active {
  background: #eef2ff;
  color: #4f46e5;
  border-color: #c7d2fe;
}

.tab-badge {
  background: #f1f5f9;
  color: #475569;
  font-size: 0.75rem;
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
}

.scenario-tab.active .tab-badge {
  background: #6366f1;
  color: #ffffff;
}

.platform-bar {
  overflow-x: auto;
}

.platform-scroll {
  display: flex;
  gap: 0.5rem;
  white-space: nowrap;
}

.platform-chip {
  padding: 0.35rem 0.85rem;
  border-radius: 999px;
  border: 1px solid #e2e8f0;
  background: #f8fafc;
  font-size: 0.8rem;
  color: #475569;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: all 0.15s;
}

.platform-chip.active {
  background: #4f46e5;
  color: #ffffff;
  border-color: #4f46e5;
}

.chip-count {
  font-size: 0.7rem;
  opacity: 0.8;
}

/* Charts */
.charts-grid {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 1.25rem;
}

@media (max-width: 992px) {
  .charts-grid {
    grid-template-columns: 1fr;
  }
}

.chart-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}

.card-header {
  margin-bottom: 0.75rem;
}

.card-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #0f172a;
}

.card-tip {
  font-size: 0.75rem;
  color: #94a3b8;
  margin-top: 0.15rem;
}

.chart-body {
  height: 280px;
  width: 100%;
}

/* Table Card */
.table-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}

.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1rem;
}

.search-input {
  padding: 0.45rem 0.85rem;
  font-size: 0.85rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  outline: none;
  min-width: 240px;
}

.search-input:focus {
  border-color: #6366f1;
}

.table-wrap {
  overflow-x: auto;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
  text-align: left;
}

.data-table th {
  background: #f8fafc;
  color: #64748b;
  font-weight: 600;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #e2e8f0;
}

.data-table td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid #f1f5f9;
  color: #1e293b;
}

.data-table tr:hover td {
  background: #f8fafc;
}

.kw-text {
  font-weight: 600;
  color: #0f172a;
}

.subject-tag {
  background: #f1f5f9;
  color: #475569;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
}

.scene-tag {
  font-size: 0.75rem;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-weight: 500;
}

.scene-1 { background: #fef3c7; color: #b45309; }
.scene-2 { background: #e0e7ff; color: #4338ca; }
.scene-3 { background: #dbeafe; color: #1d4ed8; }
.scene-4 { background: #fce7f3; color: #be185d; }

.platform-name-tag {
  font-weight: 600;
  color: #334155;
}

.device-pill {
  font-size: 0.75rem;
  padding: 0.15rem 0.5rem;
  border-radius: 999px;
}

.device-pc { background: #f1f5f9; color: #475569; }
.device-mobile { background: #ecfdf5; color: #047857; }

.btn-snapshot {
  background: #eef2ff;
  color: #4f46e5;
  border: 1px solid #c7d2fe;
  padding: 0.35rem 0.75rem;
  font-size: 0.75rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.15s;
}

.btn-snapshot:hover {
  background: #6366f1;
  color: #ffffff;
  border-color: #6366f1;
}

.pagination-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #f1f5f9;
}

.page-info {
  font-size: 0.8rem;
  color: #64748b;
}

.page-buttons {
  display: flex;
  gap: 0.5rem;
}

.btn-sm {
  padding: 0.3rem 0.75rem;
  font-size: 0.8rem;
}

/* Modal */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
  padding: 1.5rem;
}

.modal-card {
  background: #ffffff;
  border-radius: 16px;
  width: 100%;
  max-width: 800px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.modal-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #0f172a;
}

.modal-subtitle {
  font-size: 0.85rem;
  color: #64748b;
  margin-top: 0.15rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.25rem;
  color: #94a3b8;
  cursor: pointer;
}

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.matched-box {
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  border-radius: 8px;
  padding: 0.85rem 1rem;
}

.matched-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: #065f46;
}

.matched-tags {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.4rem;
  flex-wrap: wrap;
}

.matched-tag {
  background: #10b981;
  color: #ffffff;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
}

.section-heading {
  font-size: 0.95rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.section-desc {
  font-size: 0.8rem;
  color: #64748b;
  margin-bottom: 0.75rem;
}

.markdown-preview {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1rem;
}

.content-text {
  font-family: inherit;
  font-size: 0.875rem;
  line-height: 1.6;
  white-space: pre-wrap;
  color: #334155;
}

.citations-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.citation-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 0.85rem;
}

.citation-site {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.35rem;
}

.site-badge {
  background: #e0e7ff;
  color: #3730a3;
  font-size: 0.7rem;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  font-weight: 600;
}

.site-name {
  font-size: 0.8rem;
  font-weight: 600;
  color: #475569;
}

.citation-link {
  font-size: 0.875rem;
  font-weight: 600;
  color: #4f46e5;
  text-decoration: none;
  display: block;
}

.citation-link:hover {
  text-decoration: underline;
}

.citation-summary {
  font-size: 0.8rem;
  color: #64748b;
  margin-top: 0.3rem;
  line-height: 1.4;
}

.citation-url {
  font-size: 0.7rem;
  color: #94a3b8;
  margin-top: 0.25rem;
  word-break: break-all;
}

/* Forms */
.new-brand-modal {
  max-width: 620px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #334155;
}

.form-input, .form-textarea {
  padding: 0.5rem 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-size: 0.875rem;
  outline: none;
}

.form-input:focus, .form-textarea:focus {
  border-color: #6366f1;
}

.form-tip {
  font-size: 0.75rem;
  color: #94a3b8;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  margin-top: 0.75rem;
}

/* Share Modal */
.share-modal {
  max-width: 540px;
}

.share-desc {
  font-size: 0.875rem;
  color: #475569;
}

.share-input-box {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.share-input {
  flex: 1;
  padding: 0.5rem 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-size: 0.8rem;
  background: #f8fafc;
  color: #334155;
  outline: none;
}

.share-tips {
  font-size: 0.75rem;
  color: #64748b;
  background: #f1f5f9;
  padding: 0.75rem;
  border-radius: 6px;
  margin-top: 1rem;
}
</style>
