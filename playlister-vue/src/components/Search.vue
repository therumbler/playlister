<template>
  <div class="search">
    <h3>Search</h3>
    <label for="search">Search</label>
    <input type="text" v-model="query" placeholder="search" id="search" />

    <ul class="results">
      <li v-bind:key="track.id" v-for="track in items">{{track.artists[0].name}} — {{track.title}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Search",
  props: {
    query: String,
  },
  data() {
    return {
      items: null,
    };
  },
  methods: {
    search: async function (query) {
      let url = `/api/search/${query}`;
      let resp = await fetch(url);
      let data = await resp.json();
      console.log("data = ", data);
      this.items = data.tracks.items;
    },
  },
  watch: {
    query: async function (newQuery, oldQuery) {
      console.log("watch", newQuery, oldQuery);
      await this.search(newQuery);
    },
  },
};
</script>