/**
 * Voice Agent Engine - Codeforces & Infosys Interactive Audio Coach
 * Provides conversational reading of:
 * 1. Question Title & Summary
 * 2. Input / Output Format & Constraints
 * 3. Step-by-Step Sample Dry Run
 * 4. Core Intuition & Algorithmic Solution
 */

(function (window) {
  'use strict';

  class VoiceAgent {
    constructor() {
      this.synth = window.speechSynthesis;
      this.currentUtterance = null;
      this.isPlaying = false;
      this.isPaused = false;
      this.rate = 1.0;
      this.selectedVoice = null;
      this.activeQuestion = null;
      this.currentSectionKey = null;

      // Event callbacks
      this.onStateChange = null; // (state: { isPlaying, isPaused, section, text }) => void

      this.initVoices();
    }

    initVoices() {
      if (!this.synth) return;
      
      const setVoice = () => {
        const voices = this.synth.getVoices();
        // Prefer natural / high quality English voices
        this.selectedVoice = voices.find(v => 
          (v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('David') || v.name.includes('Zira')))
        ) || voices.find(v => v.lang.startsWith('en')) || voices[0];
      };

      setVoice();
      if (this.synth.onvoiceschanged !== undefined) {
        this.synth.onvoiceschanged = setVoice;
      }
    }

    setRate(newRate) {
      this.rate = Math.max(0.7, Math.min(2.0, parseFloat(newRate) || 1.0));
      if (this.isPlaying && !this.isPaused) {
        // Restart current section with updated rate
        const q = this.activeQuestion;
        const s = this.currentSectionKey;
        this.stop();
        if (q && s) this.readSection(q, s);
      }
    }

    stop() {
      if (!this.synth) return;
      this.synth.cancel();
      this.isPlaying = false;
      this.isPaused = false;
      this.currentSectionKey = null;
      this.notifyState();
    }

    pause() {
      if (!this.synth || !this.isPlaying) return;
      if (!this.isPaused) {
        this.synth.pause();
        this.isPaused = true;
        this.notifyState();
      }
    }

    resume() {
      if (!this.synth || !this.isPlaying) return;
      if (this.isPaused) {
        this.synth.resume();
        this.isPaused = false;
        this.notifyState();
      }
    }

    notifyState(customText = '') {
      if (typeof this.onStateChange === 'function') {
        this.onStateChange({
          isPlaying: this.isPlaying,
          isPaused: this.isPaused,
          section: this.currentSectionKey,
          question: this.activeQuestion,
          rate: this.rate,
          text: customText
        });
      }
    }

    /**
     * Synthesize and speak a formatted text script
     */
    speakText(text, sectionKey) {
      if (!this.synth) {
        alert('Web Speech API is not supported in this browser.');
        return;
      }

      this.synth.cancel();

      const utterance = new SpeechSynthesisUtterance(text);
      if (this.selectedVoice) utterance.voice = this.selectedVoice;
      utterance.rate = this.rate;
      utterance.pitch = 1.0;

      utterance.onstart = () => {
        this.isPlaying = true;
        this.isPaused = false;
        this.currentSectionKey = sectionKey;
        this.notifyState(text);
      };

      utterance.onend = () => {
        this.isPlaying = false;
        this.isPaused = false;
        this.currentSectionKey = null;
        this.notifyState();
      };

      utterance.onerror = (e) => {
        console.warn('SpeechSynthesis error:', e);
        this.isPlaying = false;
        this.isPaused = false;
        this.currentSectionKey = null;
        this.notifyState();
      };

      this.currentUtterance = utterance;
      this.synth.speak(utterance);
    }

    /**
     * Read specific section for a given question
     */
    readSection(question, sectionKey) {
      if (!question) return;
      this.activeQuestion = question;

      let script = '';

      switch (sectionKey) {
        case 'summary':
          script = `Reading problem summary. Problem ${question.id}: ${question.name}. Rated ${question.rating || 'unrated'}. Topics covered: ${(question.topics || []).join(', ')}. ${question.shortDescription || 'No summary provided.'}`;
          break;

        case 'io':
          const inputFormat = question.inputFormat || "Standard input as described on Codeforces.";
          const outputFormat = question.outputFormat || "Single value or YES/NO answer.";
          const sampleIn = question.sampleInput || "Refer to problem statement.";
          const sampleOut = question.sampleOutput || "Refer to problem statement.";
          script = `Input and Output details. Input specification: ${inputFormat}. Output specification: ${outputFormat}. Sample Input: ${sampleIn}. Expected Output: ${sampleOut}.`;
          break;

        case 'dryrun':
          if (question.dryRun) {
            script = `Step-by-step dry run simulation. ${question.dryRun}`;
          } else {
            // Generate a natural dry run explanation from the problem parameters
            script = `Step-by-step dry run simulation for ${question.name}. Let us trace the core mechanics. Given the input constraints, we process each element step by step. If a condition matches our invariant, we update the state and proceed. Finally, we verify that all test cases pass without edge-case violations.`;
          }
          break;

        case 'intuition':
          script = `Core Intuition and Solution. The Aha! moment: ${question.intuition || 'Focus on invariant reduction.'}. Algorithm steps: ${question.solution ? question.solution.replace(/\n/g, '. ') : 'Greedy or dynamic programming traversal.'}. Expected Time complexity: ${question.timeComplexity || 'O of N'}. Space complexity: ${question.spaceComplexity || 'O of 1'}.`;
          break;

        case 'all':
        default:
          const dryRunSnippet = question.dryRun || "We trace the algorithm with sample inputs, validating constraints and invariants.";
          script = `Welcome to the algorithmic audio breakdown for Problem ${question.id}: ${question.name}. Rated ${question.rating || 800}. Problem Summary: ${question.shortDescription || ''}. Input and Output: Sample Input is ${question.sampleInput || 'provided in statement'}. Expected output is ${question.sampleOutput || 'result'}. Dry Run Analysis: ${dryRunSnippet}. Core Intuition: ${question.intuition || ''}. Time complexity is ${question.timeComplexity || 'O of N'}, with space complexity ${question.spaceComplexity || 'O of 1'}.`;
          break;
      }

      this.speakText(script, sectionKey);
    }
  }

  // Create global instance
  window.voiceCoach = new VoiceAgent();

})(window);
