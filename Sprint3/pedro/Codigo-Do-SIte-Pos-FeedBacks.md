<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RotaPUC</title>
<meta name="description" content="Plataforma de apoio ao intercâmbio acadêmico dos alunos da PUC-Rio.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
  /* Paleta RotaPUC (mesma do projeto original) — tema claro único */
  :root {
    --brand: #165dad;
    --brand-dark: #103b66;
    --brand-yellow: #f4b942;
    --brand-light: #eaf3fc;
    --surface: #f5f7f9;
    --bg: #ffffff;
    --fg: #172b3a;
    --muted: #f5f7f9;
    --muted-fg: #667684;
    --border: #dbe4ec;
    --destructive: #c2362b;
    --on-brand: #ffffff;
    --overlay: rgb(16 59 102 / 0.55);
    --header-bg: rgb(255 255 255 / 0.95);
    --shadow-card: 0 2px 12px rgb(16 59 102 / 0.08);
    --shadow-card-hover: 0 8px 24px rgb(16 59 102 / 0.14);
    --r-lg: 12px;
    --r-xl: 16px;
    --r-2xl: 20px;
    --font: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
    --header-h: 73px;
    color-scheme: light;
  }

  *, *::before, *::after { box-sizing: border-box; }
  html { background: var(--bg); scroll-behavior: auto; }
  body {
    margin: 0;
    font-family: var(--font);
    font-size: 16px;
    line-height: 1.5;
    background: var(--bg);
    color: var(--fg);
    -webkit-font-smoothing: antialiased;
  }
  h1, h2, h3, h4, p, dl, dd, ul, ol, figure { margin: 0; }
  ul, ol { padding: 0; }
  img { display: block; max-width: 100%; }
  table { font: inherit; border-collapse: collapse; }
  button, input, select, textarea { font: inherit; color: inherit; }
  a { color: inherit; }
  :focus-visible { outline: 2px solid var(--brand-dark); outline-offset: 2px; }

  /* Webapp desktop: largura mínima fixa, sem adaptação para celular/tablet */
  .app { min-width: 1080px; min-height: 100vh; display: flex; flex-direction: column; }
  main { flex: 1; outline: none; }
  .container { width: 100%; max-width: 1280px; margin-inline: auto; padding-inline: 24px; }

  /* ---------- Cabeçalho ---------- */
  .site-header {
    position: sticky;
    top: env(safe-area-inset-top, 0px);
    z-index: 50;
    background: var(--header-bg);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--border);
  }
  .site-header .bar { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-block: 16px; }
  .logo { display: flex; align-items: center; gap: 10px; color: var(--brand-dark); text-decoration: none; border-radius: 8px; }
  .logo svg { width: 58px; height: 40px; flex-shrink: 0; }
  .logo-word { font-size: 18px; line-height: 28px; font-weight: 700; color: var(--brand-dark); }
  .logo-word span { color: var(--brand-yellow); }
  .nav ul { display: flex; align-items: center; gap: 8px; list-style: none; }
  .nav a {
    display: inline-block;
    padding: 8px 16px;
    border: 1px solid var(--brand);
    border-radius: 999px;
    background: var(--bg);
    color: var(--brand);
    font-size: 14px;
    line-height: 20px;
    font-weight: 600;
    text-decoration: none;
    white-space: nowrap;
    transition: background-color .15s, color .15s;
  }
  .nav a:hover { background: var(--brand-light); }
  .nav a[aria-current="page"] { background: var(--brand); color: var(--on-brand); }

  /* ---------- Elementos base ---------- */
  .pill {
    display: inline-flex;
    align-items: center;
    width: fit-content;
    padding: 8px 20px;
    border-radius: 999px;
    background: var(--brand);
    color: var(--on-brand);
    font-size: 14px;
    line-height: 20px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .025em;
  }
  .pill-link { text-decoration: none; transition: background-color .15s; }
  .pill-link:hover { background: var(--brand-dark); }
  .center { display: flex; justify-content: center; }
  .text-center { text-align: center; }
  .page-title { font-size: 40px; line-height: 1.2; font-weight: 700; color: var(--brand-dark); text-wrap: balance; }
  .section-title { font-size: 28px; line-height: 1.3; font-weight: 700; color: var(--brand-dark); text-wrap: balance; }
  .lead { max-width: 672px; font-size: 16px; line-height: 24px; color: var(--muted-fg); }
  .lead.centered { margin-inline: auto; text-align: center; }
  .muted-sm { font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .updated { font-size: 12px; line-height: 16px; color: var(--muted-fg); }
  .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: fit-content;
    padding: 8px 20px;
    border: 0;
    border-radius: 999px;
    font-size: 14px;
    line-height: 20px;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
    transition: background-color .15s, color .15s, opacity .15s;
  }
  .btn-lg { padding: 12px 24px; }
  .btn-primary { background: var(--brand); color: var(--on-brand); }
  .btn-primary:hover { background: var(--brand-dark); }
  .btn-white { background: var(--bg); color: var(--brand); }
  .btn-white:hover { background: var(--brand-light); }
  .btn-outline { background: var(--bg); color: var(--brand); border: 1px solid var(--brand); }
  .btn-outline:hover { background: var(--brand); color: var(--on-brand); }
  .btn:disabled { opacity: .5; cursor: not-allowed; }
  .btn-primary:disabled:hover { background: var(--brand); }
  .link-btn {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 0; border: 0; background: none; cursor: pointer;
    font-size: 14px; line-height: 20px; font-weight: 600; color: var(--brand);
    text-decoration: none; border-radius: 4px;
  }
  .link-btn:hover { text-decoration: underline; text-underline-offset: 4px; }
  .link-btn .chev { transition: transform .2s; }
  .link-btn[aria-expanded="true"] .chev { transform: rotate(180deg); }
  .text-link { color: var(--brand); text-decoration: none; }
  .text-link:hover { text-decoration: underline; text-underline-offset: 4px; }

  .card { background: var(--bg); border: 1px solid var(--border); border-radius: var(--r-xl); box-shadow: var(--shadow-card); }
  .card-hover { transition: box-shadow .2s; }
  .card-hover:hover { box-shadow: var(--shadow-card-hover); }
  .info-card { padding: 24px; }
  .info-card h3 { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .info-body { margin-top: 12px; font-size: 14px; line-height: 1.625; color: var(--muted-fg); }
  .info-body > p + p { margin-top: 0; }
  .info-body .spaced { margin-top: 12px; }
  .bullets { list-style: disc; padding-left: 20px; display: grid; gap: 4px; }
  .chip {
    display: inline-flex; align-items: center;
    padding: 4px 12px; border-radius: 999px;
    background: var(--brand-light); color: var(--brand-dark);
    font-size: 12px; line-height: 16px; font-weight: 600;
  }
  .chips { display: flex; flex-wrap: wrap; gap: 8px; list-style: none; }
  .empty { padding: 40px; text-align: center; background: var(--muted); border: 1px dashed var(--border); border-radius: var(--r-xl); }
  .empty-title { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .empty-desc { margin-top: 8px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .grid-2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
  .stack { display: grid; gap: 24px; align-content: start; }

  .table-wrap { overflow-x: auto; border: 1px solid var(--border); border-radius: var(--r-xl); }
  .table-wrap table { width: 100%; text-align: left; font-size: 14px; line-height: 20px; }
  .table-wrap thead { background: var(--brand-light); color: var(--brand-dark); }
  .table-wrap th { padding: 12px 16px; font-weight: 600; }
  .table-wrap td { padding: 12px 16px; border-top: 1px solid var(--border); font-variant-numeric: tabular-nums; }
  .table-wrap td.key { color: var(--muted-fg); }
  .table-wrap td.val { font-weight: 500; color: var(--brand-dark); }
  .table-wrap .right { text-align: right; }
  .table-wrap.compact td { padding-block: 10px; }

  .avatar {
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    width: 36px; height: 36px; border-radius: 999px;
    background: var(--brand-light); color: var(--brand-dark);
    font-size: 12px; font-weight: 700;
  }
  .avatar.lg { width: 40px; height: 40px; }
  .avatar.sm { width: 32px; height: 32px; font-size: 10px; background: var(--muted); }

  .icon { flex-shrink: 0; }

  /* Transição suave entre telas */
  .page { animation: page-in .22s ease-out; }
  @keyframes page-in { from { opacity: .4; transform: translateY(4px); } to { opacity: 1; transform: none; } }

  /* ---------- Início ---------- */
  .hero { position: relative; height: 460px; overflow: hidden; }
  .hero > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
  .hero-overlay { position: absolute; inset: 0; background: var(--overlay); }
  .hero-content { position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; }
  .hero-title { margin-top: 16px; max-width: 768px; font-size: 40px; line-height: 1.25; font-weight: 700; color: var(--on-brand); }
  .hero-text { margin-top: 12px; max-width: 672px; font-size: 16px; line-height: 24px; color: rgb(255 255 255 / .9); }
  .hero-actions { margin-top: 24px; display: flex; flex-wrap: wrap; gap: 12px; }

  .banner { padding: 32px; border-radius: var(--r-2xl); background: var(--brand-light); }
  .banner h2 { font-size: 20px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .banner p { margin-top: 8px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .banner-row { margin-top: 20px; display: flex; flex-wrap: wrap; align-items: center; gap: 16px; }
  .banner-text { animation: page-in .25s ease-out; }
  .dots { margin-left: auto; display: flex; align-items: center; gap: 8px; }
  .dots.centered { margin-left: 0; justify-content: center; gap: 12px; }
  .dot {
    width: 12px; height: 12px; padding: 0;
    border: 1px solid var(--brand); border-radius: 999px;
    background: var(--bg); cursor: pointer;
    transition: background-color .15s;
  }
  .dot[aria-current="true"] { background: var(--brand); }

  .country-card { display: block; overflow: hidden; text-decoration: none; color: inherit; }
  .country-card img { width: 100%; height: 224px; object-fit: cover; transition: transform .3s; }
  .country-card:hover img { transform: scale(1.03); }
  .country-card .body { position: relative; padding: 20px; background: var(--bg); }
  .country-card h3 { font-size: 20px; line-height: 28px; font-weight: 700; color: var(--brand-dark); }
  .country-card p { margin-top: 4px; }

  /* ---------- Universidades ---------- */
  .filters-hero { padding-block: 40px; background: var(--brand-light); }
  .filters { margin-top: 24px; display: grid; grid-template-columns: minmax(240px, 320px) minmax(0, 1fr); gap: 16px; align-items: end; }
  .selects { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; }
  .field { display: flex; flex-direction: column; gap: 4px; font-size: 14px; line-height: 20px; }
  .field-label { font-weight: 500; color: var(--brand-dark); }
  .search-wrap { position: relative; display: block; }
  .search-wrap .icon { position: absolute; left: 16px; top: 50%; transform: translateY(-50%); color: var(--muted-fg); pointer-events: none; }
  .input-pill, .select-pill {
    width: 100%;
    padding: 8px 16px;
    border: 1px solid var(--border);
    border-radius: 999px;
    background-color: var(--bg);
    font-size: 14px;
    line-height: 20px;
    color: var(--fg);
  }
  .input-pill { padding-left: 44px; }
  .input-pill::placeholder { color: var(--muted-fg); }
  .select-pill {
    appearance: none;
    -webkit-appearance: none;
    padding-right: 34px;
    text-overflow: ellipsis;
    cursor: pointer;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23165dad' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 12px center;
  }
  .select-pill.is-set { border-color: var(--brand); color: var(--brand-dark); font-weight: 500; }
  .input-pill:focus-visible, .select-pill:focus-visible { outline: 2px solid var(--brand); outline-offset: 2px; }
  .results-head { display: flex; align-items: center; gap: 16px; }
  .groups { margin-top: 32px; display: grid; gap: 48px; }
  .group-head { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; }

  .uni-card { display: flex; flex-direction: column; overflow: hidden; }
  .uni-card img { width: 100%; height: 176px; object-fit: cover; }
  .uni-card-body { flex: 1; display: flex; flex-direction: column; gap: 8px; padding: 20px; }
  .uni-card h3 { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .site-link { width: fit-content; font-size: 14px; line-height: 20px; font-weight: 500; color: var(--brand); text-decoration: none; }
  .site-link:hover { text-decoration: underline; text-underline-offset: 4px; }
  .uni-card .btn { margin-top: auto; }

  /* ---------- Detalhes ---------- */
  .detail-hero { margin-top: 24px; width: 100%; object-fit: cover; border-radius: var(--r-2xl); }
  .breadcrumb { display: flex; align-items: center; gap: 8px; margin-bottom: 20px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .breadcrumb a { display: inline-flex; align-items: center; gap: 6px; color: var(--brand); text-decoration: none; font-weight: 500; }
  .breadcrumb a:hover { text-decoration: underline; text-underline-offset: 4px; }
  .testimonials { margin-top: 40px; padding: 24px; background: var(--muted); border: 1px dashed var(--border); border-radius: var(--r-xl); }
  .testimonials h3 { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }

  /* ---------- Processo seletivo ---------- */
  .process-top { margin-top: 40px; display: grid; grid-template-columns: 320px minmax(0, 1fr); gap: 32px; align-items: start; }
  .process-index { padding: 24px; scroll-margin-top: calc(var(--header-h) + 24px); }
  .process-index h2, .cr-title { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .process-index ul { margin-top: 16px; display: grid; gap: 8px; list-style: none; }
  .process-index a { font-size: 14px; line-height: 20px; font-weight: 500; color: var(--brand); text-decoration: none; }
  .process-index a:hover { text-decoration: underline; text-underline-offset: 4px; }
  .step { margin-top: 56px; padding-top: 40px; border-top: 1px solid var(--border); scroll-margin-top: calc(var(--header-h) + 16px); }
  .step.first { margin-top: 64px; }
  .step-back { margin-top: 24px; display: flex; justify-content: flex-end; }
  .b-par { margin-top: 16px; max-width: 880px; font-size: 14px; line-height: 1.625; color: var(--muted-fg); }
  .b-sub { margin-top: 24px; font-size: 16px; line-height: 24px; font-weight: 600; color: var(--brand-dark); }
  .b-list { margin-top: 16px; padding-left: 20px; display: grid; gap: 8px; font-size: 14px; line-height: 1.625; color: var(--muted-fg); }
  .b-list.num { list-style: decimal; }
  .b-list.disc { list-style: disc; }
  .b-box { margin-top: 20px; padding: 20px; display: grid; gap: 12px; border-radius: var(--r-xl); background: var(--brand-light); font-size: 14px; line-height: 1.625; color: var(--brand-dark); }
  .b-note { margin-top: 16px; padding: 16px; border: 1px solid var(--border); border-radius: var(--r-lg); background: var(--muted); font-size: 12px; line-height: 1.625; color: var(--muted-fg); }
  .b-highlight { margin-top: 16px; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--brand); }
  .b-chips { margin-top: 16px; }
  .b-table { margin-top: 20px; max-width: 640px; }
  .b-cards { margin-top: 20px; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
  .b-card { padding: 20px; border-radius: var(--r-xl); background: var(--brand-light); }
  .b-card h4 { font-size: 14px; line-height: 20px; font-weight: 600; color: var(--brand-dark); }
  .b-card p { margin-top: 8px; font-size: 14px; line-height: 1.625; color: var(--muted-fg); }
  .faq-list { margin-top: 24px; display: grid; gap: 12px; }
  .faq { padding: 20px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--r-xl); }
  .faq summary { cursor: pointer; font-size: 16px; line-height: 24px; font-weight: 600; color: var(--brand-dark); }
  .faq p { margin-top: 8px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }

  /* ---------- Fórum ---------- */
  .forum-bar { margin-top: 40px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; }
  .forum-bar .count { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .thread-list { margin-top: 24px; display: grid; gap: 16px; }
  .thread { display: block; padding: 24px; text-decoration: none; color: inherit; }
  .thread h3 { font-size: 18px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
  .thread .desc { margin-top: 8px; }
  .meta { display: flex; flex-wrap: wrap; align-items: center; gap: 12px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .thread .meta { margin-top: 16px; }
  .meta .who { font-weight: 500; color: var(--fg); }
  .meta .push { margin-left: auto; display: inline-flex; align-items: center; gap: 8px; }
  .meta .votes { display: inline-flex; align-items: center; gap: 6px; }
  .forum-foot { margin-top: 32px; text-align: center; font-size: 12px; line-height: 16px; color: var(--muted-fg); }
  .forum-foot .link-btn { font-size: 12px; line-height: 16px; }

  .post { margin: 32px auto 0; max-width: 896px; padding: 32px; border-radius: var(--r-2xl); }
  .post h1 { margin-top: 16px; font-size: 28px; line-height: 1.3; font-weight: 700; color: var(--brand-dark); text-wrap: balance; }
  .post .body-text { margin-top: 16px; font-size: 16px; line-height: 1.625; color: var(--fg); white-space: pre-line; }
  .post .meta { margin-top: 24px; gap: 16px; }
  .post .meta .name { font-weight: 600; color: var(--fg); }
  .upvote {
    margin-left: auto;
    display: inline-flex; align-items: center; gap: 8px;
    padding: 8px 16px;
    border: 1px solid var(--brand); border-radius: 999px;
    background: var(--bg); color: var(--brand);
    font-size: 14px; line-height: 20px; font-weight: 600;
    cursor: pointer; transition: background-color .15s, color .15s;
  }
  .upvote:hover { background: var(--brand-light); }
  .upvote[aria-pressed="true"] { background: var(--brand); color: var(--on-brand); }
  .inline-count { display: inline-flex; align-items: center; gap: 8px; }
  .reply-form { margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--border); }
  .form-label { display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--brand-dark); }
  .textarea, .input {
    display: block;
    width: 100%;
    margin-top: 8px;
    padding: 12px 16px;
    border: 1px solid var(--border);
    border-radius: var(--r-lg);
    background: var(--bg);
    font-size: 14px;
    line-height: 20px;
    color: var(--fg);
    resize: vertical;
  }
  .textarea.sm { padding: 8px 16px; }
  .textarea::placeholder, .input::placeholder { color: var(--muted-fg); }
  .textarea:focus-visible, .input:focus-visible { outline: 2px solid var(--brand); outline-offset: 2px; }
  .input[aria-invalid="true"], .textarea[aria-invalid="true"] { border-color: var(--destructive); }
  .field-error { margin-top: 8px; font-size: 14px; line-height: 20px; color: var(--destructive); }
  .reply-form .btn { margin-top: 12px; padding: 10px 24px; }

  .comments { margin: 40px auto 0; max-width: 896px; }
  .comments > h2 { font-size: 20px; line-height: 28px; font-weight: 600; color: var(--brand-dark); }
  .comment-list { margin-top: 16px; display: grid; gap: 16px; list-style: none; }
  .comment { padding: 20px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--r-xl); }
  .c-head { display: flex; align-items: center; gap: 12px; }
  .c-name { font-size: 14px; line-height: 20px; font-weight: 600; color: var(--fg); }
  .c-date { font-size: 12px; line-height: 16px; color: var(--muted-fg); }
  .c-text { margin-top: 12px; font-size: 14px; line-height: 1.625; color: var(--fg); white-space: pre-line; }
  .comment > .link-btn { margin-top: 12px; }
  .c-form { margin-top: 12px; }
  .c-form .btn { margin-top: 8px; }
  .replies { margin-top: 16px; padding-left: 20px; display: grid; gap: 12px; list-style: none; border-left: 2px solid var(--brand-light); }
  .replies .c-text { margin-top: 8px; }

  .new-form { margin: 40px auto 0; max-width: 768px; padding: 32px; border-radius: var(--r-2xl); }
  .new-form .group + .group { margin-top: 24px; }
  .new-form fieldset { margin: 24px 0 0; padding: 0; border: 0; }
  .new-form legend { padding: 0; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--brand-dark); }
  .tag-toggles { margin-top: 12px; display: flex; flex-wrap: wrap; gap: 8px; }
  .tag-toggle {
    padding: 6px 16px;
    border: 1px solid var(--brand); border-radius: 999px;
    background: var(--bg); color: var(--brand);
    font-size: 14px; line-height: 20px; font-weight: 500;
    cursor: pointer; transition: background-color .15s, color .15s;
  }
  .tag-toggle:hover { background: var(--brand-light); }
  .tag-toggle[aria-pressed="true"] { background: var(--brand); color: var(--on-brand); }
  .new-form .actions { margin-top: 32px; display: flex; align-items: center; gap: 16px; }

  /* ---------- Rodapé ---------- */
  .footer { margin-top: 64px; background: var(--brand-light); }
  .footer .container { padding-block: 56px; }
  .footer dl { margin-top: 40px; display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 32px; }
  .footer dt { font-size: 16px; line-height: 24px; font-weight: 600; color: var(--brand-dark); }
  .footer dd { margin-top: 8px; display: grid; gap: 4px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .socials { margin-top: 40px; display: flex; justify-content: center; gap: 16px; list-style: none; }
  .socials a {
    display: flex; align-items: center; justify-content: center;
    width: 44px; height: 44px; border-radius: 999px;
    background: var(--brand); color: var(--on-brand);
    transition: background-color .15s;
  }
  .socials a:hover { background: var(--brand-dark); }
  .disclaimer { margin-top: 32px; text-align: center; font-size: 12px; line-height: 16px; color: var(--muted-fg); }

  /* ---------- 404 ---------- */
  .not-found { padding-block: 96px; text-align: center; }
  .not-found .code { font-size: 72px; line-height: 1; font-weight: 700; color: var(--brand-dark); }
  .not-found h1 { margin-top: 16px; font-size: 20px; line-height: 28px; font-weight: 600; color: var(--fg); }
  .not-found p { margin-top: 8px; font-size: 14px; line-height: 20px; color: var(--muted-fg); }
  .not-found .btn { margin-top: 24px; }

  /* ---------- Aviso (toast) ---------- */
  .toast {
    position: fixed;
    right: 24px;
    bottom: calc(24px + env(safe-area-inset-bottom, 0px));
    z-index: 100;
    display: flex; align-items: center; gap: 10px;
    padding: 12px 18px;
    border-radius: var(--r-lg);
    background: var(--brand-dark);
    color: var(--on-brand);
    font-size: 14px; line-height: 20px; font-weight: 500;
    box-shadow: var(--shadow-card-hover);
    opacity: 0;
    transform: translateY(8px);
    pointer-events: none;
    transition: opacity .2s, transform .2s;
  }
  .toast.show { opacity: 1; transform: none; }
  .toast .icon { color: var(--brand-yellow); }

  /* Espaçamentos utilitários */
  .mt-4 { margin-top: 4px; } .mt-8 { margin-top: 8px; } .mt-12 { margin-top: 12px; } .mt-16 { margin-top: 16px; }
  .mt-24 { margin-top: 24px; } .mt-32 { margin-top: 32px; } .mt-40 { margin-top: 40px; } .mt-48 { margin-top: 48px; } .mt-56 { margin-top: 56px; } .mt-64 { margin-top: 64px; }
  .py-40 { padding-block: 40px; } .py-48 { padding-block: 48px; } .py-64 { padding-block: 64px; } .pb-48 { padding-bottom: 48px; }

  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
  }
</style>

<div class="app">
  <header class="site-header">
    <div class="container bar">
      <a href="#/" class="logo" aria-label="RotaPUC — início">
        <svg viewBox="0 0 58 40" aria-hidden="true">
          <circle cx="8" cy="32" r="5.5" fill="currentColor"></circle>
          <circle cx="17" cy="23" r="1.8" fill="currentColor"></circle>
          <circle cx="25" cy="16" r="1.8" fill="currentColor"></circle>
          <circle cx="34" cy="11" r="1.8" fill="currentColor"></circle>
          <path d="M43 3v17" stroke="currentColor" stroke-width="2"></path>
          <path d="M44 4 55 10 44 16Z" fill="#f4b942"></path>
        </svg>
        <span class="logo-word">Rota<span>PUC</span></span>
      </a>
      <nav class="nav" aria-label="Navegação principal">
        <ul id="nav-list"></ul>
      </nav>
    </div>
  </header>
  <main id="main" tabindex="-1"></main>
  <footer class="footer" id="footer"></footer>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
(function () {
  "use strict";
  document.documentElement.lang = "pt-BR";

  /* ================================================================
     DADOS (conteúdo do projeto original — src/data/puc.ts)
     ================================================================ */
  var IMG = {
    alemanha: "assets/alemanha.jpg",
    espanha: "assets/espanha.jpg",
    argentina: "assets/argentina.jpg",
    chile: "assets/chile.jpg",
    campus: "assets/campus.jpg",
    hero: "assets/hero.jpg"
  };

  var ULTIMA_ATUALIZACAO = "12/09/2026";
  var TODOS = "Todos";

  /* Cotação de referência para mostrar o custo de vida em reais (AwesomeAPI, 17/09/2026) */
  var COTACAO = { data: "17/09/2026", EUR: 5.89, USD: 5.12 };
  var SIMBOLO = { EUR: "€", USD: "US$" };
  function reais(moeda, valor) {
    return "R$ " + (Math.round(valor * COTACAO[moeda] / 10) * 10).toLocaleString("pt-BR");
  }
  function emReais(moeda, min, max) {
    return " (≈ " + reais(moeda, min) + (max ? " a " + reais(moeda, max) : "") + ")";
  }
  function notaCotacao(itens) {
    var texto = itens.join(" ");
    if (texto.indexOf("R$") === -1) return "";
    var moedas = ["EUR", "USD"].filter(function (m) { return texto.indexOf(SIMBOLO[m]) !== -1; });
    return '<p class="updated mt-16">Valores em reais convertidos pela cotação de ' + COTACAO.data + ": " +
      moedas.map(function (m) { return SIMBOLO[m] + "1 = R$ " + COTACAO[m].toLocaleString("pt-BR", { minimumFractionDigits: 2 }); }).join(" · ") +
      ".</p>";
  }

  var paises = [
    {
      id: "alemanha", nome: "Alemanha", continente: "Europa",
      idiomaOficial: "Alemão (nível B1/B2 recomendado para a maioria das disciplinas, alguns cursos em Inglês)",
      moeda: "Euro (€)",
      fusoHorario: "GMT+1 (6 horas à frente do horário oficial de Brasília)",
      requisitosParaEntrar: [
        "Passaporte válido por pelo menos 6 meses após o retorno",
        "Visto de estudante solicitado no consulado alemão",
        "Comprovação financeira (Sperrkonto) exigida para o visto",
        "Seguro saúde internacional válido em todo o período"
      ],
      informacoesAdicionais: [
        "Custo de vida médio entre €850 e €1.100 por mês" + emReais("EUR", 850, 1100),
        "Semestre de inverno inicia em outubro; semestre de verão em abril",
        "Transporte público geralmente incluído no semester ticket",
        "Moradia estudantil deve ser solicitada com antecedência"
      ],
      imagem: IMG.alemanha
    },
    {
      id: "espanha", nome: "Espanha", continente: "Europa",
      idiomaOficial: "Espanhol (nível B1 mínimo na maioria dos convênios)",
      moeda: "Euro (€)",
      fusoHorario: "GMT+1 (5 a 6 horas à frente do horário oficial de Brasília)",
      requisitosParaEntrar: [
        "Passaporte válido",
        "Visto de estudante para estadias superiores a 90 dias",
        "Carta de aceite da universidade de destino",
        "Seguro saúde com cobertura internacional"
      ],
      informacoesAdicionais: [
        "Custo de vida médio entre €700 e €1.000 por mês" + emReais("EUR", 700, 1000),
        "Calendário acadêmico de setembro a junho",
        "Grande oferta de disciplinas em espanhol e algumas em inglês"
      ],
      imagem: IMG.espanha
    },
    {
      id: "argentina", nome: "Argentina", continente: "América do Sul",
      idiomaOficial: "Espanhol",
      moeda: "Peso argentino (ARS)",
      fusoHorario: "GMT-3 (mesmo horário oficial de Brasília)",
      requisitosParaEntrar: [
        "Documento de identidade ou passaporte válido (Mercosul)",
        "Comprovante de matrícula na universidade de destino",
        "Seguro saúde internacional"
      ],
      informacoesAdicionais: [
        "Custo de vida mais baixo em comparação com destinos europeus",
        "Calendário acadêmico de março a dezembro",
        "Proximidade facilita viagens curtas e passagens mais baratas"
      ],
      imagem: IMG.argentina
    },
    {
      id: "chile", nome: "Chile", continente: "América do Sul",
      idiomaOficial: "Espanhol",
      moeda: "Peso chileno (CLP)",
      fusoHorario: "GMT-3 (mesmo horário oficial de Brasília)",
      requisitosParaEntrar: [
        "Passaporte válido",
        "Visa de estudiante para estadias superiores a um semestre",
        "Carta de aceite da instituição chilena"
      ],
      informacoesAdicionais: [
        "Custo de vida médio entre US$600 e US$900 por mês" + emReais("USD", 600, 900),
        "Calendário acadêmico de março a dezembro",
        "Forte oferta em engenharias e ciências sociais"
      ],
      imagem: IMG.chile
    }
  ];

  var universidades = [
    {
      id: "tum", nome: "Technical University of Munich", sigla: "TUM", cidade: "Munique",
      siteOficial: "www.tum.de", ranking: "#28 no ranking global (dado demonstrativo)",
      foto: IMG.alemanha, endereco: "Arcisstraße 21, 80333 München", paisId: "alemanha", vagas: 6,
      sobre: "Universidade técnica de referência na Alemanha, com forte atuação em engenharia, tecnologia e ciências naturais.",
      perfilAcademico: "Perfil orientado à pesquisa aplicada, com laboratórios integrados à indústria e disciplinas em alemão e inglês.",
      cursos: ["Engenharia", "Ciência da Computação", "Física", "Administração"],
      certificados: ["TestDaF nível 4", "IELTS 6.5", "TOEFL iBT 88"],
      requisitosAcademicos: ["CR mínimo de 7,0", "Ter concluído pelo menos 40% do curso na PUC-Rio", "Comprovante de proficiência em alemão (B2) ou inglês"],
      custos: ["Isenção de mensalidade por convênio", "Taxa semestral aproximada de €150", "Custo de vida estimado em €1.000/mês" + emReais("EUR", 1000)],
      bolsas: ["DAAD (auxílio parcial)", "Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar em inglês", "Carta de motivação", "Comprovante de proficiência", "Cópia do passaporte"],
      contato: "international@tum.de",
      programas: [
        { id: "tum-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "1 semestre", prazoInscricao: "15/03/2027", idioma: "Alemão / Inglês", tipoIntercambio: "Convênio", vagas: 4 },
        { id: "tum-2", nivel: "Pós-graduação", custo: "Isento (convênio)", duracao: "2 semestres", prazoInscricao: "01/02/2027", idioma: "Inglês", tipoIntercambio: "Duplo diploma", vagas: 2 }
      ]
    },
    {
      id: "heidelberg", nome: "Heidelberg University", sigla: "UHD", cidade: "Heidelberg",
      siteOficial: "www.uni-heidelberg.de", ranking: "#87 no ranking global (dado demonstrativo)",
      foto: IMG.campus, endereco: "Grabengasse 1, 69117 Heidelberg", paisId: "alemanha", vagas: 4,
      sobre: "A universidade mais antiga da Alemanha, reconhecida pela tradição em humanidades, direito e ciências da vida.",
      perfilAcademico: "Ambiente acadêmico clássico, com seminários de leitura intensiva e forte produção científica.",
      cursos: ["Direito", "Medicina", "Letras", "História"],
      certificados: ["TestDaF nível 4", "IELTS 6.0"],
      requisitosAcademicos: ["CR mínimo de 7,5", "Nível B2 de alemão para disciplinas regulares"],
      custos: ["Isenção de mensalidade por convênio", "Custo de vida estimado em €900/mês" + emReais("EUR", 900)],
      bolsas: ["DAAD", "Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Carta de motivação", "Passaporte"],
      contato: "exchange@uni-heidelberg.de",
      programas: [
        { id: "uhd-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "2 semestres", prazoInscricao: "30/04/2027", idioma: "Alemão", tipoIntercambio: "Convênio", vagas: 4 }
      ]
    },
    {
      id: "uba", nome: "Universidad de Buenos Aires", sigla: "UBA", cidade: "Buenos Aires",
      siteOficial: "www.uba.ar", ranking: "#71 no ranking global (dado demonstrativo)",
      foto: IMG.argentina, endereco: "Viamonte 430, Buenos Aires", paisId: "argentina", vagas: 8,
      sobre: "Maior universidade pública da Argentina, com ampla oferta de cursos e forte vida acadêmica.",
      perfilAcademico: "Perfil público e plural, com disciplinas em espanhol e grande diversidade de áreas.",
      cursos: ["Direito", "Economia", "Arquitetura", "Comunicação"],
      certificados: ["DELE B1", "CELU intermediário"],
      requisitosAcademicos: ["CR mínimo de 6,0", "Espanhol nível B1"],
      custos: ["Isenção de mensalidade por convênio", "Custo de vida estimado em US$600/mês" + emReais("USD", 600)],
      bolsas: ["Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Passaporte ou RG", "Seguro saúde"],
      contato: "internacionales@uba.ar",
      programas: [
        { id: "uba-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "1 semestre", prazoInscricao: "10/10/2026", idioma: "Espanhol", tipoIntercambio: "Convênio", vagas: 8 }
      ]
    },
    {
      id: "uca", nome: "Pontificia Universidad Católica Argentina", sigla: "UCA", cidade: "Buenos Aires",
      siteOficial: "www.uca.edu.ar", ranking: "Referência regional (dado demonstrativo)",
      foto: IMG.campus, endereco: "Av. Alicia Moreau de Justo 1400, Buenos Aires", paisId: "argentina", vagas: 5,
      sobre: "Universidade católica com forte tradição em ciências sociais, economia e direito.",
      perfilAcademico: "Turmas menores e acompanhamento próximo, com identidade acadêmica semelhante à da PUC-Rio.",
      cursos: ["Administração", "Economia", "Direito", "Psicologia"],
      certificados: ["DELE B1"],
      requisitosAcademicos: ["CR mínimo de 6,5", "Espanhol nível B1"],
      custos: ["Isenção de mensalidade por convênio", "Moradia a partir de US$350/mês"],
      bolsas: ["Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Carta de motivação", "Passaporte ou RG"],
      contato: "intercambio@uca.edu.ar",
      programas: [
        { id: "uca-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "1 semestre", prazoInscricao: "20/10/2026", idioma: "Espanhol", tipoIntercambio: "Convênio", vagas: 5 }
      ]
    },
    {
      id: "salamanca", nome: "Universidad de Salamanca", sigla: "USAL", cidade: "Salamanca",
      siteOficial: "www.usal.es", ranking: "Referência histórica na Europa (dado demonstrativo)",
      foto: IMG.espanha, endereco: "Patio de Escuelas 1, Salamanca", paisId: "espanha", vagas: 6,
      sobre: "Universidade mais antiga da Espanha, referência no ensino de língua espanhola e humanidades.",
      perfilAcademico: "Cidade universitária com ambiente acolhedor e ampla oferta de cursos de língua.",
      cursos: ["Letras", "Direito", "História", "Relações Internacionais"],
      certificados: ["DELE B1", "SIELE 700 pontos"],
      requisitosAcademicos: ["CR mínimo de 6,5", "Espanhol nível B1 comprovado"],
      custos: ["Isenção de mensalidade por convênio", "Custo de vida de €750/mês" + emReais("EUR", 750)],
      bolsas: ["Erasmus+ (mobilidade internacional)", "Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Passaporte", "Comprovante de proficiência"],
      contato: "relint@usal.es",
      programas: [
        { id: "usal-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "2 semestres", prazoInscricao: "15/04/2027", idioma: "Espanhol", tipoIntercambio: "Convênio", vagas: 6 }
      ]
    },
    {
      id: "upm", nome: "Universidad Politécnica de Madrid", sigla: "UPM", cidade: "Madri",
      siteOficial: "www.upm.es", ranking: "Principal politécnica da Espanha (dado demonstrativo)",
      foto: IMG.campus, endereco: "Ramiro de Maeztu 7, Madrid", paisId: "espanha", vagas: 7,
      sobre: "Instituição técnica com forte atuação em engenharia, arquitetura e tecnologia.",
      perfilAcademico: "Currículo técnico com laboratórios e projetos aplicados.",
      cursos: ["Engenharia", "Arquitetura", "Ciência da Computação"],
      certificados: ["DELE B2", "IELTS 6.0"],
      requisitosAcademicos: ["CR mínimo de 7,0", "Espanhol nível B2"],
      custos: ["Isenção de mensalidade por convênio", "Custo de vida de €1.000/mês" + emReais("EUR", 1000)],
      bolsas: ["Erasmus+", "Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Carta de motivação", "Passaporte"],
      contato: "movilidad@upm.es",
      programas: [
        { id: "upm-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "1 semestre", prazoInscricao: "01/05/2027", idioma: "Espanhol", tipoIntercambio: "Convênio", vagas: 4 },
        { id: "upm-2", nivel: "Pós-graduação", custo: "€900 (taxas administrativas)", duracao: "2 semestres", prazoInscricao: "01/03/2027", idioma: "Espanhol / Inglês", tipoIntercambio: "Duplo diploma", vagas: 3 }
      ]
    },
    {
      id: "puc-chile", nome: "Pontificia Universidad Católica de Chile", sigla: "UC", cidade: "Santiago",
      siteOficial: "www.uc.cl", ranking: "#93 no ranking global (dado demonstrativo)",
      foto: IMG.chile, endereco: "Av. Libertador Bernardo O'Higgins 340, Santiago", paisId: "chile", vagas: 6,
      sobre: "Uma das universidades mais bem avaliadas da América Latina, parceira histórica da PUC-Rio.",
      perfilAcademico: "Forte em engenharia, economia e ciências sociais, com campus integrado à cidade.",
      cursos: ["Engenharia", "Economia", "Design", "Ciências Sociais"],
      certificados: ["DELE B1"],
      requisitosAcademicos: ["CR mínimo de 7,0", "Espanhol nível B1"],
      custos: ["Isenção de mensalidade por convênio", "Custo de vida de US$800/mês" + emReais("USD", 800)],
      bolsas: ["Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Passaporte", "Seguro saúde"],
      contato: "intercambio@uc.cl",
      programas: [
        { id: "uc-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "1 semestre", prazoInscricao: "05/10/2026", idioma: "Espanhol", tipoIntercambio: "Convênio", vagas: 6 }
      ]
    },
    {
      id: "uchile", nome: "Universidad de Chile", sigla: "UCH", cidade: "Santiago",
      siteOficial: "www.uchile.cl", ranking: "Referência pública no Chile (dado demonstrativo)",
      foto: IMG.campus, endereco: "Av. Libertador Bernardo O'Higgins 1058, Santiago", paisId: "chile", vagas: 4,
      sobre: "Principal universidade pública chilena, com produção científica reconhecida.",
      perfilAcademico: "Ambiente plural com foco em pesquisa e extensão.",
      cursos: ["Medicina", "Direito", "Engenharia", "Artes"],
      certificados: ["DELE B1"],
      requisitosAcademicos: ["CR mínimo de 6,5", "Espanhol nível B1"],
      custos: ["Isenção de mensalidade por convênio", "Custo de vida de US$700/mês" + emReais("USD", 700)],
      bolsas: ["Bolsa de mobilidade PUC-Rio"],
      documentacao: ["Histórico escolar", "Passaporte"],
      contato: "movilidad@uchile.cl",
      programas: [
        { id: "uch-1", nivel: "Graduação", custo: "Isento (convênio)", duracao: "2 semestres", prazoInscricao: "15/10/2026", idioma: "Espanhol", tipoIntercambio: "Convênio", vagas: 4 }
      ]
    }
  ];

  var cursosDisponiveis = Array.from(new Set(universidades.reduce(function (acc, u) { return acc.concat(u.cursos); }, []))).sort();

  function getPais(id) { return paises.find(function (p) { return p.id === id; }); }
  function getUniversidade(id) { return universidades.find(function (u) { return u.id === id; }); }
  function universidadesDoPais(paisId) { return universidades.filter(function (u) { return u.paisId === paisId; }); }

  var processoSeletivo = {
    atualizadoEm: ULTIMA_ATUALIZACAO,
    indice: [
      { id: "pre-requisitos", label: "Pré-requisitos" },
      { id: "passo-1", label: "Passo 1 → Requisitos" },
      { id: "passo-2", label: "Passo 2 → Custos" },
      { id: "passo-3", label: "Passo 3 → Antes de se inscrever" },
      { id: "passo-4", label: "Passo 4 → Comprovante de Proficiência" },
      { id: "passo-5", label: "Passo 5 → Como se Inscrever" },
      { id: "passo-6", label: "Passo 6 → Banca de Seleção" },
      { id: "passo-7", label: "Passo 7 → Resultado da seleção" },
      { id: "passo-8", label: "Passo 8 → Segunda fase" },
      { id: "passo-9", label: "Passo 9 → Aceitação na Universidade de destino" },
      { id: "passo-10", label: "Passo 10 → Após o aceite" }
    ],
    listaCr: {
      titulo: "Lista de CR",
      colunas: ["Departamento", "Nota de corte"],
      nota: "Base de dados sujeita a variações. Lista de CR / Corte 50% - 2026.2",
      linhas: [
        ["Administração", "7,2"], ["Arquitetura e Urbanismo", "7,8"], ["Artes e Design", "8,73"],
        ["Biologia", "7,54"], ["Ciência da Computação", "6,9"], ["Ciências Sociais", "8,34"],
        ["Comunicação Social", "8,91"], ["Direito", "8,35"], ["Economia", "6,85"],
        ["Educação", "8,79"], ["Engenharia Ciclo Básico", "6,37"], ["Engenharia Ciclo Profissional", "7,37"],
        ["Filosofia", "8,2"], ["Física", "8,2"], ["Geografia e Meio Ambiente", "8,84"],
        ["História", "8,18"], ["Inteligência Artificial", "7,8"], ["Letras", "8,6"],
        ["Matemática", "7,31"], ["Nutrição", "8,09"], ["Psicologia/Neurociência", "8,58"],
        ["Química", "7,68"], ["Relações Internacionais", "8,37"], ["Serviço Social", "9,13"],
        ["Teologia", "9,03"]
      ]
    },
    preRequisitos: {
      id: "pre-requisitos",
      titulo: "Pré-requisitos",
      itens: [
        "Estar regularmente matriculado em um curso de Graduação, Mestrado ou Doutorado da PUC-Rio;",
        "Ter cursado no mínimo 40 créditos na PUC-Rio;",
        "Não completar os estudos durante o intercâmbio;",
        "Ter CR igual ou maior que 7,0*;",
        "Ser classificado entre os 50% melhores alunos do seu Departamento*;",
        "Não possuir mais do que TRÊS reprovações*"
      ],
      nota: "* Caso o candidato não se enquadre nas exigências estipuladas, sua solicitação de inscrição deverá passar por avaliação especial junto à coordenação acadêmica de intercâmbio da CCCI, que julgará o mérito de forma excepcional."
    },
    passos: [
      {
        id: "passo-1", titulo: "Passo 1 - Requisitos",
        blocos: [
          { tipo: "lista-numerada", itens: [
            "Verificar a regularidade acadêmica e financeira junto à PUC-Rio;",
            "Consultar as vagas e requisitos específicos para cada convênio de interesse;",
            "Comprovar o domínio do idioma do país de destino nos níveis mínimos exigidos pelas parceiras;",
            "Estar em conformidade com as orientações do coordenador do respectivo curso de graduação;",
            "Apresentar plano de estudos preliminar validado internamente;",
            "Obter recomendação formal de ao menos um docente permanente de sua faculdade;",
            "Efetuar o pagamento da taxa administrativa CCCI dentro do prazo estabelecido."
          ] },
          { tipo: "nota", texto: "* Algumas instituições parceiras podem aplicar testes adicionais ou exigir comprovação curricular diferenciada que exceda as regras gerais da PUC-Rio. Atente-se às páginas de descrição de cada universidade no portal." }
        ]
      },
      {
        id: "passo-2", titulo: "Passo 2 - Custos",
        blocos: [
          { tipo: "paragrafo", texto: "O aluno em intercâmbio acadêmico internacional promovido pela CCCI PUC-Rio continua isento de mensalidades na instituição estrangeira de acolhimento, devendo obrigatoriamente manter o pagamento de sua respectiva mensalidade/matrícula acadêmica regular na PUC-Rio durante o período de estudos fora." },
          { tipo: "paragrafo", texto: "Os custos relativos a passagens aéreas, alojamento, plano de saúde internacional obrigatório, alimentação e transporte são de responsabilidade integral do estudante." },
          { tipo: "subtitulo", texto: "Países que exigem comprovação financeira rigorosa para emissão de visto:" },
          { tipo: "chips", itens: ["Alemanha", "Bélgica", "Coréia", "Dinamarca", "Estados Unidos", "Holanda", "Noruega", "Nova Zelândia", "Suécia"] },
          { tipo: "nota", texto: "Nota: Verifique oportunidades de bolsas de mobilidade internacional (Santander, Erasmus+, etc.) disponíveis nos editais vigentes da secretaria." }
        ]
      },
      {
        id: "passo-3", titulo: "Passo 3 - Antes de se inscrever",
        blocos: [
          { tipo: "lista-numerada", itens: [
            "Participar das reuniões informativas gerais organizadas pela equipe CCCI;",
            "Verificar seu CR e comparar com a lista de corte histórica dos semestres anteriores;",
            "Fazer o levantamento das grades curriculares das universidades conveniadas desejadas;",
            "Analisar as opções de hospedagem oferecidas (on-campus ou off-campus) e seus respectivos custos estimativos;",
            "Verificar a validade de seu passaporte, que deve ser de no mínimo 6 meses pós-data de retorno prevista;",
            "Pesquisar sobre as exigências de seguro-saúde e vacinas no país de destino;",
            "Alinhar a expectativa de equivalência de créditos com o coordenador pedagógico do seu curso;",
            "Iniciar a elaboração de sua carta de motivação em português e no idioma das aulas internacionais."
          ] }
        ]
      },
      {
        id: "passo-4", titulo: "Passo 4 - Comprovante de Proficiência",
        blocos: [
          { tipo: "caixa", paragrafos: [
            "Para participar do intercâmbio em países que não possuem a língua portuguesa como oficial, o candidato deve comprovar o nível adequado do idioma de instrução exigido pela parceira de acolhimento.",
            "Os comprovantes aceitos e as notas mínimas variam de acordo com as especificidades acadêmicas de cada departamento internacional e país-membro.",
            "Informações sobre comprovantes aceitos estão presentes no site na aba especifica de cada universidade",
            "Caso o aluno pretenda cursar matérias em múltiplos idiomas, deverá anexar as respectivas certificações para cada uma das línguas correspondentes."
          ] },
          { tipo: "subtitulo", texto: "Requisitos de Validade dos Exames:" },
          { tipo: "lista-numerada", itens: [
            "O certificado deve possuir data de emissão de no máximo 2 anos na data de inscrição interna;",
            "Não serão aceitos prints de telas de resultados preliminares sem assinatura ou código verificador eletrônico;",
            "Certificados fora do prazo de validade oficial da certificadora não serão processados pela banca de seleção;",
            "O envio do PDF oficial deve ser feito exclusivamente via upload na área do candidato."
          ] },
          { tipo: "subtitulo", texto: "Certificados de inglês aceitos:" },
          { tipo: "lista", itens: ["TOEFL-IBT, IELTS, CIP, Duolingo, Pearson, Cambridge, IB."] },
          { tipo: "tabela", colunas: ["Certificado", "Pontuação Mínima"], linhas: [
            ["TOEFL IBT", "80"], ["IELTS", "6.5"], ["CIP", "B2"], ["Duolingo", "110"],
            ["Pearson", "58"], ["Cambridge", "FCE"], ["IB", "35"]
          ] },
          { tipo: "nota", texto: "* Atenção: Algumas universidades exigem pontuações mínimas específicas (subscores) por seção do exame (reading, writing, speaking, listening)." },
          { tipo: "cards", itens: [
            { titulo: "Inglês", texto: "TOEFL, IELTS ou Duolingo. Exigido pela maioria das universidades norte-americanas, europeias e asiáticas." },
            { titulo: "Espanhol", texto: "DELE ou teste de proficiência próprio aceito por instituições da Espanha e América Latina." },
            { titulo: "Francês", texto: "DELF/DALF mínimo B2 para acompanhar aulas regulares em universidades francesas conveniadas." },
            { titulo: "Alemão", texto: "Goethe-Zertifikat ou TestDaF. Muitas instituições alemãs oferecem cursos também em inglês." },
            { titulo: "Chinês", texto: "HSK nível 4 ou superior para cursos em mandarim, ou comprovação de inglês para cursos internacionais." },
            { titulo: "Japonês", texto: "JLPT N2 para cursos gerais, ou comprovação de proficiência em inglês para programas especiais de intercâmbio." }
          ] }
        ]
      },
      {
        id: "passo-5", titulo: "Passo 5 - Como se Inscrever",
        blocos: [
          { tipo: "lista-numerada", itens: [
            "Acessar o portal eletrônico de inscrições CCCI da PUC-Rio dentro do prazo de chamada ativa;",
            "Preencher o cadastro inicial com dados acadêmicos e contatos atualizados;",
            "Selecionar até 3 opções de universidades de destino por ordem de preferência pessoal;",
            "Fazer upload de toda a documentação comprobatória exigida em formato PDF unificado;",
            "Anexar os comprovantes válidos de proficiência linguística exigidos por cada opção selecionada;",
            "Concluir o processo de envio e guardar o comprovante eletrônico de submissão do protocolo."
          ] },
          { tipo: "destaque", texto: "Prazo impreterível: Não serão admitidas alterações após o encerramento do sistema na data-limite oficial do edital." }
        ]
      },
      {
        id: "passo-6", titulo: "Passo 6 - Banca de Seleção",
        blocos: [
          { tipo: "paragrafo", texto: "A banca examinadora, composta por docentes indicados pelos departamentos acadêmicos correspondentes e assessores internacionais da CCCI, avaliará de forma integrada o perfil global do estudante com base nos critérios regimentais de mérito." },
          { tipo: "subtitulo", texto: "Critérios e expectativas avaliados na entrevista:" },
          { tipo: "lista", itens: [
            "Demonstração clara de maturidade psicossocial para vivência em ambiente multicultural;",
            "Consistência acadêmica na argumentação de escolha das disciplinas do plano de estudos;",
            "Habilidade de comunicação oral e fluidez de raciocínio no idioma oficial de destino;",
            "Alinhamento dos objetivos pessoais e de carreira com o plano de mobilidade apresentado;",
            "Postura embaixadora ética para representação institucional da PUC-Rio no exterior."
          ] }
        ]
      },
      {
        id: "passo-7", titulo: "Passo 7 - Resultado da seleção",
        blocos: [
          { tipo: "paragrafo", texto: "O resultado oficial da primeira fase de alocação de vagas será publicado no site oficial da CCCI e disponibilizado de forma individual no portal de acompanhamento do candidato." },
          { tipo: "paragrafo", texto: "Os candidatos classificados receberão as orientações iniciais por e-mail para confirmação de interesse na vaga concedida." },
          { tipo: "subtitulo", texto: "Regras em caso de Desistência:" },
          { tipo: "lista", itens: [
            "A desistência formal deve ser formalizada imediatamente via protocolo digital no portal da CCCI;",
            "O não preenchimento do termo de aceite de alocação no prazo de 48h implicará em desistência automática;",
            "O abandono da vaga sem justificativa formal homologada pela coordenação poderá acarretar sanções acadêmicas."
          ] }
        ]
      },
      {
        id: "passo-8", titulo: "Passo 8 - Segunda fase",
        blocos: [
          { tipo: "paragrafo", texto: "Parabéns! Na segunda fase do processo seletivo, o aluno inicia a preparação da candidatura direta junto à instituição de destino." },
          { tipo: "subtitulo", texto: "Documentos Obrigatórios da Segunda Fase:" },
          { tipo: "lista-numerada", itens: [
            "Formulário oficial de aplicação da instituição internacional de acolhimento;",
            "Histórico escolar oficial em inglês ou idioma de destino emitido pela DAR PUC-Rio;",
            "Carta de indicação oficial assinada pela assessoria acadêmica da CCCI;",
            "Declaração de suporte financeiro ou comprovação de recursos mínimos exigidos para subsistência;",
            "Cópia legível da folha de identificação do passaporte dentro do padrão de validade;",
            "Laudo médico oficial internacional com histórico vacinal (se exigido pela parceira);",
            "Plano de estudos final acordado e validado pelo coordenador de departamento."
          ] }
        ]
      },
      {
        id: "passo-9", titulo: "Passo 9 - Aceitação na Universidade de destino",
        blocos: [
          { tipo: "lista-numerada", itens: [
            "Aguardar a análise documental realizada pelo comitê de admissões da instituição parceira;",
            "Acompanhar eventuais pedidos de correções ou documentos adicionais via e-mail acadêmico;",
            "Receber a Carta de Aceite Oficial (Letter of Acceptance) emitida pela instituição parceira;",
            "Validar a recepção do documento digital ou a chegada do documento físico na secretaria da CCCI;",
            "Efetivar o preenchimento da ficha cadastral de pré-embarque exigida pela PUC-Rio;",
            "Iniciar imediatamente os trâmites do processo de obtenção do visto consular correspondente;",
            "Contratar o plano de seguro-saúde internacional com cobertura integral contra acidentes e enfermidades."
          ] },
          { tipo: "subtitulo", texto: "Casos de recusa ou desistência:" },
          { tipo: "lista", itens: [
            "Se a parceira recusar a candidatura por falta de vagas, o aluno poderá solicitar remanejamento de emergência;",
            "O cancelamento do intercâmbio após a emissão do aceite internacional requer devolução formal da carta oficial;",
            "Taxas administrativas desembolsadas à CCCI ou taxas externas não são reembolsadas em caso de desistência tardia."
          ] }
        ]
      },
      {
        id: "passo-10", titulo: "Passo 10 - Após o aceite",
        blocos: [
          { tipo: "subtitulo", texto: "1. Trâmites do Visto e Entrada no País de Destino:" },
          { tipo: "lista", itens: [
            "Agendar a entrevista no consulado de destino assim que receber a Carta de Aceite;",
            "Apresentar a comprovação financeira em conformidade com as regras oficiais do país;",
            "Adquirir as passagens aéreas somente após a confirmação final do visto no passaporte;",
            "Atentar-se para as exigências específicas de vacinação e quarentena das autoridades sanitárias locais."
          ] },
          { tipo: "subtitulo", texto: "2. Confirmações Acadêmicas PUC-Rio:" },
          { tipo: "lista", itens: [
            "Assinar o Termo de Compromisso e Responsabilidade de Mobilidade Internacional junto à CCCI;",
            "Efetuar a matrícula em regime especial de intercâmbio no sistema acadêmico da PUC-Rio;",
            "Entregar cópia do seguro de saúde internacional contratado com cobertura de repatriação;",
            "Fornecer detalhes atualizados de contato e endereço de moradia no exterior à coordenação."
          ] },
          { tipo: "caixa", paragrafos: [
            "Observações Importantes sobre Desistência Pré-embarque:",
            "A desistência após o recebimento do visto internacional ou próximo à data prevista do embarque deve ser imediatamente informada à CCCI por escrito, anexando justificativa formal fundamentada. Casos de omissão serão encaminhados para a respectiva vice-reitoria acadêmica para avaliação e aplicação de eventuais advertências."
          ] }
        ]
      }
    ]
  };

  var faq = [
    { pergunta: "Posso fazer intercâmbio em qualquer período do curso?", resposta: "É necessário ter concluído ao menos dois períodos na PUC-Rio e não estar no último semestre do curso." },
    { pergunta: "A mensalidade da PUC-Rio continua sendo paga?", resposta: "Nos convênios de isenção, o aluno mantém o vínculo e a mensalidade na PUC-Rio e não paga mensalidade no destino." },
    { pergunta: "As disciplinas cursadas fora são aproveitadas?", resposta: "Sim, mediante análise de equivalência feita pelo coordenador do curso na volta do intercâmbio." },
    { pergunta: "Existe bolsa para o intercâmbio?", resposta: "Há bolsas parciais e programas externos, como DAAD e Erasmus+, conforme o edital vigente." }
  ];

  var contato = {
    endereco: ["Rua Marquês de São Vicente, 225", "Gávea, Rio de Janeiro - RJ", "Edifício Cardeal Leme, Sala 130"],
    email: ["ccci-puc@puc-rio.br", "info.ccci@puc-rio.br", "intercambio@puc-rio.br"],
    telefone: ["+55 (21) 3527-1577", "+55 (21) 3527-1578", "Fax: ramal 1579"],
    instagram: ["@ccci_pucrio", "#PUCRioIntercambio", "Updates e editais ativos"],
    horario: ["Segunda a Sexta-feira", "9h00 às 12h00", "14h00 às 17h00"]
  };
  var blocosContato = [
    { titulo: "Endereço", linhas: contato.endereco },
    { titulo: "Email", linhas: contato.email },
    { titulo: "Telefone", linhas: contato.telefone },
    { titulo: "Instagram", linhas: contato.instagram },
    { titulo: "Horário de funcionamento", linhas: contato.horario }
  ];

  /* ================================================================
     FÓRUM (src/lib/forum-store.ts) — salvo neste navegador
     ================================================================ */
  var seedPosts = [
    { id: "p1", author: "Mariana Costa", course: "Engenharia de Produção", title: "Como é o processo de matrícula na TUM?", description: "Fui nomeada para a Technical University of Munich e estou com dúvidas sobre o prazo de escolha das disciplinas e o registro no sistema deles. Alguém já passou por isso?", createdAt: "12/08/2026", tags: ["Alemanha", "Europa", "Matrícula"], upvotes: 24 },
    { id: "p2", author: "Rafael Lima", course: "Relações Internacionais", title: "Alguém já fez intercâmbio na UBA?", description: "Queria saber como funciona a vida acadêmica na Universidad de Buenos Aires, principalmente carga horária e moradia perto da faculdade.", createdAt: "05/08/2026", tags: ["Argentina", "América do Sul"], upvotes: 17 },
    { id: "p3", author: "Beatriz Nunes", course: "Letras", title: "Qual nível de proficiência em espanhol exigido na Universidad de Salamanca?", description: "Tenho DELE B1 e estou em dúvida se é suficiente para as disciplinas regulares ou se preciso subir para B2 antes da inscrição.", createdAt: "28/07/2026", tags: ["Espanha", "Europa", "Proficiência"], upvotes: 11 },
    { id: "p4", author: "Lucas Andrade", course: "Direito", title: "Visto de estudante para a Alemanha: quanto tempo demora?", description: "Estou organizando a documentação e a comprovação financeira. Quanto tempo levou entre o agendamento no consulado e a emissão do visto?", createdAt: "20/07/2026", tags: ["Alemanha", "Visto"], upvotes: 9 },
    { id: "p5", author: "Camila Ferreira", course: "Administração", title: "Vale a pena escolher duplo diploma?", description: "Estou entre um semestre de convênio e um programa de duplo diploma de dois semestres. Como foi a experiência de quem escolheu o duplo diploma?", createdAt: "14/07/2026", tags: ["Europa", "Duplo diploma"], upvotes: 15 },
    { id: "p6", author: "Pedro Henrique", course: "Ciência da Computação", title: "Moradia estudantil em Santiago: como conseguir?", description: "Fui aceito na UC Chile e queria dicas de bairros e de como funciona a residência universitária por lá.", createdAt: "02/07/2026", tags: ["Chile", "Moradia"], upvotes: 7 }
  ];
  var seedComments = [
    { id: "c1", postId: "p1", parentCommentId: null, author: "João Vitor", content: "A matrícula é feita no TUMonline. Você recebe o login junto com a carta de aceite e escolhe as disciplinas nas primeiras duas semanas do semestre.", createdAt: "13/08/2026", upvotes: 12 },
    { id: "c2", postId: "p1", parentCommentId: "c1", author: "Mariana Costa", content: "Perfeito, obrigada! E o prazo de troca de disciplinas é o mesmo?", createdAt: "13/08/2026", upvotes: 3 },
    { id: "c3", postId: "p1", parentCommentId: null, author: "Ana Paula", content: "Vale conferir também o Welcome Week: eles explicam o sistema de créditos e o seguro saúde obrigatório.", createdAt: "14/08/2026", upvotes: 6 },
    { id: "c4", postId: "p2", parentCommentId: null, author: "Gabriel Rocha", content: "Fiz um semestre na UBA. A carga horária é puxada, mas o custo de vida ajuda bastante. Recomendo morar em Recoleta ou Palermo.", createdAt: "06/08/2026", upvotes: 8 },
    { id: "c5", postId: "p3", parentCommentId: null, author: "Coordenação CCCI", content: "O convênio com Salamanca aceita B1 para disciplinas regulares, mas algumas cadeiras específicas pedem B2. Confira a lista no site da instituição.", createdAt: "29/07/2026", upvotes: 14 }
  ];

  var STORE_KEY = "rotapuc-forum-v1";
  function clone(x) { return JSON.parse(JSON.stringify(x)); }
  function seedForum() { return { posts: clone(seedPosts), comments: clone(seedComments), votedPosts: [] }; }
  function loadForum() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      if (raw) {
        var s = JSON.parse(raw);
        if (s && Array.isArray(s.posts) && Array.isArray(s.comments)) {
          return { posts: s.posts, comments: s.comments, votedPosts: Array.isArray(s.votedPosts) ? s.votedPosts : [] };
        }
      }
    } catch (e) { /* armazenamento indisponível: usa dados de exemplo */ }
    return seedForum();
  }
  var forum = loadForum();
  function saveForum() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(forum)); } catch (e) { /* segue só em memória */ }
  }
  function hoje() { return new Date().toLocaleDateString("pt-BR"); }
  function uid(prefix) { return prefix + Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }

  function addPost(input) {
    var id = uid("p");
    forum.posts.unshift({ id: id, author: "Você", course: "Aluno PUC-Rio", title: input.title, description: input.description, createdAt: hoje(), tags: input.tags, upvotes: 0 });
    saveForum();
    return id;
  }
  function addComment(postId, content, parentCommentId) {
    forum.comments.push({ id: uid("c"), postId: postId, parentCommentId: parentCommentId || null, author: "Você", content: content, createdAt: hoje(), upvotes: 0 });
    saveForum();
  }
  function togglePostUpvote(postId) {
    var voted = forum.votedPosts.indexOf(postId) !== -1;
    forum.votedPosts = voted ? forum.votedPosts.filter(function (id) { return id !== postId; }) : forum.votedPosts.concat(postId);
    forum.posts.forEach(function (p) { if (p.id === postId) p.upvotes += voted ? -1 : 1; });
    saveForum();
  }
  function commentsOf(postId) { return forum.comments.filter(function (c) { return c.postId === postId && !c.parentCommentId; }); }
  function repliesOf(commentId) { return forum.comments.filter(function (c) { return c.parentCommentId === commentId; }); }
  function totalRespostas(postId) { return forum.comments.filter(function (c) { return c.postId === postId; }).length; }
  function initials(name) {
    return name.split(" ").slice(0, 2).map(function (n) { return n.charAt(0); }).join("").toUpperCase();
  }

  /* ================================================================
     UTILITÁRIOS DE INTERFACE
     ================================================================ */
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function map(arr, fn) { return arr.map(fn).join(""); }
  function plural(n, um, varios) { return n + " " + (n === 1 ? um : varios); }
  function reduceMotion() {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  var ICONS = {
    search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    chevronDown: '<path d="m6 9 6 6 6-6"/>',
    chevronRight: '<path d="m9 18 6-6-6-6"/>',
    message: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    plus: '<path d="M5 12h14"/><path d="M12 5v14"/>',
    arrowUp: '<path d="M9 18v-6H5l7-7 7 7h-4v6H9z"/>',
    arrowLeft: '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    instagram: '<rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>',
    facebook: '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    youtube: '<path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>'
  };
  function icon(name, size, cls) {
    return '<svg class="icon ' + (cls || "") + '" width="' + (size || 16) + '" height="' + (size || 16) + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ICONS[name] + "</svg>";
  }

  function pill(t, cls) { return '<span class="pill ' + (cls || "") + '">' + esc(t) + "</span>"; }
  function sectionTitle(t, cls, id) { return '<h2 class="section-title ' + (cls || "") + '"' + (id ? ' id="' + id + '"' : "") + ">" + esc(t) + "</h2>"; }
  function chip(t) { return '<span class="chip">' + esc(t) + "</span>"; }
  function bullets(itens) { return '<ul class="bullets">' + map(itens, function (i) { return "<li>" + esc(i) + "</li>"; }) + "</ul>"; }
  function infoCard(title, body) { return '<div class="card info-card"><h3>' + esc(title) + '</h3><div class="info-body">' + body + "</div></div>"; }
  function emptyState(title, desc) { return '<div class="empty"><p class="empty-title">' + esc(title) + '</p><p class="empty-desc">' + esc(desc) + "</p></div>"; }
  function updatedAt(d) { return '<p class="updated">Última atualização: ' + esc(d) + " · Dados demonstrativos do protótipo</p>"; }
  function avatar(name, cls) { return '<span class="avatar ' + (cls || "") + '" aria-hidden="true">' + esc(initials(name)) + "</span>"; }

  function universityCard(u) {
    return '<article class="card card-hover uni-card">' +
      '<img src="' + u.foto + '" alt="Campus da ' + esc(u.nome) + '" loading="lazy" width="1200" height="800">' +
      '<div class="uni-card-body">' +
        "<h3>" + esc(u.nome) + "</h3>" +
        '<p class="muted-sm">' + esc(u.cidade) + "</p>" +
        '<a class="site-link" href="https://' + esc(u.siteOficial) + '" target="_blank" rel="noreferrer">' + esc(u.siteOficial) + "</a>" +
        '<a class="btn btn-primary" href="#/universidades/' + u.id + '">Saiba mais</a>' +
      "</div></article>";
  }
  function countryCard(p) {
    var n = universidadesDoPais(p.id).length;
    return '<a class="card card-hover country-card" href="#/paises/' + p.id + '">' +
      '<img src="' + p.imagem + '" alt="Paisagem representativa: ' + esc(p.nome) + '" loading="lazy" width="1200" height="800">' +
      '<div class="body"><h3>' + esc(p.nome) + '</h3><p class="muted-sm">' + plural(n, "universidade conveniada", "universidades conveniadas") + "</p></div></a>";
  }
  function threadCard(post) {
    var n = totalRespostas(post.id);
    return '<a class="card card-hover thread" href="#/forum/' + post.id + '">' +
      "<h3>" + esc(post.title) + "</h3>" +
      '<p class="muted-sm desc clamp-2">' + esc(post.description) + "</p>" +
      '<div class="meta">' + avatar(post.author) +
        '<span class="who">' + esc(post.author) + "</span><span>·</span><span>" + esc(post.createdAt) + "</span>" +
        '<span class="push"><span class="votes">' + icon("arrowUp", 16) + post.upvotes + "</span>" +
        '<span class="votes">' + icon("message", 16) + plural(n, "resposta", "respostas") + "</span></span>" +
      "</div></a>";
  }

  var toastTimer = null;
  function toast(msg) {
    var el = document.getElementById("toast");
    el.innerHTML = icon("check", 16) + "<span>" + esc(msg) + "</span>";
    el.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.classList.remove("show"); }, 2600);
  }

  function scrollToId(id) {
    var el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: reduceMotion() ? "auto" : "smooth", block: "start" });
  }

  /* Estado de interface preservado entre telas */
  var ui = {
    slide: 0,
    uni: { termo: "", continente: TODOS, lingua: TODOS, nivel: TODOS, duracao: TODOS, curso: TODOS, tipo: TODOS, expandidos: [] },
    paisesExpandidos: [],
    forumPage: 0,
    drafts: {},
    openReplies: {},
    nova: { titulo: "", descricao: "", tags: [], erros: {} }
  };

  /* ================================================================
     TELAS
     ================================================================ */

  /* ---- Início ---- */
  var banners = [
    { titulo: "Inscrições abertas para o semestre de outono", texto: "Confira os prazos e a documentação exigida no processo seletivo.", to: "/processo-seletivo", cta: "Ver processo seletivo" },
    { titulo: "Mais de 40 universidades conveniadas", texto: "Filtre por continente, idioma, nível, duração, curso e tipo.", to: "/universidades", cta: "Buscar universidades" },
    { titulo: "Converse com quem já foi", texto: "Tire dúvidas na comunidade de intercâmbio da PUC-Rio.", to: "/forum", cta: "Ir para o fórum" }
  ];
  function bannerHtml() {
    var b = banners[ui.slide] || banners[0];
    return '<div class="banner" id="banner">' +
      '<div class="banner-text" id="banner-text"><h2>' + esc(b.titulo) + "</h2><p>" + esc(b.texto) + "</p></div>" +
      '<div class="banner-row"><a class="btn btn-primary" id="banner-cta" href="#' + b.to + '">' + esc(b.cta) + "</a>" +
      '<div class="dots">' + map(banners, function (x, i) {
        return '<button type="button" class="dot" data-slide="' + i + '" aria-label="Mostrar destaque ' + (i + 1) + '" aria-current="' + (i === ui.slide) + '"></button>';
      }) + "</div></div></div>";
  }
  function viewHome() {
    return {
      title: "RotaPUC | Intercâmbio acadêmico da PUC-Rio",
      html:
        '<section class="hero">' +
          '<img src="' + IMG.hero + '" alt="Estudantes da PUC-Rio caminhando por um campus internacional" width="1600" height="912">' +
          '<div class="hero-overlay"></div>' +
          '<div class="container hero-content">' +
            pill("Intercâmbio PUC-Rio") +
            '<h1 class="hero-title">Seu intercâmbio começa aqui</h1>' +
            '<p class="hero-text">Descubra países parceiros, universidades conveniadas e todas as etapas do processo seletivo em um único lugar.</p>' +
            '<div class="hero-actions"><a class="btn btn-primary btn-lg" href="#/universidades">Buscar universidades</a>' +
            '<a class="btn btn-white btn-lg" href="#/paises">Ver países parceiros</a></div>' +
          "</div></section>" +
        '<div class="container py-48" id="banner-slot">' + bannerHtml() + "</div>" +
        '<div class="container pb-48">' +
          '<div class="center">' + pill("Países parceiros") + "</div>" +
          sectionTitle("Escolha seu destino", "mt-24 text-center") +
          '<div class="grid-2 mt-32">' + map(paises, countryCard) + "</div>" +
        "</div>",
      mount: function (root) {
        var slot = root.querySelector("#banner-slot");
        slot.addEventListener("click", function (e) {
          var d = e.target.closest("[data-slide]");
          if (!d) return;
          ui.slide = Number(d.getAttribute("data-slide"));
          slot.innerHTML = bannerHtml();
          var btn = slot.querySelector('[data-slide="' + ui.slide + '"]');
          if (btn) btn.focus();
        });
      }
    };
  }

  /* ---- Universidades ---- */
  var FILTROS = [
    { key: "continente", label: "Continente", options: ["Europa", "América do Sul"] },
    { key: "lingua", label: "Línguas", options: ["Alemão", "Inglês", "Espanhol"] },
    { key: "nivel", label: "Nível", options: ["Graduação", "Pós-graduação"] },
    { key: "duracao", label: "Duração", options: ["1 semestre", "2 semestres"] },
    { key: "curso", label: "Curso", options: cursosDisponiveis },
    { key: "tipo", label: "Tipo", options: ["Convênio", "Duplo diploma", "Verão"] }
  ];
  function filtrarUniversidades() {
    var f = ui.uni;
    var t = f.termo.trim().toLowerCase();
    return universidades.filter(function (u) {
      var pais = getPais(u.paisId);
      if (t && (u.nome + " " + u.sigla + " " + u.cidade + " " + pais.nome).toLowerCase().indexOf(t) === -1) return false;
      if (f.continente !== TODOS && pais.continente !== f.continente) return false;
      if (f.curso !== TODOS && u.cursos.indexOf(f.curso) === -1) return false;
      if (f.lingua !== TODOS && !u.programas.some(function (p) { return p.idioma.indexOf(f.lingua) !== -1; })) return false;
      if (f.nivel !== TODOS && !u.programas.some(function (p) { return p.nivel === f.nivel; })) return false;
      if (f.duracao !== TODOS && !u.programas.some(function (p) { return p.duracao === f.duracao; })) return false;
      if (f.tipo !== TODOS && !u.programas.some(function (p) { return p.tipoIntercambio === f.tipo; })) return false;
      return true;
    });
  }
  function filtrosAtivos() {
    return ui.uni.termo.trim() !== "" || FILTROS.some(function (f) { return ui.uni[f.key] !== TODOS; });
  }
  function uniResultsHtml() {
    var res = filtrarUniversidades();
    var grupos = paises.map(function (p) {
      return { pais: p, lista: res.filter(function (u) { return u.paisId === p.id; }) };
    }).filter(function (g) { return g.lista.length > 0; });

    var head = '<div class="results-head"><p class="muted-sm" aria-live="polite">' +
      res.length + " universidade(s) encontrada(s)</p>" +
      (filtrosAtivos() ? '<button type="button" class="link-btn" data-action="limpar">Limpar filtros</button>' : "") + "</div>";

    if (!grupos.length) {
      return head + '<div class="mt-32">' + emptyState("Nenhuma universidade encontrada", "Não encontramos universidades com esses critérios. Tente ampliar ou remover algum filtro.") + "</div>";
    }
    return head + '<div class="groups">' + map(grupos, function (g) {
      var aberto = ui.uni.expandidos.indexOf(g.pais.id) !== -1;
      var visiveis = aberto ? g.lista : g.lista.slice(0, 2);
      return '<section aria-label="' + esc(g.pais.nome) + '"><div class="group-head">' +
        '<a href="#/paises/' + g.pais.id + '" class="pill pill-link" title="Ver guia do país">' + esc(g.pais.nome) + "</a>" +
        (g.lista.length > 2 ? '<button type="button" class="link-btn" data-expand="' + g.pais.id + '" aria-expanded="' + aberto + '">' + (aberto ? "Ver menos" : "Ver mais") + icon("chevronDown", 16, "chev") + "</button>" : "") +
        '</div><div class="grid-2 mt-24">' + map(visiveis, universityCard) + "</div></section>";
    }) + "</div>";
  }
  function viewUniversidades() {
    var f = ui.uni;
    return {
      title: "Universidades parceiras | RotaPUC",
      html:
        '<section class="filters-hero"><div class="container">' +
          pill("Universidades conveniadas") +
          '<h1 class="page-title mt-16">Encontre sua universidade</h1>' +
          '<div class="filters">' +
            '<label class="field" for="busca"><span class="field-label">Busca universidade</span>' +
              '<span class="search-wrap">' + icon("search", 16) +
              '<input type="search" id="busca" class="input-pill" placeholder="Nome, cidade ou país" autocomplete="off" value="' + esc(f.termo) + '"></span></label>' +
            '<div class="selects">' + map(FILTROS, function (flt) {
              var val = f[flt.key];
              return '<label class="field" for="f-' + flt.key + '"><span class="field-label">' + flt.label + "</span>" +
                '<select id="f-' + flt.key + '" class="select-pill' + (val !== TODOS ? " is-set" : "") + '" data-filter="' + flt.key + '">' +
                map([TODOS].concat(flt.options), function (o) {
                  return '<option value="' + esc(o) + '"' + (o === val ? " selected" : "") + ">" + esc(o) + "</option>";
                }) + "</select></label>";
            }) + "</div>" +
          "</div>" +
        "</div></section>" +
        '<div class="container py-48" id="uni-results">' + uniResultsHtml() + "</div>",
      mount: function (root) {
        var results = root.querySelector("#uni-results");
        function refresh() { results.innerHTML = uniResultsHtml(); }
        root.querySelector("#busca").addEventListener("input", function (e) { ui.uni.termo = e.target.value; refresh(); });
        root.querySelectorAll("select[data-filter]").forEach(function (s) {
          s.addEventListener("change", function () {
            ui.uni[s.getAttribute("data-filter")] = s.value;
            s.classList.toggle("is-set", s.value !== TODOS);
            refresh();
          });
        });
        results.addEventListener("click", function (e) {
          var exp = e.target.closest("[data-expand]");
          if (exp) {
            var id = exp.getAttribute("data-expand");
            var i = ui.uni.expandidos.indexOf(id);
            if (i === -1) ui.uni.expandidos.push(id); else ui.uni.expandidos.splice(i, 1);
            refresh();
            return;
          }
          if (e.target.closest('[data-action="limpar"]')) {
            ui.uni = { termo: "", continente: TODOS, lingua: TODOS, nivel: TODOS, duracao: TODOS, curso: TODOS, tipo: TODOS, expandidos: [] };
            render({ scroll: false });
            var busca = document.getElementById("busca");
            if (busca) busca.focus();
          }
        });
      }
    };
  }

  function viewUniversidade(id) {
    var u = getUniversidade(id);
    if (!u) return viewNotFound("Universidade não encontrada", "Não encontramos essa universidade entre os convênios da PUC-Rio.", "#/universidades", "Ver universidades");
    var pais = getPais(u.paisId);
    return {
      title: u.nome + " | RotaPUC",
      html:
        '<div class="container py-40">' +
          '<nav class="breadcrumb" aria-label="Você está em"><a href="#/universidades">Universidades</a>' + icon("chevronRight", 14) +
          '<a href="#/paises/' + pais.id + '">' + esc(pais.nome) + "</a>" + icon("chevronRight", 14) + "<span>" + esc(u.sigla) + "</span></nav>" +
          pill(u.sigla) +
          '<h1 class="page-title mt-16">' + esc(u.nome) + "</h1>" +
          '<p class="lead mt-8">' + esc(u.cidade) + ' · <a class="text-link" href="#/paises/' + pais.id + '">' + esc(pais.nome) + "</a></p>" +
          '<img class="detail-hero" style="height:320px" src="' + u.foto + '" alt="Campus da ' + esc(u.nome) + '" width="1200" height="800">' +
          '<div class="grid-2 mt-32">' +
            infoCard("Sobre a universidade",
              "<p>" + esc(u.sobre) + "</p>" +
              '<p class="spaced">Endereço: ' + esc(u.endereco) + "</p>" +
              "<p>Ranking: " + esc(u.ranking) + "</p>" +
              '<p>Site oficial: <a class="text-link" href="https://' + esc(u.siteOficial) + '" target="_blank" rel="noreferrer">' + esc(u.siteOficial) + "</a></p>" +
              "<p>Vagas disponíveis: " + u.vagas + "</p>") +
            infoCard("Perfil acadêmico",
              "<p>" + esc(u.perfilAcademico) + '</p><div class="chips spaced">' + map(u.cursos, chip) + "</div>") +
          "</div>" +
          sectionTitle("Programas", "mt-48") +
          '<div class="table-wrap mt-24"><table><caption class="sr-only">Programas oferecidos pela ' + esc(u.nome) + "</caption>" +
            "<thead><tr>" + map(["Nível", "Tipo", "Duração", "Idioma", "Custo", "Prazo", "Vagas"], function (h) { return '<th scope="col">' + h + "</th>"; }) + "</tr></thead>" +
            "<tbody>" + map(u.programas, function (p) {
              return "<tr><td>" + esc(p.nivel) + "</td><td>" + esc(p.tipoIntercambio) + "</td><td>" + esc(p.duracao) + "</td><td>" + esc(p.idioma) +
                "</td><td>" + esc(p.custo) + "</td><td>" + esc(p.prazoInscricao) + "</td><td>" + p.vagas + "</td></tr>";
            }) + "</tbody></table></div>" +
          '<div class="grid-2 mt-48">' +
            infoCard("Requisitos acadêmicos", bullets(u.requisitosAcademicos) + '<div class="mt-16">' + updatedAt(ULTIMA_ATUALIZACAO) + "</div>") +
            infoCard("Certificados de aptidão e línguas aceitos", bullets(u.certificados)) +
            infoCard("Custos e bolsas", bullets(u.custos.concat(u.bolsas)) + notaCotacao(u.custos)) +
            infoCard("Documentação necessária", bullets(u.documentacao)) +
          "</div>" +
          '<div class="mt-24">' + infoCard("Contato com a instituição", "<p>" + esc(u.contato) + "</p>") + "</div>" +
          '<div class="testimonials"><h3>Depoimentos</h3><p class="muted-sm mt-8">Ainda não há depoimentos publicados para esta universidade. Relatos de ex-intercambistas serão exibidos aqui após moderação da coordenação.</p></div>' +
        "</div>"
    };
  }

  /* ---- Países ---- */
  var continentes = ["Europa", "América do Sul"];
  function viewPaises() {
    function conteudo() {
      return map(continentes, function (c) {
        var lista = paises.filter(function (p) { return p.continente === c; });
        var aberto = ui.paisesExpandidos.indexOf(c) !== -1;
        var visiveis = aberto ? lista : lista.slice(0, 2);
        return '<section><div class="group-head">' + sectionTitle(c) +
          (lista.length > 2 ? '<button type="button" class="link-btn" data-expand="' + esc(c) + '" aria-expanded="' + aberto + '">' + (aberto ? "Ver menos" : "Ver mais") + icon("chevronDown", 16, "chev") + "</button>" : "") +
          '</div><div class="grid-2 mt-24">' + map(visiveis, countryCard) + "</div></section>";
      });
    }
    return {
      title: "Países parceiros | RotaPUC",
      html:
        '<div class="container py-48">' +
          '<div class="center">' + pill("Guia de destinos") + "</div>" +
          '<h1 class="page-title text-center mt-24">Países Parceiros</h1>' +
          '<p class="lead centered mt-12">Explore os destinos com convênio ativo da PUC-Rio e veja quantas universidades estão disponíveis em cada país.</p>' +
          '<div class="groups mt-48" id="paises-list" style="gap:56px">' + conteudo() + "</div>" +
        "</div>",
      mount: function (root) {
        var list = root.querySelector("#paises-list");
        list.addEventListener("click", function (e) {
          var b = e.target.closest("[data-expand]");
          if (!b) return;
          var c = b.getAttribute("data-expand");
          var i = ui.paisesExpandidos.indexOf(c);
          if (i === -1) ui.paisesExpandidos.push(c); else ui.paisesExpandidos.splice(i, 1);
          list.innerHTML = conteudo();
        });
      }
    };
  }

  function viewPais(id) {
    var pais = getPais(id);
    if (!pais) return viewNotFound("País não encontrado", "Esse destino ainda não faz parte dos convênios da PUC-Rio.", "#/paises", "Ver países parceiros");
    var lista = universidadesDoPais(pais.id);
    return {
      title: pais.nome + " | Destinos RotaPUC",
      html:
        '<div class="container py-40">' +
          '<nav class="breadcrumb" aria-label="Você está em"><a href="#/paises">Países</a>' + icon("chevronRight", 14) + "<span>" + esc(pais.nome) + "</span></nav>" +
          pill(pais.nome) +
          '<h1 class="sr-only">' + esc(pais.nome) + "</h1>" +
          '<img class="detail-hero" style="height:340px" src="' + pais.imagem + '" alt="Paisagem representativa: ' + esc(pais.nome) + '" width="1200" height="800">' +
          '<div class="grid-2 mt-32">' +
            '<div class="stack">' +
              infoCard("Idiomas", "<p>" + esc(pais.idiomaOficial) + "</p>") +
              infoCard("Moeda", "<p>" + esc(pais.moeda) + "</p>") +
              infoCard("Fuso-horário", "<p>" + esc(pais.fusoHorario) + "</p>") +
            "</div>" +
            '<div class="stack">' +
              infoCard("Requisitos de entrada", bullets(pais.requisitosParaEntrar) + '<div class="mt-16">' + updatedAt(ULTIMA_ATUALIZACAO) + "</div>") +
              infoCard("Informações adicionais", bullets(pais.informacoesAdicionais) + notaCotacao(pais.informacoesAdicionais)) +
            "</div>" +
          "</div>" +
          sectionTitle("Universidades conveniadas", "mt-56") +
          '<div class="grid-2 mt-24">' + map(lista, universityCard) + "</div>" +
        "</div>"
    };
  }

  /* ---- Processo seletivo ---- */
  function bloco(b) {
    switch (b.tipo) {
      case "paragrafo": return '<p class="b-par">' + esc(b.texto) + "</p>";
      case "subtitulo": return '<h3 class="b-sub">' + esc(b.texto) + "</h3>";
      case "lista-numerada": return '<ol class="b-list num">' + map(b.itens, function (i) { return "<li>" + esc(i) + "</li>"; }) + "</ol>";
      case "lista": return '<ul class="b-list disc">' + map(b.itens, function (i) { return "<li>" + esc(i) + "</li>"; }) + "</ul>";
      case "caixa": return '<div class="b-box">' + map(b.paragrafos, function (p) { return "<p>" + esc(p) + "</p>"; }) + "</div>";
      case "nota": return '<p class="b-note">' + esc(b.texto) + "</p>";
      case "destaque": return '<p class="b-highlight">' + esc(b.texto) + "</p>";
      case "chips": return '<ul class="chips b-chips">' + map(b.itens, function (i) { return "<li>" + chip(i) + "</li>"; }) + "</ul>";
      case "tabela":
        return '<div class="table-wrap b-table"><table><thead><tr><th scope="col">' + esc(b.colunas[0]) + '</th><th scope="col">' + esc(b.colunas[1]) + "</th></tr></thead><tbody>" +
          map(b.linhas, function (l) { return '<tr><td class="key">' + esc(l[0]) + '</td><td class="val">' + esc(l[1]) + "</td></tr>"; }) + "</tbody></table></div>";
      case "cards":
        return '<div class="b-cards">' + map(b.itens, function (c) { return '<div class="b-card"><h4>' + esc(c.titulo) + "</h4><p>" + esc(c.texto) + "</p></div>"; }) + "</div>";
      default: return "";
    }
  }
  function voltarAoIndice() {
    return '<div class="step-back"><a class="btn btn-outline" href="#/processo-seletivo" data-scroll="indice-do-processo">Voltar</a></div>';
  }
  function viewProcesso() {
    var ps = processoSeletivo;
    return {
      title: "Processo seletivo | RotaPUC",
      html:
        '<div class="container py-48">' +
          '<div class="center">' + pill("Processo seletivo") + "</div>" +
          '<div class="text-center mt-16">' + updatedAt(ps.atualizadoEm) + "</div>" +
          '<div class="process-top">' +
            '<nav id="indice-do-processo" class="card process-index" aria-label="Índice do Processo"><h2>Índice do Processo</h2><ul>' +
              map(ps.indice, function (i) { return '<li><a href="#/processo-seletivo" data-scroll="' + i.id + '">' + esc(i.label) + "</a></li>"; }) +
            "</ul></nav>" +
            '<section aria-labelledby="lista-de-cr"><h2 id="lista-de-cr" class="cr-title">' + esc(ps.listaCr.titulo) + "</h2>" +
              '<div class="table-wrap compact mt-16"><table><caption class="sr-only">Nota de corte por departamento</caption>' +
              '<thead><tr><th scope="col">' + ps.listaCr.colunas[0] + '</th><th scope="col" class="right">' + ps.listaCr.colunas[1] + "</th></tr></thead><tbody>" +
              map(ps.listaCr.linhas, function (l) { return '<tr><td class="key">' + esc(l[0]) + '</td><td class="val right">' + esc(l[1]) + "</td></tr>"; }) +
              '</tbody></table></div><p class="updated mt-12">' + esc(ps.listaCr.nota) + "</p>" +
            "</section>" +
          "</div>" +
          '<section id="' + ps.preRequisitos.id + '" class="step first">' +
            sectionTitle(ps.preRequisitos.titulo) +
            '<ol class="b-list num">' + map(ps.preRequisitos.itens, function (i) { return "<li>" + esc(i) + "</li>"; }) + "</ol>" +
            '<p class="b-note">' + esc(ps.preRequisitos.nota) + "</p>" + voltarAoIndice() +
          "</section>" +
          map(ps.passos, function (p) {
            return '<section id="' + p.id + '" class="step">' + sectionTitle(p.titulo) + map(p.blocos, bloco) + voltarAoIndice() + "</section>";
          }) +
          sectionTitle("Perguntas frequentes", "mt-64") +
          '<div class="faq-list">' + map(faq, function (f) {
            return '<details class="faq"><summary>' + esc(f.pergunta) + "</summary><p>" + esc(f.resposta) + "</p></details>";
          }) + "</div>" +
        "</div>"
    };
  }

  /* ---- Fórum ---- */
  var PAGE_SIZE = 4;
  function viewForum() {
    var total = Math.max(1, Math.ceil(forum.posts.length / PAGE_SIZE));
    if (ui.forumPage > total - 1) ui.forumPage = total - 1;
    var visiveis = forum.posts.slice(ui.forumPage * PAGE_SIZE, ui.forumPage * PAGE_SIZE + PAGE_SIZE);
    return {
      title: "Fórum | RotaPUC",
      html:
        '<div class="container py-48">' +
          '<div class="center">' + pill("Fórum de perguntas") + "</div>" +
          '<h1 class="page-title text-center mt-24">Comunidade de Intercâmbio</h1>' +
          '<p class="lead centered mt-12">Troque experiências com alunos e ex-intercambistas da PUC-Rio sobre processo seletivo, destinos e vida acadêmica no exterior.</p>' +
          '<div class="forum-bar" id="forum-top"><p class="count">Todas as discussões (' + forum.posts.length + ")</p>" +
            '<a class="btn btn-primary" href="#/forum/nova">' + icon("plus", 16) + "Adicionar Pergunta</a></div>" +
          (visiveis.length === 0
            ? '<div class="mt-32">' + emptyState("Nenhuma discussão por aqui", "Seja a primeira pessoa a abrir uma pergunta na comunidade.") + "</div>"
            : '<div class="thread-list">' + map(visiveis, threadCard) + "</div>") +
          (total > 1
            ? '<div class="dots centered mt-40">' + Array.from({ length: total }).map(function (_, i) {
                return '<button type="button" class="dot" data-page="' + i + '" aria-label="Página ' + (i + 1) + '" aria-current="' + (i === ui.forumPage) + '"></button>';
              }).join("") + "</div>"
            : "") +
          '<p class="forum-foot">As perguntas e respostas publicadas ficam salvas apenas neste navegador. ' +
            '<button type="button" class="link-btn" data-action="reset">Restaurar discussões de exemplo</button></p>' +
        "</div>",
      mount: function (root) {
        root.addEventListener("click", function (e) {
          var pg = e.target.closest("[data-page]");
          if (pg) {
            ui.forumPage = Number(pg.getAttribute("data-page"));
            render({ scroll: false });
            return;
          }
          if (e.target.closest('[data-action="reset"]')) {
            if (!window.confirm("Restaurar as discussões de exemplo? As perguntas e respostas que você publicou serão removidas deste navegador.")) return;
            forum = seedForum();
            saveForum();
            ui.forumPage = 0;
            ui.drafts = {};
            render({ scroll: false });
            toast("Discussões de exemplo restauradas");
          }
        });
      }
    };
  }

  function comentarioHtml(post, c) {
    var key = post.id + ":" + c.id;
    var aberto = !!ui.openReplies[key];
    var draft = ui.drafts[key] || "";
    var respostas = repliesOf(c.id);
    return '<li class="comment">' +
      '<div class="c-head">' + avatar(c.author) + '<div><p class="c-name">' + esc(c.author) + '</p><p class="c-date">' + esc(c.createdAt) + "</p></div></div>" +
      '<p class="c-text">' + esc(c.content) + "</p>" +
      '<button type="button" class="link-btn" data-toggle-reply="' + c.id + '" aria-expanded="' + aberto + '">' + (aberto ? "Cancelar" : "Responder") + "</button>" +
      (aberto
        ? '<form class="c-form" data-reply-to="' + c.id + '"><label for="resposta-' + c.id + '" class="sr-only">Sua resposta</label>' +
          '<textarea id="resposta-' + c.id + '" class="textarea sm" rows="3" data-draft="' + key + '" placeholder="Escreva sua resposta">' + esc(draft) + "</textarea>" +
          '<button type="submit" class="btn btn-primary"' + (draft.trim() ? "" : " disabled") + ">Enviar resposta</button></form>"
        : "") +
      (respostas.length
        ? '<ul class="replies">' + map(respostas, function (r) {
            return "<li>" + '<div class="c-head">' + avatar(r.author, "sm") + '<div><p class="c-name">' + esc(r.author) + '</p><p class="c-date">' + esc(r.createdAt) + "</p></div></div>" +
              '<p class="c-text">' + esc(r.content) + "</p></li>";
          }) + "</ul>"
        : "") +
      "</li>";
  }

  function viewDiscussao(id) {
    var post = forum.posts.find(function (p) { return p.id === id; });
    if (!post) {
      return {
        title: "Discussão não encontrada | RotaPUC",
        html: '<div class="container py-64">' + emptyState("Discussão não encontrada", "Esta pergunta não existe ou foi removida.") +
          '<div class="text-center mt-24"><a class="link-btn" href="#/forum">Voltar para o fórum</a></div></div>'
      };
    }
    var topKey = post.id + ":top";
    var topDraft = ui.drafts[topKey] || "";
    var principais = commentsOf(post.id);
    var votou = forum.votedPosts.indexOf(post.id) !== -1;
    return {
      title: post.title + " | Fórum RotaPUC",
      html:
        '<div class="container py-48">' +
          '<nav class="breadcrumb" aria-label="Você está em" style="max-width:896px;margin-inline:auto">' +
            '<a href="#/forum">' + icon("arrowLeft", 14) + "Voltar para o fórum</a></nav>" +
          '<div class="center">' + pill("Fórum de perguntas") + "</div>" +
          '<article class="card post">' +
            '<div class="chips">' + map(post.tags, chip) + "</div>" +
            "<h1>" + esc(post.title) + "</h1>" +
            '<p class="body-text">' + esc(post.description) + "</p>" +
            '<div class="meta">' + avatar(post.author, "lg") +
              '<div><p class="name">' + esc(post.author) + "</p><p>" + esc(post.course) + " · " + esc(post.createdAt) + "</p></div>" +
              '<button type="button" class="upvote" data-action="upvote" aria-pressed="' + votou + '">' + icon("arrowUp", 16) + post.upvotes + " upvotes</button>" +
              '<span class="inline-count">' + icon("message", 16) + plural(totalRespostas(post.id), "resposta", "respostas") + "</span>" +
            "</div>" +
            '<form class="reply-form" data-reply-to="top">' +
              '<label for="resposta-principal" class="form-label">Responder</label>' +
              '<textarea id="resposta-principal" class="textarea" rows="4" data-draft="' + topKey + '" placeholder="Compartilhe sua experiência ou resposta">' + esc(topDraft) + "</textarea>" +
              '<button type="submit" class="btn btn-primary"' + (topDraft.trim() ? "" : " disabled") + ">Publicar resposta</button>" +
            "</form>" +
          "</article>" +
          '<section class="comments" id="respostas"><h2>Respostas e Comentários</h2>' +
            (principais.length === 0
              ? '<div class="mt-16">' + emptyState("Ainda sem respostas", "Seja a primeira pessoa a responder esta pergunta.") + "</div>"
              : '<ul class="comment-list">' + map(principais, function (c) { return comentarioHtml(post, c); }) + "</ul>") +
          "</section>" +
        "</div>",
      mount: function (root) {
        root.addEventListener("input", function (e) {
          var t = e.target.closest("textarea[data-draft]");
          if (!t) return;
          ui.drafts[t.getAttribute("data-draft")] = t.value;
          var btn = t.form && t.form.querySelector('button[type="submit"]');
          if (btn) btn.disabled = !t.value.trim();
        });
        root.addEventListener("click", function (e) {
          if (e.target.closest('[data-action="upvote"]')) {
            togglePostUpvote(post.id);
            render({ scroll: false });
            var up = document.querySelector('[data-action="upvote"]');
            if (up) up.focus();
            return;
          }
          var tg = e.target.closest("[data-toggle-reply]");
          if (tg) {
            var cid = tg.getAttribute("data-toggle-reply");
            var key = post.id + ":" + cid;
            ui.openReplies[key] = !ui.openReplies[key];
            render({ scroll: false });
            var ta = document.getElementById("resposta-" + cid);
            if (ta) ta.focus();
            else {
              var again = document.querySelector('[data-toggle-reply="' + cid + '"]');
              if (again) again.focus();
            }
          }
        });
        root.addEventListener("submit", function (e) {
          e.preventDefault();
          var form = e.target;
          var alvo = form.getAttribute("data-reply-to");
          var ta = form.querySelector("textarea");
          var texto = ta.value.trim();
          if (!texto) return;
          if (alvo === "top") {
            addComment(post.id, texto, null);
            ui.drafts[topKey] = "";
            render({ scroll: false });
            toast("Resposta publicada");
            scrollToId("respostas");
          } else {
            var key = post.id + ":" + alvo;
            addComment(post.id, texto, alvo);
            ui.drafts[key] = "";
            ui.openReplies[key] = false;
            render({ scroll: false });
            toast("Resposta enviada");
          }
        });
      }
    };
  }

  var marcadores = ["Alemanha", "Europa", "Matrícula", "Visto"];
  function viewNovaPergunta() {
    var n = ui.nova;
    return {
      title: "Nova pergunta | Fórum RotaPUC",
      html:
        '<div class="container py-48">' +
          '<div class="center">' + pill("Fórum de perguntas") + "</div>" +
          '<h1 class="page-title text-center mt-24">Nova Pergunta</h1>' +
          '<p class="lead centered mt-12">Formule sua dúvida de maneira clara para obter melhores respostas da comunidade.</p>' +
          '<form class="card new-form" id="nova-form" novalidate>' +
            '<div class="group"><label for="titulo" class="form-label">Título da Pergunta *</label>' +
              '<input id="titulo" class="input" value="' + esc(n.titulo) + '" placeholder="Ex.: Como funciona a matrícula na universidade de destino?" maxlength="160"' +
              (n.erros.titulo ? ' aria-invalid="true" aria-describedby="erro-titulo"' : "") + ">" +
              (n.erros.titulo ? '<p id="erro-titulo" class="field-error">' + esc(n.erros.titulo) + "</p>" : "") +
            "</div>" +
            '<div class="group"><label for="descricao" class="form-label">Descrição detalhada *</label>' +
              '<textarea id="descricao" class="textarea" rows="6" placeholder="Explique o contexto da sua dúvida."' +
              (n.erros.descricao ? ' aria-invalid="true" aria-describedby="erro-descricao"' : "") + ">" + esc(n.descricao) + "</textarea>" +
              (n.erros.descricao ? '<p id="erro-descricao" class="field-error">' + esc(n.erros.descricao) + "</p>" : "") +
            "</div>" +
            "<fieldset><legend>Marcadores sugeridos</legend><div class=\"tag-toggles\">" +
              map(marcadores, function (m) {
                var ativo = n.tags.indexOf(m) !== -1;
                return '<button type="button" class="tag-toggle" data-tag="' + esc(m) + '" aria-pressed="' + ativo + '">+' + esc(m) + "</button>";
              }) +
            "</div></fieldset>" +
            '<div class="actions"><button type="submit" class="btn btn-primary btn-lg">Postar</button>' +
            '<a class="link-btn" href="#/forum">Cancelar</a></div>' +
          "</form>" +
        "</div>",
      mount: function (root) {
        var form = root.querySelector("#nova-form");
        form.addEventListener("input", function (e) {
          if (e.target.id === "titulo") ui.nova.titulo = e.target.value;
          if (e.target.id === "descricao") ui.nova.descricao = e.target.value;
        });
        form.addEventListener("click", function (e) {
          var b = e.target.closest("[data-tag]");
          if (!b) return;
          var t = b.getAttribute("data-tag");
          var i = ui.nova.tags.indexOf(t);
          if (i === -1) ui.nova.tags.push(t); else ui.nova.tags.splice(i, 1);
          b.setAttribute("aria-pressed", String(i === -1));
        });
        form.addEventListener("submit", function (e) {
          e.preventDefault();
          var erros = {};
          if (!ui.nova.titulo.trim()) erros.titulo = "Informe o título da pergunta.";
          if (!ui.nova.descricao.trim()) erros.descricao = "Descreva sua dúvida com mais detalhes.";
          ui.nova.erros = erros;
          if (Object.keys(erros).length) {
            render({ scroll: false });
            var first = document.getElementById(erros.titulo ? "titulo" : "descricao");
            if (first) first.focus();
            return;
          }
          var id = addPost({ title: ui.nova.titulo.trim(), description: ui.nova.descricao.trim(), tags: ui.nova.tags.slice() });
          ui.nova = { titulo: "", descricao: "", tags: [], erros: {} };
          ui.forumPage = 0;
          location.hash = "#/forum/" + id;
          toast("Pergunta publicada");
        });
      }
    };
  }

  /* ---- Contatos / Quem somos ---- */
  function viewContatos() {
    return {
      title: "Contatos | RotaPUC",
      html:
        '<div class="container py-48">' +
          pill("Contatos") +
          '<h1 class="page-title mt-16">Contato com a coordenação</h1>' +
          '<p class="lead mt-12">Fale com a coordenação de cooperação internacional da PUC-Rio para dúvidas sobre convênios, prazos e documentação.</p>' +
          '<div class="grid-3 mt-40">' + map(blocosContato, function (b) {
            return infoCard(b.titulo, map(b.linhas, function (l) { return "<p>" + esc(l) + "</p>"; }));
          }) + "</div>" +
        "</div>"
    };
  }
  function viewQuemSomos() {
    return {
      title: "Quem somos | RotaPUC",
      html:
        '<div class="container py-64">' +
          pill("Quem somos") +
          '<h1 class="page-title mt-16">Conteúdo institucional pendente</h1>' +
          '<p class="lead mt-16">Esta página faz parte da navegação do RotaPUC, mas o conteúdo institucional ainda não foi definido. O texto será fornecido pela coordenação e publicado aqui, mantendo o mesmo padrão visual das demais páginas.</p>' +
        "</div>"
    };
  }

  function viewNotFound(titulo, texto, href, cta) {
    return {
      title: "Página não encontrada | RotaPUC",
      html:
        '<div class="container not-found"><p class="code">404</p>' +
          "<h1>" + esc(titulo || "Página não encontrada") + "</h1>" +
          "<p>" + esc(texto || "A página que você procura não existe ou foi movida.") + "</p>" +
          '<a class="btn btn-primary" href="' + (href || "#/") + '">' + esc(cta || "Voltar ao início") + "</a></div>"
    };
  }

  /* ================================================================
     ROTEADOR (hash) + NAVEGAÇÃO
     ================================================================ */
  var navItems = [
    { label: "Início", to: "/" },
    { label: "Universidades", to: "/universidades" },
    { label: "Países", to: "/paises" },
    { label: "Processo seletivo", to: "/processo-seletivo" },
    { label: "Fórum", to: "/forum" },
    { label: "Contatos", to: "/contatos" },
    { label: "Quem somos", to: "/quem-somos" }
  ];

  function currentPath() {
    var h = location.hash.replace(/^#/, "");
    if (h.charAt(0) !== "/") h = "/";
    var p = h.split("?")[0].replace(/\/+$/, "");
    return p || "/";
  }

  function resolve(path) {
    var seg = path.split("/").filter(Boolean).map(function (s) {
      try { return decodeURIComponent(s); } catch (e) { return s; }
    });
    if (seg.length === 0) return viewHome();
    switch (seg[0]) {
      case "universidades":
        if (seg.length === 1) return viewUniversidades();
        if (seg.length === 2) return viewUniversidade(seg[1]);
        break;
      case "paises":
        if (seg.length === 1) return viewPaises();
        if (seg.length === 2) return viewPais(seg[1]);
        break;
      case "processo-seletivo":
        if (seg.length === 1) return viewProcesso();
        break;
      case "forum":
        if (seg.length === 1) return viewForum();
        if (seg.length === 2 && seg[1] === "nova") return viewNovaPergunta();
        if (seg.length === 2) return viewDiscussao(seg[1]);
        break;
      case "contatos":
        if (seg.length === 1) return viewContatos();
        break;
      case "quem-somos":
        if (seg.length === 1) return viewQuemSomos();
        break;
    }
    return viewNotFound();
  }

  var navList = document.getElementById("nav-list");
  function renderNav(path) {
    var first = "/" + (path.split("/")[1] || "");
    navList.innerHTML = map(navItems, function (i) {
      var active = i.to === "/" ? path === "/" : first === i.to;
      return '<li><a href="#' + i.to + '"' + (active ? ' aria-current="page"' : "") + ">" + i.label + "</a></li>";
    });
  }

  var main = document.getElementById("main");
  var lastPath = null;
  function render(opts) {
    var path = currentPath();
    var view = resolve(path);
    var changed = path !== lastPath;
    lastPath = path;
    var y = window.scrollY;

    document.title = view.title;
    renderNav(path);

    var page = document.createElement("div");
    if (changed) page.className = "page";
    page.innerHTML = view.html;
    main.replaceChildren(page);
    if (view.mount) view.mount(page);

    if (opts && opts.scroll === false) window.scrollTo(0, y);
    else if (changed) {
      window.scrollTo(0, 0);
      main.focus({ preventScroll: true });
    }
  }

  function renderFooter() {
    var redes = [
      { label: "Instagram da CCCI PUC-Rio", href: "https://www.instagram.com/ccci_pucrio_intercambio/", icon: "instagram" },
      { label: "Facebook da CCCI PUC-Rio", href: "https://www.facebook.com/pucriointercambio#", icon: "facebook" },
      { label: "YouTube da PUC-Rio", href: "https://www.youtube.com/pucriooficial", icon: "youtube" },
      { label: "Site oficial da CCCI PUC-Rio", href: "https://www.puc-rio.br/ensinopesq/ccci/", icon: "globe" }
    ];
    document.getElementById("footer").innerHTML =
      '<div class="container">' +
        '<div class="center">' + pill("Contato com a coordenação") + "</div>" +
        "<dl>" + map(blocosContato, function (b) {
          return "<div><dt>" + esc(b.titulo) + "</dt><dd>" + map(b.linhas, function (l) { return "<p>" + esc(l) + "</p>"; }) + "</dd></div>";
        }) + "</dl>" +
        '<ul class="socials">' + map(redes, function (r) {
          return '<li><a href="' + r.href + '" target="_blank" rel="noopener noreferrer" aria-label="' + esc(r.label) + '" title="' + esc(r.label) + '">' + icon(r.icon, 20) + "</a></li>";
        }) + "</ul>" +
        '<p class="disclaimer">Protótipo acadêmico RotaPUC — conteúdo demonstrativo, não oficial.</p>' +
      "</div>";
  }

  /* Rolagem interna (índice do processo seletivo) sem trocar de rota */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-scroll]");
    if (!a) return;
    e.preventDefault();
    scrollToId(a.getAttribute("data-scroll"));
  });

  window.addEventListener("hashchange", function () { render(); });
  renderFooter();
  render();
})();
</script>
