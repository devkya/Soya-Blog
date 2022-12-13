<template>
	<v-app>
		<MenuBar></MenuBar>
		<v-main>
			<router-view></router-view>
		</v-main>
	</v-app>
</template>
<script>
import MenuBar from '@/components/common/MenuBar.vue';
export default {
	components: { MenuBar },
	data() {
		return {};
	},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	methods: {},
};
</script>
