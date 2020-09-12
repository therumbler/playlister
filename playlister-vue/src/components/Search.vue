<template>
<div class="search">
<input type="text" placeholder="search" id="search"/>
</div>
</template>


<script>
export default {
  name: 'Search',
  props: {
    searchTerm: String
  }
}
</script>