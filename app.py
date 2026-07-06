from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Paula Cunha Advocacia — Direito Penal, Civil, Trabalhista e do Consumidor</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --ink: #16233A;
    --green: #1F3D2B;
    --brass: #A6812C;
    --paper: #EFEAE4;
    --paper-light: #FAF8F3;
    --charcoal: #26241F;
    --line: rgba(22,35,58,0.16);
  }

  *{ box-sizing: border-box; }

  html{ scroll-behavior: smooth; }

  body{
    margin:0;
    background: var(--paper);
    color: var(--charcoal);
    font-family: 'IBM Plex Sans', sans-serif;
    line-height: 1.6;
  }

  h1, h2, h3, .display{
    font-family: 'Fraunces', serif;
    font-weight: 600;
    color: var(--ink);
    margin: 0;
  }

  .mono{
    font-family: 'IBM Plex Mono', monospace;
  }

  a{ color: inherit; }

  /* ---------- Folder-tab nav ---------- */
  .filebar{
    position: sticky;
    top: 0;
    z-index: 50;
    background: var(--ink);
    color: var(--paper-light);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 28px;
    height: 64px;
  }
  .filebar .brand{
    font-family: 'Fraunces', serif;
    font-size: 1.15rem;
    letter-spacing: 0.02em;
  }
  .filebar nav{
    display: flex;
    gap: 8px;
  }
  .tab{
    background: transparent;
    border: 1px solid transparent;
    color: var(--paper-light);
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.85rem;
    padding: 8px 16px;
    border-radius: 6px 6px 0 0;
    cursor: pointer;
    transition: background 0.2s ease, border-color 0.2s ease;
  }
  .tab:hover{
    background: rgba(250,248,243,0.08);
    border-color: rgba(250,248,243,0.25);
  }

  /* ---------- Dossier header (hero) ---------- */
  .dossier{
    max-width: 980px;
    margin: 40px auto 0;
    background: var(--paper-light);
    border: 1px solid var(--line);
    box-shadow: 0 1px 0 var(--line);
  }
  .dossier-meta{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 32px;
    border-bottom: 1px solid var(--line);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--green);
  }
  .hero{
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 32px;
    padding: 56px 48px 64px;
  }
  .hero h1{
    font-size: clamp(2.1rem, 4vw, 3rem);
    line-height: 1.08;
  }
  .hero .kicker{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--brass);
    margin-bottom: 14px;
    display: block;
  }
  .hero p.lead{
    margin-top: 18px;
    max-width: 46ch;
    color: #4a463d;
  }
  .cta-row{
    margin-top: 30px;
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .btn{
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    padding: 12px 22px;
    border-radius: 3px;
    border: 1px solid transparent;
    cursor: pointer;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .btn:hover{ transform: translateY(-1px); }
  .btn:focus-visible{ outline: 3px solid var(--brass); outline-offset: 2px; }
  .btn-primary{ background: var(--green); color: var(--paper-light); }
  .btn-primary:hover{ box-shadow: 0 4px 14px rgba(31,61,43,0.35); }
  .btn-ghost{ background: transparent; color: var(--ink); border-color: var(--ink); }
  .btn-ghost:hover{ background: var(--ink); color: var(--paper-light); }
  .btn-brass{ background: var(--brass); color: var(--paper-light); }
  .btn-brass:hover{ box-shadow: 0 4px 14px rgba(166,129,44,0.4); }

  .seal{
    justify-self: end;
    align-self: start;
    width: 132px;
    height: 132px;
    border-radius: 50%;
    border: 2.5px solid var(--brass);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: 'Fraunces', serif;
    font-size: 0.72rem;
    color: var(--brass);
    letter-spacing: 0.05em;
    padding: 12px;
    position: relative;
  }
  .seal::before{
    content: "";
    position: absolute;
    inset: 10px;
    border: 1px solid var(--brass);
    border-radius: 50%;
  }

  /* ---------- Numbered "Art." sections ---------- */
  section.article{
    max-width: 980px;
    margin: 0 auto;
    padding: 56px 48px;
    border-top: 1px solid var(--line);
    opacity: 0;
    transform: translateY(14px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  section.article.visible{
    opacity: 1;
    transform: translateY(0);
  }
  .art-label{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: var(--brass);
    letter-spacing: 0.08em;
    margin-bottom: 10px;
    display: block;
  }
  section.article h2{
    font-size: 1.7rem;
    margin-bottom: 22px;
  }

  /* qualifications */
  .quals{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
  }
  .qual-card{
    background: var(--paper-light);
    border: 1px solid var(--line);
    border-left: 3px solid var(--green);
    padding: 18px 20px;
  }
  .qual-card .tag{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    color: var(--green);
    letter-spacing: 0.05em;
  }
  .qual-card h3{
    font-size: 1.05rem;
    margin: 6px 0 4px;
  }
  .qual-card p{ margin: 0; color: #55503f; font-size: 0.92rem; }

  /* areas */
  .areas{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
  }
  .area-chip{
    background: var(--paper-light);
    border: 1px solid var(--line);
    padding: 16px;
    text-align: center;
    font-size: 0.92rem;
    transition: border-color 0.2s ease;
  }
  .area-chip:hover{ border-color: var(--brass); }

  /* ---------- Simulator ---------- */
  .sim-box{
    background: var(--paper-light);
    border: 1px solid var(--line);
    padding: 32px;
    position: relative;
    overflow: hidden;
  }
  .sim-grid{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 22px;
  }
  label.field-label{
    display: block;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--green);
    margin-bottom: 6px;
    font-family: 'IBM Plex Mono', monospace;
  }
  select{
    width: 100%;
    padding: 11px 12px;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.95rem;
    border: 1px solid var(--line);
    background: #fff;
    color: var(--charcoal);
    border-radius: 3px;
  }
  select:focus-visible{ outline: 3px solid var(--brass); outline-offset: 1px; }

  .sim-result{
    border-top: 1px dashed var(--line);
    padding-top: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
  }
  .sim-value{
    font-family: 'Fraunces', serif;
    font-size: 2.1rem;
    color: var(--ink);
  }
  .sim-value .cents{ font-size: 1.1rem; }
  .sim-note{
    max-width: 40ch;
    font-size: 0.85rem;
    color: #6b6656;
  }
  .stamp{
    font-family: 'Fraunces', serif;
    font-weight: 700;
    color: var(--brass);
    border: 2.5px solid var(--brass);
    border-radius: 50%;
    width: 92px;
    height: 92px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 0.68rem;
    letter-spacing: 0.04em;
    transform: rotate(-14deg) scale(0);
    transition: transform 0.35s cubic-bezier(.34,1.56,.64,1);
  }
  .stamp.stamped{ transform: rotate(-14deg) scale(1); }

  /* ---------- Contact ---------- */
  .contact-grid{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
  .contact-item{
    padding: 16px 0;
    border-bottom: 1px solid var(--line);
  }
  .contact-item .tag{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    text-transform: uppercase;
    color: var(--brass);
    letter-spacing: 0.06em;
  }
  .contact-item p{ margin: 4px 0 0; }

  footer{
    text-align: center;
    padding: 30px;
    font-size: 0.78rem;
    color: #7a755f;
    font-family: 'IBM Plex Mono', monospace;
  }

  @media (max-width: 760px){
    .hero{ grid-template-columns: 1fr; padding: 40px 24px; }
    .seal{ justify-self: start; }
    section.article{ padding: 40px 24px; }
    .quals, .areas, .sim-grid, .contact-grid{ grid-template-columns: 1fr; }
    .filebar{ padding: 0 16px; }
    .filebar nav{ gap: 2px; }
    .tab{ padding: 8px 10px; font-size: 0.78rem; }
  }

  @media (prefers-reduced-motion: reduce){
    *{ transition: none !important; }
    section.article{ opacity: 1; transform: none; }
  }
</style>
</head>
<body>

  <div class="filebar">
    <div class="brand">Paula Cunha Advocacia</div>
    <nav>
      <button class="tab" onclick="document.getElementById('sobre').scrollIntoView()">Sobre</button>
      <button class="tab" onclick="document.getElementById('atuacao').scrollIntoView()">Atuação</button>
      <button class="tab" onclick="document.getElementById('simulador').scrollIntoView()">Simulador</button>
      <button class="tab" onclick="document.getElementById('contato').scrollIntoView()">Contato</button>
    </nav>
  </div>

  <div class="dossier">
    <div class="dossier-meta">
      <span>Processo Nº 2026.AM.0417 — Advocacia Autônoma</span>
      <span>Manaus / AM</span>
    </div>

    <div class="hero">
      <div>
        <span class="kicker">Penal &middot; Civil &middot; Trabalhista &middot; Consumidor</span>
        <h1>Dra. Paula Talita Maia da Cunha</h1>
        <p class="lead">
          Advocacia autônoma com atuação em Direito Penal e Processo Penal,
          Direito Civil e Processo Civil, Direito do Trabalho e Direito do
          Consumidor — da consultoria inicial ao acompanhamento completo do
          seu processo.
        </p>
        <div class="cta-row">
          <button class="btn btn-primary" onclick="document.getElementById('sobre').scrollIntoView()">Saiba mais</button>
          <button class="btn btn-brass" onclick="document.getElementById('simulador').scrollIntoView()">Simular meu caso</button>
          <button class="btn btn-ghost" onclick="document.getElementById('contato').scrollIntoView()">Fale conosco</button>
        </div>
      </div>
      <div class="seal">OAB/AM<br>21.396</div>
    </div>
  </div>

  <section class="article" id="sobre">
    <span class="art-label">Art. 1º — Formação e Qualificações</span>
    <h2>Uma trajetória construída em Direito Penal e Civil</h2>
    <div class="quals">
      <div class="qual-card">
        <span class="tag">Graduação</span>
        <h3>Bacharelado em Direito</h3>
        <p>Centro Universitário Fametro — Manaus, AM</p>
      </div>
      <div class="qual-card">
        <span class="tag">Especialização</span>
        <h3>Direito Penal e Processo Penal</h3>
        <p>Pós-graduação lato sensu</p>
      </div>
      <div class="qual-card">
        <span class="tag">Especialização</span>
        <h3>Direito Civil e Processo Civil</h3>
        <p>Pós-graduação lato sensu</p>
      </div>
      <div class="qual-card">
        <span class="tag">Cursos complementares</span>
        <h3>Formação continuada</h3>
        <p>LGPD (Fundação Bradesco), Gerenciamento de Conflitos e Liderança e Gestão de Equipes (Sebrae), Informática Avançada e Excel (RF Treinamentos), Word (Fundação Bradesco)</p>
      </div>
    </div>
  </section>

  <section class="article" id="atuacao">
    <span class="art-label">Art. 2º — Áreas de Atuação</span>
    <h2>Onde podemos ajudar</h2>
    <div class="areas">
      <div class="area-chip">Direito Penal e Processo Penal</div>
      <div class="area-chip">Direito Civil e Processo Civil</div>
      <div class="area-chip">Direito do Trabalho e Processo do Trabalho</div>
      <div class="area-chip">Direito do Consumidor</div>
    </div>
  </section>

  <section class="article" id="simulador">
    <span class="art-label">Art. 3º — Estimativa de Honorários</span>
    <h2>Simule o valor do seu caso</h2>
    <div class="sim-box">
      <div class="sim-grid">
        <div>
          <label class="field-label" for="tipo">Tipo de serviço</label>
          <select id="tipo">
            <option value="consulta" data-base="200">Consulta jurídica avulsa</option>
            <option value="peca" data-base="700">Elaboração de peça processual</option>
            <option value="acao_civel" data-base="2200">Ação cível ou trabalhista</option>
            <option value="acao_penal" data-base="3000">Defesa criminal</option>
            <option value="consumidor" data-base="600">Demanda no Juizado Especial (consumidor)</option>
          </select>
        </div>
        <div>
          <label class="field-label" for="complexidade">Complexidade do caso</label>
          <select id="complexidade">
            <option value="1" data-mult="1">Baixa</option>
            <option value="2" data-mult="1.6">Média</option>
            <option value="3" data-mult="2.4">Alta</option>
          </select>
        </div>
      </div>

      <button class="btn btn-primary" onclick="simular()">Calcular estimativa</button>

      <div class="sim-result" style="margin-top:24px;">
        <div>
          <div class="sim-value mono" id="valorEstimado">R$ 0<span class="cents">,00</span></div>
          <p class="sim-note">Valor estimado com base no tipo de serviço e complexidade informados.
          A proposta final é sempre definida em consulta inicial gratuita.</p>
        </div>
        <div class="stamp" id="stamp">ESTIMATIVA<br>PRELIMINAR</div>
      </div>
    </div>
  </section>

  <section class="article" id="contato">
    <span class="art-label">Art. 4º — Contato</span>
    <h2>Vamos conversar sobre o seu caso</h2>
    <div class="contact-grid">
      <div class="contact-item">
        <span class="tag">Telefone / WhatsApp</span>
        <p>(92) 98401-9098</p>
      </div>
      <div class="contact-item">
        <span class="tag">E-mail</span>
        <p>Adv.PaulaCunha@outlook.com</p>
      </div>
      <div class="contact-item">
        <span class="tag">Localização</span>
        <p>Manaus, AM</p>
      </div>
      <div class="contact-item">
        <span class="tag">LinkedIn</span>
        <p><a href="https://linkedin.com/in/paula-cunha-323703336" target="_blank" rel="noopener">linkedin.com/in/paula-cunha-323703336</a></p>
      </div>
    </div>
    <div class="cta-row" style="margin-top:20px;">
      <a class="btn btn-brass" href="https://wa.me/5592984019098" target="_blank" rel="noopener">Chamar no WhatsApp</a>
      <a class="btn btn-ghost" href="mailto:Adv.PaulaCunha@outlook.com">Enviar e-mail</a>
    </div>
  </section>

  <footer>© 2026 Paula Cunha Advocacia — OAB/AM 21.396. Todos os direitos reservados.</footer>

  <script>
    function simular(){
      const tipoEl = document.getElementById('tipo');
      const compEl = document.getElementById('complexidade');
      const base = parseFloat(tipoEl.selectedOptions[0].dataset.base);
      const mult = parseFloat(compEl.selectedOptions[0].dataset.mult);
      const total = base * mult;

      const [reais, centavos] = total.toFixed(2).split('.');
      document.getElementById('valorEstimado').innerHTML =
        'R$ ' + Number(reais).toLocaleString('pt-BR') + '<span class="cents">,' + centavos + '</span>';

      const stamp = document.getElementById('stamp');
      stamp.classList.remove('stamped');
      void stamp.offsetWidth; // restart animation
      stamp.classList.add('stamped');
    }

    // reveal sections on scroll
    const sections = document.querySelectorAll('section.article');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting){
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.15 });
    sections.forEach(s => observer.observe(s));
  </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(debug=True)
