/**
 * Export complete 1,158 Codeforces DP questions with Infosys Match Matrix & Prediction Index to CSV
 * and update data.js for the interactive web app.
 */

const fs = require('fs');

global.window = {};
require('./infosys-db.js');
require('./matcher.js');

const rawQuestions = JSON.parse(fs.readFileSync('cf_dp_1158_full.json', 'utf-8'));
const infosysDb = window.INFOSYS_QUESTION_DB || [];
const matcher = window.InfosysMatcher;

console.log(`Matching all ${rawQuestions.length} Codeforces DP questions against ${infosysDb.length} Infosys questions...`);

const rows = [];
// CSV Header
rows.push([
  "Problem ID",
  "Problem Name",
  "CF Rating",
  "Topics / Paradigm",
  "Brief Question Summary",
  "Core Intuition",
  "Solution Algorithm",
  "Dry Run Trace",
  "Time Complexity",
  "Space Complexity",
  "Nearest Infosys Question ID",
  "Nearest Infosys Question Title",
  "Target Exam Role",
  "Likeliness Index (%)",
  "Exam Prediction Index (%)",
  "Prediction Tier",
  "Match Invariant Reason",
  "Codeforces Link"
]);

function escapeCsv(str) {
  if (str === null || str === undefined) return '""';
  const s = String(str).replace(/"/g, '""');
  return `"${s}"`;
}

let hotCount = 0;
let highCount = 0;
let moderateCount = 0;
let spCount = 0;
let dseCount = 0;
let bothCount = 0;

rawQuestions.forEach(q => {
  const match = matcher.matchQuestion(q, infosysDb);
  q.matchData = match;

  if (match.predictionTier.includes('HOT')) hotCount++;
  else if (match.predictionTier.includes('HIGH')) highCount++;
  else moderateCount++;

  if (match.targetExam === 'SP') spCount++;
  else if (match.targetExam === 'DSE') dseCount++;
  else bothCount++;

  const best = match.bestMatch || {};

  rows.push([
    q.id,
    q.name,
    q.rating,
    (q.topics || []).join('; '),
    q.shortDescription,
    q.intuition,
    q.solution,
    q.dryRun,
    q.timeComplexity,
    q.spaceComplexity,
    best.id || 'N/A',
    best.title || 'N/A',
    match.targetExam,
    match.overallLikeness,
    match.predictionIndex,
    match.predictionTier,
    match.matchReason,
    q.link
  ]);
});

// Write complete master CSV
const csvContent = rows.map(r => r.map(escapeCsv).join(',')).join('\r\n');
fs.writeFileSync('infosys_cf_dp_matched_master.csv', csvContent, 'utf-8');

console.log(`\nSuccessfully generated 'infosys_cf_dp_matched_master.csv' with all ${rawQuestions.length} Codeforces DP questions!`);
console.log(`Statistics across full 1,158 DP dataset:`);
console.log(`  HOT Prediction (>=82%): ${hotCount}`);
console.log(`  HIGH Prediction (68-81%): ${highCount}`);
console.log(`  MODERATE Prediction (50-67%): ${moderateCount}`);
console.log(`  Target SP (9.5 LPA): ${spCount}`);
console.log(`  Target DSE (6.5 LPA): ${dseCount}`);
console.log(`  Target BOTH: ${bothCount}`);

// Write updated data.js with all 1,158 questions
const updatedDataJs = `/**
 * Codeforces 1200 Memory Sheet - 1,158 High-Yield DP Questions Dataset (Rating 1400-2200)
 * Complete dataset covering all Codeforces DP problemset pages 1 to 12.
 * Enhanced with Input/Output specifications, Step-by-Step Dry Run narratives,
 * and Precomputed Infosys Match Matrix & Exam Prediction Indices.
 */

const INITIAL_QUESTIONS = ${JSON.stringify(rawQuestions, null, 2)};

// Attach globally
if (typeof window !== 'undefined') {
  window.INITIAL_QUESTIONS = INITIAL_QUESTIONS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = INITIAL_QUESTIONS;
}
`;
fs.writeFileSync('data.js', updatedDataJs, 'utf-8');
console.log("Updated data.js with all 1,158 Codeforces DP questions!");
