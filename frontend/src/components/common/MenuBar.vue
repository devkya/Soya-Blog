<template>
	<div>
		<v-app-bar absolute color="white" app>
			<v-toolbar-title class="font-weight-bold">SoKya Blog</v-toolbar-title>

			<v-spacer></v-spacer>

			<v-slide-group class="hidden-md-and-down">
				<v-slide-item
					v-for="(item, index) in menu"
					:key="index"
					v-slot="{ active, toggle }"
				>
					<v-btn
						id="menu-btn"
						class="elevation-0 px-5"
						:input-value="active"
						v-model="menu"
						:style="active ? 'color: #fbbd28' : undefined"
						@click="
							toggle();
							$emit('menuChg', item.to);
						"
						plain
					>
						{{ item.title }}
					</v-btn>
				</v-slide-item>
			</v-slide-group>
		</v-app-bar>
	</div>
</template>
<script>
export default {
	components: {},
	data() {
		return {
			menu: [
				{ icon: 'mdi-home', title: 'HOME', to: 'home' },

				{ icon: 'mdi-account-circle', title: 'POST', to: 'post' },
				{ icon: 'mdi-web', title: 'ALBUM', to: 'album' },
			],
		};
	},
	setup() {},
	created() {},
	mounted() {},
	unmounted() {},
	methods: {},
};
</script>
