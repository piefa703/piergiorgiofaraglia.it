Title: Contatti
Date: 2015-04-02
Lang: it
Template: page-no-sidebar
navbar-order: 04

<div class="row">
  <div class="twelve columns">
    <div class="wrapcontact">
      <h5>Scrivi un messaggio o una richiesta di preventivo. A breve sarai
      ricontattato.</h5>
      <div class="done">
        <div class="alert-box success">
          Messaggio correttamente inviato! <a href="" class="close">x</a>
        </div>
      </div>
      <form method="post" action="http://api.piergiorgiofaraglia.it/sendmail">
        <div class="form">
          <div class="six columns noleftmargin">
            <label>Nome</label>
            <input type="text" name="name" class="smoothborder" placeholder="Nome *"/>
          </div>
          <div class="six columns">
            <label>E-mail</label>
            <input type="text" name="email" class="smoothborder" placeholder="Email *"/>
          </div>
          <label>Messaggio</label>
          <textarea name="comment" class="smoothborder ctextarea" rows="14" placeholder="Inserisci qui il tuo messaggio *"></textarea>
          <input type="submit" id="submit" class="readmore" value="Invia">
        </div>
      </form>
    </div>
  </div>
</div>
