<script lang="ts">
	import TopAppBar, { Row, Section, Title } from '@smui/top-app-bar';
	import IconButton from '@smui/icon-button';

	const prominent = false;
	const dense = false;
</script>

<div>
	<TopAppBar variant="static" {prominent} {dense} color="primary">
		<Row>
			<Section>
				<IconButton class="material-icons">menu</IconButton>
				<Title>Lookout</Title>
			</Section>
		</Row>
	</TopAppBar>
</div>

<slot />
