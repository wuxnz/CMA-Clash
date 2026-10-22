<script lang="ts">
	interface Props {
		checked?: boolean;
		disabled?: boolean;
		id?: string;
		label?: string;
		onchange?: (_checked: boolean) => void;
	}

	let {
		checked = $bindable(false),
		disabled = false,
		id,
		label,
		onchange
	}: Props = $props();
</script>

<button
	type="button"
	role="switch"
	{id}
	aria-checked={checked}
	aria-label={label}
	{disabled}
	class="toggle min-h-11 min-w-11 inline-flex items-center justify-center press-scale"
	onclick={() => {
		if (disabled) return;
		checked = !checked;
		onchange?.(checked);
	}}
></button>
