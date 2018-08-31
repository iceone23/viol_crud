<template>
  <div id="z">
    <b-navbar type="dark" variant="primary" toggleable>
      <b-navbar-toggle target="nav_dropdown_collapse"></b-navbar-toggle>
      <b-collapse is-nav id="nav_dropdown_collapse">
        <b-navbar-nav>
          <b-nav-item href="/violations">Database</b-nav-item>
          <b-nav-item href="/statistics">Statistics</b-nav-item>
          <b-nav-item-dropdown text="User" right>
            <b-dropdown-item href="#">Account</b-dropdown-item>
            <b-dropdown-item href="/user">Settings</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
  </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
  #app {
    background-color:#ebebeb;
    margin-top: 60px;
  }
  body {
    font-family: 'Lato', sans-serif;
    background-color:#ebebeb;
  }
  .nav {
    background-color:#f8f9fa;
  }
</style>
