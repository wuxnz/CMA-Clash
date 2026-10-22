<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<!--<script lang='ts'>
	import { onMount } from 'svelte';
	import '$lib/hljs.css';

	onMount(async () => {
		const { default: hljs } = await import('highlight.js/lib/common');
		hljs.highlightAll();
	});
</script>-->

<svelte:head>
	<title>CMA Clash: docs - Terms of Service</title>
	<meta
		name="description"
		content="The terms of service of CMA Clash, the open-source quiz-application"
	/>
</svelte:head>

<article
	class="prose prose-sm sm:prose lg:prose-lg xl:prose-xl mx-auto mt-10 prose-slate px-4 dark:prose-invert"
>
	<h1>Terms of Service</h1>

	<h2>For those who don't like reading</h2>

	<ul>
		<li>
			<b>The maintainers</b> may do anything with the data you provide, stop providing this service,
			etc.
		</li>
		<li>
			<b
				>You don't upload, write, create any harmful content or anything that is against any
				applicable law.</b
			>
		</li>
	</ul>

	<h2>What doesn't belong on CMA Clash</h2>
	<p>
		The admins may delete, change and modify any quiz. Quizzes with any pornography, illegal
		content or propaganda <b>have to be reported</b> and will be reviewed and deleted, if it's
		against these rules. This platform is made to share educational content, which can include
		anything, but <b>NO PORNOGRAPHY, ILLEGAL CONTENT or PROPAGANDA</b>.
		<i>We hope you understand what we mean.</i> 😇
	</p>
	<h2>How to report illegal content</h2>
	<p>
		You have to report illegal content by opening an issue on the
		<a href="https://github.com/wuxnz/CMA-Clash/issues/new">project issue tracker</a>. If the
		report is about a specific quiz, please include its quiz ID and URL. For reports that should
		not be public, use a
		<a href="https://github.com/wuxnz/CMA-Clash/security/advisories/new"
			>private security advisory</a
		>
		instead.
	</p>
	<h2>The rights of the admin</h2>
	<p>
		The admins are allowed to publish <b>ANY</b> data provided by the user, although the admins
		don't want to do it. The admins can also delete <b>ANY</b> content, whether it's against any
		rule or not. CMA Clash also doesn't provide any (uptime)-guarantee, so CMA Clash could be shut
		down without any warning and without any ability for the user to get their data. The admins may
		publish any data provided by the user anywhere and share it with anyone.
	</p>
	<h2>The rights of the user</h2>
	<p>
		You can request the deletion of your data at any time by
		<a href="https://github.com/wuxnz/CMA-Clash/security/advisories/new"
			>opening a private security advisory</a
		>. Please include the email you registered with on CMA Clash, and, if possible, a proof that
		you are the owner of the account, by, eg., writing from the email-address which is
		associated with your CMA Clash account.
	</p>

	<h2>Final Words</h2>
	<p>
		All of that may sound hard, but, for example, the part with the data-publishing: What
		happens if data should be stolen and published? We don't run this platform to get insulted
		for publishing (personal) data, so we just make sure you're fine with that! Of course, we'll
		try to not publish any data, delete any content without a reason, etc, but we could. If you
		still got any questions, please open an issue on the
		<a href="https://github.com/wuxnz/CMA-Clash/issues/new">project repository</a>.
	</p>
</article>
