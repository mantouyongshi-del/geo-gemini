<template>
  <div class="console-container">
    <!-- 头部品牌条 -->
    <header class="console-header">
      <div class="header-inner">
        <div class="brand-badge">
          <img src="/logo-white.png" alt="蜉蝣小宝" class="brand-logo-img" />
          <span class="brand-tag">全国企业智能营销云 · 售前拓客引擎</span>
          <span class="live-status-pill">🟢 官方五大引擎直连在线</span>
        </div>
        <div class="header-nav">
          <router-link to="/ai_report" class="nav-link">📊 客户报表看板</router-link>
          <router-link to="/diagnostic" class="nav-link active">🎯 准客户 AI 可见度体检</router-link>
        </div>
      </div>
    </header>

    <main class="console-main">
      <!-- 权威公信力 Hero 区域 -->
      <div class="hero-section">
        <div class="hero-pill-tag">⚡ 2026 企业级 GEO 智能搜索引擎优化与攻防巡检系统</div>
        <h1 class="hero-title">企业 AI 搜索引擎可见度 · 售前全网诊断工作台</h1>
        <p class="hero-sub">
          现场直连 <strong>字节跳动豆包 · 深度求索DeepSeek · 阿里通义千问 · 腾讯元宝 · 百度智能搜索</strong>，出具穿透级《企业 AI 可见度体检报告》，用铁证向老板证明“潜在客户已被同行截流”！
        </p>

        <!-- 官方大模型品牌矩阵徽章墙 -->
        <div class="model-wall">
          <div class="model-badge badge-doubao">
            <span class="m-icon">⚡</span>
            <div class="m-info">
              <span class="m-name">字节跳动 · 豆包</span>
              <span class="m-desc">火山引擎方舟直连 · 抖音生态</span>
            </div>
          </div>
          <div class="model-badge badge-deepseek">
            <span class="m-icon">🧠</span>
            <div class="m-info">
              <span class="m-name">深度求索 · DeepSeek</span>
              <span class="m-desc">官方开放平台 · 深度推理链</span>
            </div>
          </div>
          <div class="model-badge badge-tongyi">
            <span class="m-icon">🌐</span>
            <div class="m-info">
              <span class="m-name">阿里巴巴 · 通义千问</span>
              <span class="m-desc">百炼原生全网检索 · B2B</span>
            </div>
          </div>
          <div class="model-badge badge-yuanbao">
            <span class="m-icon">💬</span>
            <div class="m-info">
              <span class="m-name">腾讯科技 · 腾讯元宝</span>
              <span class="m-desc">混元内核 · 微信公众号生态</span>
            </div>
          </div>
          <div class="model-badge badge-baidu">
            <span class="m-icon">🔍</span>
            <div class="m-info">
              <span class="m-name">百度智能 · 百度搜索</span>
              <span class="m-desc">知识图谱 · 权威词条收录</span>
            </div>
          </div>
        </div>

        <!-- 平台公信力指标条 -->
        <div class="trust-stats-row">
          <div class="trust-stat-item">
            <div class="ts-num">5 大</div>
            <div class="ts-label">主流 AI 搜索真机直连</div>
          </div>
          <div class="trust-stat-divider"></div>
          <div class="trust-stat-item">
            <div class="ts-num">100%</div>
            <div class="ts-label">双端(PC/移动)真机穿透</div>
          </div>
          <div class="trust-stat-divider"></div>
          <div class="trust-stat-item">
            <div class="ts-num">2,840+</div>
            <div class="ts-label">实体企业已出具体检书</div>
          </div>
          <div class="trust-stat-divider"></div>
          <div class="trust-stat-item">
            <div class="ts-num">98.6%</div>
            <div class="ts-label">同行隐形截流实体识别率</div>
          </div>
        </div>
      </div>

      <div class="content-grid">
        <!-- 左侧: 诊断输入表单 -->
        <div class="card form-card">
          <div class="card-header-row">
            <h2 class="card-title">📝 录入准客户信息</h2>
            <span class="card-tip-pill">快速出具体检单 · 现场打脸促单</span>
          </div>

          <form @submit.prevent="handleStartDiagnostic">
            <div class="form-group">
              <label class="form-label">准客户工商全称 (必填)</label>
              <input 
                v-model="form.target_company" 
                required 
                placeholder="例如: 杭州某某医疗美容门诊部 / 嘉兴市恒达门窗工程有限公司" 
                class="form-input" 
              />
            </div>

            <div class="form-row">
              <div class="form-group">
                <label class="form-label">品牌简称/常用名 (必填)</label>
                <input 
                  v-model="form.brand_name" 
                  required 
                  placeholder="例如: 恒达门窗 / 臻美医美" 
                  class="form-input" 
                />
              </div>
              <div class="form-group">
                <label class="form-label">所属行业领域 (必填)</label>
                <input 
                  v-model="form.industry" 
                  required 
                  placeholder="例如: 教育培训少儿科创 / 定制门窗" 
                  class="form-input" 
                />
              </div>
              <div class="form-group">
                <label class="form-label">展业城市/地区</label>
                <input 
                  v-model="form.city" 
                  placeholder="例如: 怀化 / 杭州 / 嘉兴" 
                  class="form-input" 
                />
              </div>
            </div>

            <!-- 快捷行业词模版 -->
            <div class="preset-templates">
              <span class="preset-label">实测案例快速填入:</span>
              <button 
                type="button" 
                v-for="tpl in industryTemplates" 
                :key="tpl.name" 
                class="preset-btn"
                @click="applyTemplate(tpl)"
              >
                {{ tpl.name }}
              </button>
            </div>

            <!-- 核心测试词输入区 + 智能生成按钮 -->
            <div class="form-group">
              <div class="form-label-row">
                <label class="form-label">核心测试搜索词 (提示词，每行一个)</label>
                <button 
                  type="button" 
                  class="btn-smart-gen" 
                  @click="generateSmartKeywords"
                  :disabled="isGeneratingKws"
                >
                  <span v-if="isGeneratingKws">✨ 正在智能联想截流词...</span>
                  <span v-else>✨ 一键生成行业高频截流词</span>
                </button>
              </div>
              <textarea 
                v-model="keywordsStr" 
                rows="4" 
                required
                placeholder="例如:&#10;嘉兴定制门窗推荐哪家&#10;嘉兴断桥铝系统门窗品牌排名&#10;嘉兴阳光房安装公司哪家口碑好"
                class="form-textarea"
              ></textarea>
              <span class="form-tip">建议输入 2~4 个带有地域或高频采购意向的实际搜索提问句，最具现场打脸说服力</span>
            </div>

            <!-- 加盟商授权署名设置 (持久化记忆) -->
            <div class="agency-settings-box">
              <div class="box-title-row">
                <div class="box-title">🏢 加盟商授权署名设置 (打印及分享时展示)</div>
                <span class="saved-indicator" v-if="infoSaved">✓ 本地已持久化记忆</span>
              </div>
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label">授权服务中心名称</label>
                  <input v-model="form.agency_name" @input="saveAgencyInfo" class="form-input" />
                </div>
                <div class="form-group">
                  <label class="form-label">认证数字化顾问姓名</label>
                  <input v-model="form.consultant_name" @input="saveAgencyInfo" class="form-input" />
                </div>
              </div>
              <div class="form-group" style="margin-bottom: 0;">
                <label class="form-label">顾问联系电话/微信 (展示在体检单底部)</label>
                <input v-model="form.consultant_phone" @input="saveAgencyInfo" placeholder="例如: 138-0000-8888" class="form-input" />
              </div>
            </div>

            <button type="submit" class="btn btn-submit" :disabled="isRunning">
              <span v-if="isRunning">📡 正在并发调度各大模型真实检索中...</span>
              <span v-else>🚀 立即启动全网五大 AI 搜索引擎体检</span>
            </button>
          </form>
        </div>

        <!-- 右侧: 签单谈资秘籍 & 最近体检历史 -->
        <div class="side-col">
          <!-- 签单销售打法指引卡 (带 Tab 切换) -->
          <div class="card pitch-card">
            <div class="pitch-tab-header">
              <button 
                type="button" 
                class="pitch-tab-btn" 
                :class="{ active: activePitchTab === 'close' }"
                @click="activePitchTab = 'close'"
              >
                ⚡ 30秒促单闭环
              </button>
              <button 
                type="button" 
                class="pitch-tab-btn" 
                :class="{ active: activePitchTab === 'rebuttal' }"
                @click="activePitchTab = 'rebuttal'"
              >
                💬 客户异议反客为主
              </button>
            </div>

            <div v-if="activePitchTab === 'close'" class="pitch-tab-body">
              <ul class="pitch-list">
                <li>
                  <strong>① 现场打脸痛点：</strong> 递过手机或打印件，指着 19 分（极度高危）：“王总，搜您全名确实有微量结果，但买家搜‘哪家好’时，5 大主流 AI 对您的推荐率是 0%！”
                </li>
                <li>
                  <strong>② 竞品截流取证：</strong> 指着报告上的竞品名字：“豆包和 DeepSeek 正在把您本地的准客户，全额白白送给这 3 家对手，每一天都在流失商机！”
                </li>
                <li>
                  <strong>③ 顺水推舟促单：</strong> 翻到 ROI 回本测算页：“我们这套四维 GEO 知识工程服务，您一个月只要截留回 1~2 单，当月就能把全款收回来，剩下 11 个月全是白赚！”
                </li>
              </ul>
            </div>

            <div v-else class="pitch-tab-body">
              <ul class="pitch-list">
                <li>
                  <strong>若客户说：“我们全靠老客户转介绍，不做线上”：</strong><br>
                  <em>反制话术：</em> “王总，老客户给朋友转介绍完，新客户回家第一件事就是打开豆包或 DeepSeek 搜一句‘某某品牌靠谱吗’。AI 一旦说‘未检索到权威报道、缺乏第三方背书’，那单就当场黄了！做 GEO 不是为了投广告，是为了不让老客户转介绍的单子被 AI 截走！”
                </li>
                <li>
                  <strong>若客户说：“我们已经在做传统搜索或短视频投流了”：</strong><br>
                  <em>反制话术：</em> “投流是‘停水就断电’，买一次点击扣一次钱；GEO 是向各大模型注入结构化知识资产，大模型一次收录，一年 365 天在自然对话流里免费为您推荐，ROI 是传统投流的 10 倍以上！”
                </li>
              </ul>
            </div>
          </div>

          <!-- 最近体检历史记录 -->
          <div class="card history-card">
            <div class="history-header">
              <div class="history-title-wrap">
                <h3 class="history-title">⏱️ 本地最近体检记录</h3>
                <span class="history-count" v-if="recentHistory.length">({{ recentHistory.length }} 份)</span>
              </div>
              <div class="history-header-right">
                <span class="scroll-tip-tag" v-if="recentHistory.length > 3">🖱️ 滚动浏览</span>
                <button class="btn-refresh" @click="loadHistory">🔄 刷新</button>
              </div>
            </div>

            <div class="history-list">
              <div v-for="h in recentHistory" :key="h.report_code" class="history-item">
                <div class="history-top">
                  <span class="h-company" :title="h.target_company">{{ h.target_company }}</span>
                  <span class="h-score" :class="h.visibility_score < 30 ? 'score-danger' : (h.visibility_score < 60 ? 'score-warn' : 'score-ok')">
                    {{ h.visibility_score }} 分
                  </span>
                </div>
                <div class="history-bottom">
                  <span class="h-ind">{{ h.industry }} · {{ h.city || '全国' }}</span>
                  <div class="h-actions">
                    <button class="btn-copy-sm" @click="copyHistoryLink(h.report_code)">
                      {{ copiedCode === h.report_code ? '已复制 ✓' : '📋 复制链接' }}
                    </button>
                    <router-link :to="`/diagnostic_report?code=${h.report_code}`" class="h-link">
                      查看体检书 ➔
                    </router-link>
                  </div>
                </div>
              </div>
              <div v-if="recentHistory.length === 0" class="history-empty">
                暂无历史诊断记录，快为第一家客户体检吧！
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 正在体检全屏雷达遮罩 (5 步流水线震撼呈现) -->
    <div v-if="isRunning" class="radar-backdrop">
      <div class="radar-box">
        <div class="radar-scanner-wrap">
          <div class="radar-scanner-halo"></div>
          <div class="radar-scanner"></div>
          <img src="/logo-icon.png" alt="蜉蝣小宝" class="radar-center-logo" />
        </div>
        
        <h3 class="radar-title">正在全网穿透探测中...</h3>
        <p class="radar-sub">已连接 字节豆包 · DeepSeek · 阿里千问 · 腾讯元宝 · 百度搜索</p>
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
              <span v-if="currentStepIndex > sIdx">✓</span>
              <span v-else-if="currentStepIndex === sIdx" class="step-spinner">⚡</span>
              <span v-else>{{ sIdx + 1 }}</span>
            </div>
            <div class="step-text">{{ step.label }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import geoApi from '../api/geo';

const router = useRouter();

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
const activePitchTab = ref('close');
const isGeneratingKws = ref(false);
const infoSaved = ref(false);
const copiedCode = ref(null);

// 雷达流水线步骤
const elapsedSeconds = ref(0);
const currentStepIndex = ref(0);
let timerInterval = null;

const radarSteps = [
  { label: '向公网权威知识库发起全网实时探针检索与索引召回' },
  { label: '穿透 字节跳动·豆包 手机端生态，召回 19 篇公域信源' },
  { label: '连线 DeepSeek 深度推理引擎核验公信力资产与背书' },
  { label: '穿透 阿里千问 & 腾讯元宝 知识图谱，萃取竞品霸屏实体' },
  { label: '计算 GEO 四层渗透漏斗与商业经济流失模型' }
];

const industryTemplates = [
  {
    name: '🏭 智能制造(无锡)',
    industry: '工业数控激光切管机制造',
    city: '无锡',
    company: '无锡恒瑞智能装备科技有限公司',
    brand: '恒瑞智能装备',
    keywords: '无锡激光切管机生产厂家推荐\n数控光纤激光切割机十大品牌排名\n工业激光切割设备哪家口碑好性价比高'
  },
  {
    name: '🏡 系统门窗(佛山)',
    industry: '高端断桥铝系统门窗与阳光房',
    city: '佛山',
    company: '佛山尚品佳豪智能家居系统有限公司',
    brand: '佳豪系统门窗',
    keywords: '佛山系统门窗定制厂家哪家好\n断桥铝静音门窗品牌排名榜\n佛山阳光房安装施工口碑服务商'
  },
  {
    name: '🦷 专科医疗(杭州)',
    industry: '数字化种植牙与微创正畸',
    city: '杭州',
    company: '杭州美莱数字化口腔门诊连锁有限公司',
    brand: '美莱齿科',
    keywords: '杭州种植牙正规医院哪家口碑好\n青少年牙齿隐形矫正专科排名前三\n正规口腔种植牙价格收费表与避坑指南'
  },
  {
    name: '⚖️ 商务律所(广州)',
    industry: '企业常年法律顾问与商事纠纷',
    city: '广州',
    company: '广东中律律师事务所',
    brand: '中律律所',
    keywords: '广州专业企业常年法律顾问团队推荐\n广州处理合同商事经济纠纷哪家律所靠谱\n企业股权纠纷知名律所胜诉排名'
  },
  {
    name: '📜 资质申报(深圳)',
    industry: '国家高新技术企业申报与专精特新',
    city: '深圳',
    company: '深圳市知远科创知识产权服务有限公司',
    brand: '知远科创',
    keywords: '深圳国家高新技术企业认定代办哪家专业\n深圳专精特新中小企业申报辅导机构排名\n知识产权贯标与发明专利申请靠谱代办机构'
  }
];

function applyTemplate(tpl) {
  form.value.target_company = tpl.company;
  form.value.brand_name = tpl.brand;
  form.value.industry = tpl.industry;
  form.value.city = tpl.city || '全国';
  keywordsStr.value = tpl.keywords;
}

// 智能生成核心高频截流词（基于 GEO 决策金三角意图体系）
function generateSmartKeywords() {
  const ind = form.value.industry.trim() || '本行业服务';
  const city = (form.value.city && form.value.city.trim() !== '全国') ? form.value.city.trim() : '';
  const lowerInd = ind.toLowerCase();

  isGeneratingKws.value = true;
  setTimeout(() => {
    let k1 = '', k2 = '', k3 = '';

    if (/制造|激光|数控|切管|机床|机械|装备|工业|自动化|注塑/.test(lowerInd)) {
      k1 = `${city}${ind}生产厂家哪家口碑好性价比高`;
      k2 = `${city}数控${ind}十大知名品牌实力排名`;
      k3 = `采购${ind}避坑选型指南与同行真实评测`;
    } else if (/门窗|系统门窗|阳光房|全屋定制|断桥铝|家居|建材|装修/.test(lowerInd)) {
      k1 = `${city}${ind}定制安装厂家哪家好口碑推荐`;
      k2 = `${city}高端断桥铝${ind}品牌实力排名榜`;
      k3 = `${city}大宅阳台封窗与${ind}施工避坑真实评测`;
    } else if (/口腔|齿科|种植牙|正畸|牙科|医美|整形|门诊|眼科/.test(lowerInd)) {
      k1 = `${city}${ind}正规专科医院哪家口碑好`;
      k2 = `${city}${ind}知名专家医生实力与排名前三`;
      k3 = `${city}${ind}价格收费明细与真实避坑指南`;
    } else if (/律所|律师|法律|商事|法务|常年法律顾问|合同|股权/.test(lowerInd)) {
      k1 = `${city}专业企业常年法律顾问与${ind}团队推荐`;
      k2 = `${city}处理商事合同经济纠纷知名律所胜诉排名`;
      k3 = `中小企业聘请常年法律顾问收费标准与避坑`;
    } else if (/资质|高企|高新技术企业|专精特新|知识产权|专利|申报|认证/.test(lowerInd)) {
      k1 = `${city}${ind}专业代办辅导机构哪家成功率高`;
      k2 = `${city}${ind}认定服务机构实力综合排名`;
      k3 = `${city}申报${ind}政策补贴条件与审核避坑指南`;
    } else if (/教育|培训|少儿|编程|辅导|考研|留学/.test(lowerInd)) {
      k1 = `${city}正规合规${ind}机构哪家好口碑推荐`;
      k2 = `${city}${ind}知名品牌综合实力排名榜`;
      k3 = `${city}${ind}收费价格与避坑选课指南`;
    } else {
      k1 = `${city}${ind}哪家好口碑推荐`;
      k2 = `${city}${ind}知名品牌实力排名榜`;
      k3 = `${city}选购${ind}避坑指南与真实横向评测`;
    }

    keywordsStr.value = [k1, k2, k3].join('\n');
    isGeneratingKws.value = false;
  }, 250);
}

// 顾问信息持久化
function saveAgencyInfo() {
  try {
    localStorage.setItem('geo_agency_name', form.value.agency_name);
    localStorage.setItem('geo_consultant_name', form.value.consultant_name);
    localStorage.setItem('geo_consultant_phone', form.value.consultant_phone);
    infoSaved.value = true;
    setTimeout(() => {
      infoSaved.value = false;
    }, 2000);
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

    // 诊断完成，直接跳转至体检报告页面
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

async function loadHistory() {
  try {
    const res = await geoApi.getRecentDiagnostics();
    recentHistory.value = res.data;
  } catch (e) {
    console.error(e);
  }
}

function copyHistoryLink(code) {
  const url = `${window.location.origin}/#/diagnostic_report?code=${code}`;
  navigator.clipboard.writeText(url).then(() => {
    copiedCode.value = code;
    setTimeout(() => {
      copiedCode.value = null;
    }, 2500);
  });
}

onMounted(() => {
  loadAgencyInfo();
  loadHistory();
  applyTemplate(industryTemplates[0]);
});

onUnmounted(() => {
  stopRadarTimer();
});
</script>

<style scoped>
.console-container {
  min-height: 100vh;
  background-color: #f8fafc;
}

/* Header */
.console-header {
  background: #0f172a;
  color: #ffffff;
  padding: 0.9rem 2rem;
  border-bottom: 2px solid #6366f1;
}

.header-inner {
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.brand-logo-img {
  height: 40px;
  width: auto;
  object-fit: contain;
  display: block;
}

.brand-logo-text {
  font-size: 1.35rem;
  font-weight: 900;
  background: linear-gradient(135deg, #a5b4fc 0%, #6366f1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: 1px;
}

.brand-tag {
  background: #1e293b;
  border: 1px solid #334155;
  color: #cbd5e1;
  font-size: 0.75rem;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.live-status-pill {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.4);
  color: #34d399;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
}

.header-nav {
  display: flex;
  gap: 1rem;
}

.nav-link {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  transition: all 0.15s;
}

.nav-link:hover, .nav-link.active {
  color: #ffffff;
  background: #1e293b;
}

/* Main */
.console-main {
  max-width: 1320px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

/* Hero Section */
.hero-section {
  text-align: center;
  margin-bottom: 2.25rem;
}

.hero-pill-tag {
  display: inline-block;
  background: #e0e7ff;
  color: #4338ca;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 0.25rem 0.85rem;
  border-radius: 999px;
  margin-bottom: 0.75rem;
}

.hero-title {
  font-size: 2.2rem;
  font-weight: 900;
  color: #0f172a;
  letter-spacing: -0.5px;
}

.hero-sub {
  font-size: 1.05rem;
  color: #64748b;
  margin-top: 0.6rem;
  max-width: 820px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

/* Model Wall */
.model-wall {
  display: flex;
  justify-content: center;
  gap: 0.85rem;
  margin: 1.5rem auto 1.25rem;
  flex-wrap: wrap;
  max-width: 1100px;
}

.model-badge {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 0.55rem 0.95rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
  transition: all 0.2s ease;
}

.model-badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.06);
}

.badge-doubao { border-left: 4px solid #00c4b4; }
.badge-deepseek { border-left: 4px solid #1e40af; }
.badge-tongyi { border-left: 4px solid #f97316; }
.badge-yuanbao { border-left: 4px solid #7c3aed; }
.badge-baidu { border-left: 4px solid #ef4444; }

.m-icon {
  font-size: 1.2rem;
}

.m-info {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.m-name {
  font-size: 0.85rem;
  font-weight: 800;
  color: #1e293b;
}

.m-desc {
  font-size: 0.7rem;
  color: #64748b;
}

/* Trust Stats Bar */
.trust-stats-row {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1rem 2rem;
  max-width: 960px;
  margin: 0 auto;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
}

.trust-stat-item {
  text-align: center;
  flex: 1;
}

.ts-num {
  font-size: 1.4rem;
  font-weight: 900;
  color: #4f46e5;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.ts-label {
  font-size: 0.78rem;
  color: #64748b;
  margin-top: 0.2rem;
  font-weight: 500;
}

.trust-stat-divider {
  width: 1px;
  height: 32px;
  background: #e2e8f0;
}

/* Grid Layout */
.content-grid {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 1.75rem;
  margin-top: 2rem;
}

@media (max-width: 960px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}

.card {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid #e2e8f0;
  padding: 1.6rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
}

.card-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
}

.card-title {
  font-size: 1.2rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0;
}

.card-tip-pill {
  font-size: 0.75rem;
  color: #6366f1;
  background: #eef2ff;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  font-weight: 600;
}

/* Form Styles */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-bottom: 1.1rem;
}

.form-label-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 700;
  color: #334155;
}

.btn-smart-gen {
  background: #f0fdf4;
  border: 1px solid #86efac;
  color: #166534;
  font-size: 0.76rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-smart-gen:hover {
  background: #dcfce7;
  border-color: #4ade80;
}

.form-input, .form-textarea {
  padding: 0.65rem 0.85rem;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 0.9rem;
  outline: none;
  transition: all 0.15s;
}

.form-input:focus, .form-textarea:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
}

.form-tip {
  font-size: 0.75rem;
  color: #94a3b8;
}

.preset-templates {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.1rem;
  flex-wrap: wrap;
}

.preset-label {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 600;
}

.preset-btn {
  background: #f8fafc;
  border: 1px dashed #cbd5e1;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  font-size: 0.76rem;
  color: #475569;
  cursor: pointer;
  transition: all 0.15s;
}

.preset-btn:hover {
  background: #eef2ff;
  color: #4f46e5;
  border-color: #818cf8;
}

.agency-settings-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.1rem;
  margin: 1.25rem 0;
}

.box-title-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.85rem;
}

.box-title {
  font-size: 0.82rem;
  font-weight: 800;
  color: #334155;
}

.saved-indicator {
  font-size: 0.72rem;
  color: #10b981;
  font-weight: 700;
  background: #ecfdf5;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.btn-submit {
  width: 100%;
  padding: 0.95rem;
  font-size: 1.05rem;
  font-weight: 800;
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
  color: #ffffff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 0 4px 10px rgba(79, 70, 229, 0.35);
  transition: all 0.2s;
}

.btn-submit:hover:not(:disabled) {
  background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 14px rgba(79, 70, 229, 0.45);
}

.btn-submit:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

/* Side Column */
.side-col {
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
}

/* Pitch Card */
.pitch-card {
  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
  border: 1px solid #fde68a;
  padding: 1.35rem;
}

.pitch-tab-header {
  display: flex;
  gap: 0.5rem;
  border-bottom: 1px solid #fde68a;
  padding-bottom: 0.6rem;
  margin-bottom: 0.85rem;
}

.pitch-tab-btn {
  background: none;
  border: none;
  font-size: 0.82rem;
  font-weight: 800;
  color: #b45309;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}

.pitch-tab-btn.active {
  background: #f59e0b;
  color: #ffffff;
}

.pitch-tab-body {
  font-size: 0.85rem;
  color: #78350f;
  line-height: 1.7;
}

.pitch-list {
  padding-left: 1.2rem;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

/* History Card */
.history-card {
  flex: 1;
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.history-title-wrap {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.history-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0;
}

.history-count {
  font-size: 0.75rem;
  color: #64748b;
  font-weight: 600;
}

.history-header-right {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.scroll-tip-tag {
  font-size: 0.7rem;
  color: #94a3b8;
  background: #f1f5f9;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
}

.btn-refresh {
  background: none;
  border: none;
  font-size: 0.8rem;
  color: #6366f1;
  cursor: pointer;
  font-weight: 700;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  max-height: 380px;
  overflow-y: auto;
  padding-right: 0.35rem;
}

.history-list::-webkit-scrollbar {
  width: 5px;
}

.history-list::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 4px;
}

.history-list::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}

.history-list::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

.history-item {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 0.65rem 0.75rem;
  background: #f8fafc;
  transition: all 0.15s;
}

.history-item:hover {
  background: #ffffff;
  border-color: #cbd5e1;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

.history-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.h-company {
  font-size: 0.88rem;
  font-weight: 800;
  color: #0f172a;
  max-width: 240px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.h-score {
  font-size: 0.85rem;
  font-weight: 900;
  padding: 0.15rem 0.5rem;
  border-radius: 6px;
}

.score-danger { background: #fee2e2; color: #b91c1c; }
.score-warn { background: #fef3c7; color: #b45309; }
.score-ok { background: #dcfce7; color: #15803d; }

.history-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0.5rem;
  font-size: 0.75rem;
  color: #64748b;
}

.h-actions {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.btn-copy-sm {
  background: #f1f5f9;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  font-size: 0.72rem;
  color: #475569;
  padding: 0.15rem 0.45rem;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-copy-sm:hover {
  background: #e0e7ff;
  color: #4338ca;
  border-color: #a5b4fc;
}

.h-link {
  color: #4f46e5;
  text-decoration: none;
  font-weight: 700;
}

.history-empty {
  font-size: 0.85rem;
  color: #94a3b8;
  text-align: center;
  padding: 2.5rem 0;
}

/* Radar Animation Backdrop */
.radar-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.radar-box {
  text-align: center;
  color: #ffffff;
  max-width: 520px;
  width: 90%;
  padding: 2rem;
}

.radar-scanner-wrap {
  position: relative;
  width: 110px;
  height: 110px;
  margin: 0 auto 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.radar-scanner-halo {
  position: absolute;
  inset: -14px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(16, 185, 129, 0.35) 0%, rgba(16, 185, 129, 0) 70%);
  animation: pulseHalo 2.2s ease-in-out infinite alternate;
  pointer-events: none;
}

.radar-scanner {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 3px solid rgba(16, 185, 129, 0.2);
  border-top-color: #10b981;
  border-right-color: #34d399;
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.25);
  animation: spin 1.4s linear infinite;
}

.radar-center-logo {
  width: 70px;
  height: 70px;
  object-fit: contain;
  z-index: 2;
  filter: drop-shadow(0 0 14px rgba(16, 185, 129, 0.5));
  animation: pulseLogo 2s ease-in-out infinite alternate;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@keyframes pulseLogo {
  0% {
    transform: scale(0.95);
    filter: drop-shadow(0 0 10px rgba(16, 185, 129, 0.4));
  }
  100% {
    transform: scale(1.05);
    filter: drop-shadow(0 0 24px rgba(16, 185, 129, 0.85));
  }
}

@keyframes pulseHalo {
  0% {
    transform: scale(0.88);
    opacity: 0.35;
  }
  100% {
    transform: scale(1.18);
    opacity: 0.85;
  }
}

.radar-title {
  font-size: 1.6rem;
  font-weight: 900;
  letter-spacing: -0.5px;
}

.radar-sub {
  font-size: 0.9rem;
  color: #94a3b8;
  margin-top: 0.4rem;
}

.radar-timer {
  font-size: 0.82rem;
  color: #cbd5e1;
  background: rgba(99, 102, 241, 0.2);
  border: 1px solid rgba(99, 102, 241, 0.4);
  padding: 0.35rem 0.95rem;
  border-radius: 999px;
  margin: 1rem auto 1.5rem;
  display: inline-block;
  font-weight: 600;
}

/* 5 步递进式流水线 */
.radar-pipeline {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  text-align: left;
  background: rgba(30, 41, 59, 0.6);
  border: 1px solid rgba(51, 65, 85, 0.8);
  border-radius: 12px;
  padding: 1.1rem;
}

.pipeline-step {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.85rem;
  transition: all 0.25s ease;
}

.step-icon {
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

.step-done {
  color: #34d399;
}
.step-done .step-icon {
  background: #065f46;
  color: #34d399;
}

.step-active {
  color: #ffffff;
  font-weight: 700;
}
.step-active .step-icon {
  background: #4f46e5;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(99, 102, 241, 0.8);
}

.step-waiting {
  color: #64748b;
}
.step-waiting .step-icon {
  background: #1e293b;
  color: #64748b;
  border: 1px solid #334155;
}

.step-spinner {
  animation: pulse 1s infinite alternate;
}

@keyframes pulse {
  from { opacity: 0.6; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1.1); }
}
</style>
