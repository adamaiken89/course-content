# Glossary — trade-lifecycle

Canonical terms for this course. Lessons, quizzes, cloze, cumulative quizzes, and SRS cards use **Canonical** only. Spec: SKILL.md A4.2.

Language: yue. First mention in a lesson may pair EN + local (`Front Office 前台`); afterwards keep one form.

## Lifecycle steps

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| Order | 落單 | 下單（作步驟名） | 客人指示買賣，單入系統 | 01, 03, 04 |
| Execution | 執行 | — | 張單送去市場搵對手成交 | 01, 05 |
| Matching | 配對 | 撮合（作步驟名） | 買賣雙方資料對得上，確認成交存在 | 01, 07 |
| Allocation | 分配 | — | 成交按比例入返正確 account（含單客單 1:1） | 01, 08 |
| Clearing | 清算 | — | CCP 保證 + netting，對已確認成交做處理 | 01, 09 |
| Settlement | 結算 | — | 錢貨兩訖，T+2 過戶完成 | 01, 10 |
| Booking | 入帳 | — | 結算後股票/現金記入客人戶口；月結單先見到 | 01, 14 |

**撮合 vs 配對:** 撮合 = 交易所 match 買賣單（execution venue 行為）；配對 = 雙方交易記錄互核（module 07）。兩者唔可以互換。

## Departments

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| Front Office | 前台 | 前線（部門名） | 落單、執行；直接接觸客人同市場 | 01, 02, 17 |
| Middle Office | 中台 | — | 配對、分配、合規、風控 | 01, 07, 15 |
| Back Office | 後台 | 後線 | 清算、結算、對帳、報告 | 01, 14, 16 |
| RM | 客戶經理 RM | — | 代表客人落單，屬前台 | 01, 18 |

「前線」只可以作普通名詞（如前線同事泛指面對客人的崗位），唔可以當部門正式名。

## Confirmation & matching

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| fill report | fill report | — | T+0 即時成交通知，非 CNR 法定成交單據，但係交易證據 | 06 |
| contract note | contract note | Contract Note（正文） | 法定成交單，列費用；H1 保留 Title Case | 06, 10, 14, 18 |
| affirmation | affirmation | — | 買賣雙方確認配對，T+1 / 48 小時限期 | 06, 07 |
| CTM | CTM | — | Central Trade Manager（DTCC）：機構配對/affirmation 自動化平台，常配 M2i、ALERT | 07, 17 |
| unmatched trade | 未配對交易 | — | 價/量/日期對唔上，要查證修正 | 07, 16 |
| trade break | trade break | — | 對帳發現嘅帳目差異 | 14, 16 |

## Clearing & settlement

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| CCP | 清算所 CCP Central Counterparty | — | 交易對手保證人，降低對手風險 | 01, 09 |
| CSD | 結算機構 CSD Central Securities Depository | — | 中央登記，記錄邊個揸住邊隻股票 | 01, 10 |
| CCASS | CCASS Central Clearing and Settlement System | — | 香港結算系統（CCP + CSD 角色） | 09, 10 |
| DvP | 貨銀兩訖 DvP Delivery versus Payment | — | 貨交割同錢交割綁埋一齊，靠結算系統同步過戶 | 10, 12 |
| custodian | 托管行 Custodian | — | 代客戶持有證券、發 settlement instruction 俾 CSD、對帳出單、failing 管理 | 01, 10, 17 |
| SSI | SSI 常設結算指示 Standing Settlement Instructions | — | 預先登記嘅收付款戶口指引；常設資料，唔係呢單嘅指令（嗰個係 settlement instruction） | 07, 10 |
| netting | netting | — | 對沖交易互抵，減少過手金額 | 09, 18 |
| T+2 | T+2 | T＋2（全形） | 交易日起 2 個工作天內完成交收（港股股票） | 01, 10, 18 |
| settlement fail | 交收失敗 | — | 到期冇完成錢貨交割 | 10, 11 |
| buy-in | 強制買入 buy-in | — | 賣家追數，代買家市場買入，差價+罰則 | 11 |
| margin | 保證金 | — | 保證金購買/持倉抵押；margin call = 追保 | 02, 15 |

## Accounts & allocation

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| omnibus account | 複合戶口 omnibus | 綜合戶口 | 一個市場戶口接多個客：真戶口開喺 CSD/托管行以銀行名義，客人 sub-account 只係銀行內部記帳；點解用：慳戶口成本+結算效率 | 02, 08 |
| average price | 平均價 | — | 合併單統一成本 = 總成本 ÷ 總股數 | 08 |
| discretionary | 全權委託 | — | 客人俾 RM/經理全權操盤 | 02 |
| advisory | 議價式/諮詢 | — | RM 建議，客人自己決定 | 02 |
| agency | 代理模式 agency | — | 幫客搵對手唔持倉，賺佣金；broker/agent 屬此 | 04 |
| principal | 自營模式 principal | — | 自己持倉做客對手，賺 spread；dealer 屬此 | 04 |

## Systems & controls

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| OMS | OMS 訂單管理系統 Order Management System | — | 訂單一生管理，落單到成交狀態 | 17, 18 |
| EMS | EMS 執行管理系統 Execution Management System | — | 執行質素、路由 | 17 |
| suitability | 適當性 | — | 產品風險 vs 客人承受力，事前必查 | 15, 18 |
| pre-trade check | 事前檢查 | — | 落單前攔截：適當性/資金/限制清單 | 15 |
| SLA | SLA 服務水平 | — | 異常處理時限 | 16 |
| cancel-correct | cancel-correct | — | 先 Cancel 再 Correct 再落單，次序唔可亂 | 16 |
| reconciliation | 對帳 | — | 自己 vs 對手 vs 清算所三方核數 | 14 |

## Instruments & fees

| Term | Canonical | Avoid | Definition | Appears |
|---|---|---|---|---|
| NAV | NAV 資產淨值 | — | 基金計價：資產減負債 ÷ 份數 | 12 |
| commission | 佣金 | — | 經紀收費 | 13 |
| stamp duty | 印花稅 | — | 政府稅，買賣各 0.1%（港股） | 13 |
| spread | 買賣差價 spread | — | bid/ask 距離，入場隱性成本 | 05, 13 |
