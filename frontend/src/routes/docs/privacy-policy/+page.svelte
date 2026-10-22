<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { onMount } from 'svelte';
	import '$lib/hljs.css';

	onMount(async () => {
		const { default: hljs } = await import('highlight.js/lib/common');
		hljs.highlightAll();
	});
</script>

<svelte:head>
	<title>CMA Clash: docs - Privacy policy</title>
	<meta
		name="description"
		content="What data CMA Clash stores, for how long, and how cookies and analytics are used."
	/>
</svelte:head>

<article
	class="prose prose-sm sm:prose lg:prose-lg xl:prose-xl mx-auto mt-10 prose-slate px-4 dark:prose-invert"
>
	<h1>Privacy Policy</h1>

	<h2>What gets stored for how long and why</h2>
	<table>
		<thead>
			<tr>
				<th>What?</th>
				<th>Why?</th>
				<th>How long?</th>
				<th>Where?</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td> The IP-Address of the user</td>
				<td>
					<ul>
						<li>To prevent abuse</li>
						<li>To provide user-sessions</li>
					</ul>
				</td>
				<td> For a very long time</td>
				<td> On the CMA Clash servers, hosted by Render.</td>
			</tr>
			<tr>
				<td> The data the user enters (quizzes, email, username)</td>
				<td> Self-explaining</td>
				<td> Maximum of 30 days after you've deleted your account</td>
				<td> On the CMA Clash servers, hosted by Render.</td>
			</tr>
			<tr>
				<td>The <b>hashed</b> password of the user</td>
				<td>Self-explaining</td>
				<td>Maximum of 30 days after you've deleted your account</td>
				<td>In the CMA Clash database, hosted by Render.</td>
			</tr>
		</tbody>
	</table>

	<h2>Cookies</h2>
	<p>
		Cookies are used to store access-tokens, user-sessions and preferences. They expire after a
		year.
	</p>

	<h2>Tracking</h2>
	<p>
		This site uses <a href="https://sentry.io/">Sentry</a> for error-logging. An opt-out is not
		available at the moment. This website also uses
		<a href="https://plausible.io/">Plausible</a> to log usage-data. Both are privacy-friendly tools
		that do not build a profile of you, and Plausible does not set cookies.
	</p>
	<h3>Third-Parties</h3>
	<p>
		The quiz-admin can enable the captcha, which then loads Google's ReCaptcha which then sends
		something to Google. Refer to Google's <a
			href="https://policies.google.com/privacy?hl=en-GB"
			target="_blank"
			rel="noreferrer">Privacy policy</a
		>.
	</p>
</article>
