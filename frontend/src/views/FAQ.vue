<template>
  <div>
    <ul class="questions-list">
      <li v-for="faq in faqs" v-bind:key="faq.id">
        <Faqitem question="faq.quetion" answer="faq.answer" />
      </li>
    </ul>
  </div>
</template>