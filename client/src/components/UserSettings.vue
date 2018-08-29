<template>
  <div>
      <h2 class="text-center m-2">Налаштування користувача {{ userName }}</h2>
  </div>
</template>

<script>

export default {
  name: 'UserSettings',
  data() {
    return {
      violations: [],
    };
  },
};
</script>

<style scoped>

</style>
