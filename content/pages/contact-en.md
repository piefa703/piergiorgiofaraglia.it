Title: Contacts
Date: 2015-04-02
Lang: en
Template: page-no-sidebar
navbar-order: 04

<div class="row">
  <div class="twelve columns">
    <div class="wrapcontact">
      <h5>SEND ME A MESSAGE</h5>
      <div class="done">
        <div class="alert-box success">
          Message successfully sent! <a href="" class="close">x</a>
        </div>
      </div>
      <form method="post" action="http://api.piergiorgiofaraglia.it/sendmail">
        <div class="form">
          <div class="six columns noleftmargin">
            <label>Name</label>
            <input type="text" name="name" class="smoothborder" placeholder="Your name *"/>
          </div>
          <div class="six columns">
            <label>E-mail address</label>
            <input type="text" name="email" class="smoothborder" placeholder="Your e-mail address *"/>
          </div>
          <label>Messaggio</label>
          <textarea name="message" class="smoothborder ctextarea" rows="14" placeholder="Message, feedback, comments *"></textarea>
          <input type="submit" id="submit" class="readmore" value="Send">
        </div>
      </form>
    </div>
  </div>
</div>
