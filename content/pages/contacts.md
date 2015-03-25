Title: Contatti
Template: full_page

<div class="row">
	<!-- CONTACT FORM -->
	<div class="twelve columns">
		<div class="wrapcontact">
			<h5>SEND US A MESSAGE</h5>
			<div class="done">
				<div class="alert-box success">
				 Messaggio correttamente inviato! <a href="" class="close">x</a>
				</div>
			</div>
				<form method="post" action="{{ SITEURL }}/bin/contact.php" id="contactform">
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
					<input type="submit" id="submit" class="readmore" value="Submit">
				</div>
				</form>
		</div>
	</div>
</div>