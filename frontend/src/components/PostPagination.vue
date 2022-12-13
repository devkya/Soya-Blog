<template>
	<div>
		<vueper-slides
			class="no-shadow"
			:visible-slides="3"
			:slide-ratio="1 / 4"
			:dragging-distance="70"
		>
			<vueper-slide v-for="i in 9" :key="i" :title="i.toString()" />
		</vueper-slides>
	</div>
</template>
<script>
import { VueperSlides, VueperSlide } from 'vueperslides';
import 'vueperslides/dist/vueperslides.css';
export default {
	components: { VueperSlides, VueperSlide },
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
