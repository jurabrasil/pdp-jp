<<<<<<< HEAD
$(function (classificados) {

	
	document.querySelectorAll('.jp')
	$('.jg').change((e) => {
		xuxu = e.target
		el_timea = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.timea')
		id_timea = $(el_timea).attr('id')
		el_timeb = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.timeb')
		id_timeb = $(el_timeb).attr('id')
		el_placara = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.placara')
		el_placarb = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.placarb')
		
		if (el_placara.val() != "" && el_placarb.val() != "") {
			timea = (el_timea.text().trim()).split(' ', 1)
			timeb = (el_timeb.text().trim()).split(' ', 1)
			placara_form = !isNaN(el_placara.val().trim()) ? el_placara.val().trim() : "erro"
			placarb_form = !isNaN(el_placarb.val().trim()) ? el_placarb.val().trim() : "erro"
			
			class_timea = $('#' + id_timea)
			class_timeb = $('#' + id_timeb)
			placara = parseInt(placara_form)
			placarb = parseInt(placarb_form)
			el_placara.val(parseInt(el_placara.val()))
			el_placara.val(parseInt(el_placara.val()))
			
			if ((placara > -1 && placara < 30) && (placarb > -1 && placarb < 30)) {
				int_placara = parseInt(placara)
				el_placara.val(parseInt(el_placara.val()))
				el_placara.attr('disabled', 'disabled')
				el_placarb.attr('disabled', 'disabled')
				el_placara.val(placara)
				el_placarb.val(placarb)
				pontos(class_timea, class_timeb, placara, placarb)
				
			}
			else if (isNaN(placara) || isNaN(placarb)) {
				if (isNaN(placara)) {
					el_placara.val("")
					el_placara.focus()
				}
				else {
					el_placarb.val("")
					el_placarb.focus()
				}
			}
			else {
				el_placara.val("")
				el_placarb.val("")
				el_placara.focus()
			}
		}
		setTimeout(()=>{

			classificados = $('.primeiros8').find('a')
			console.log(classificados)
			fase2(classificados)
		},1000)
	})
		
	})

	
	function pontos(class_timea, class_timeb, placara, placarb) {
		// times na classificação
		pg_timea = $(class_timea[0]).find('.pontos')
		pg_timeb = $(class_timeb[0]).find('.pontos')
		
		j_timea = $(class_timea[0]).find('.jogo')
		j_timeb = $(class_timeb[0]).find('.jogo')
		
		e_timea = $(class_timea[0]).find('.empate')
		e_timeb = $(class_timeb[0]).find('.empate')
		
		d_timea = $(class_timea[0]).find('.derrota')
		d_timeb = $(class_timeb[0]).find('.derrota')
		
		gp_timea = $(class_timea[0]).find('.golspro')
		gp_timeb = $(class_timeb[0]).find('.golspro')
		
		gc_timea = $(class_timea[0]).find('.golscontra')
		gc_timeb = $(class_timeb[0]).find('.golscontra')
		
		sg_timea = $(class_timea[0]).find('.saldo')
		sg_timeb = $(class_timeb[0]).find('.saldo')
		
		v_timea = $(class_timea[0]).find('.vitoria')
		v_timeb = $(class_timeb[0]).find('.vitoria')
		
		$(j_timea).text(parseInt(j_timea[0].innerText) + 1)
		$(j_timeb).text(parseInt(j_timeb[0].innerText) + 1)
		
		$(gp_timea).text(parseInt(gp_timea[0].innerText) + placara)
		$(gp_timeb).text(parseInt(gp_timeb[0].innerText) + placarb)

		$(gc_timea).text(parseInt(gc_timea[0].innerText) + placarb)
		$(gc_timeb).text(parseInt(gc_timeb[0].innerText) + placara)
		
		if (placara > placarb) {
			$(pg_timea).text(parseInt(pg_timea[0].innerText) + 3)
			$(v_timea).text(parseInt(v_timea[0].innerText) + 1)
			$(d_timeb).text(parseInt(d_timeb[0].innerText) + 1)
			$(sg_timea).text(parseInt(sg_timea[0].innerText) + (placara - placarb))
			$(sg_timeb).text(parseInt(sg_timeb[0].innerText) - (placara - placarb))

		} else if (placara == placarb) {
			$(pg_timea).text(parseInt(pg_timea[0].innerText) + 1)
			$(pg_timeb).text(parseInt(pg_timeb[0].innerText) + 1)
			$(e_timea).text(parseInt(e_timea[0].innerText) + 1)
			$(e_timeb).text(parseInt(e_timeb[0].innerText) + 1)

		} else if (placarb > placara) {
			$(pg_timeb).text(parseInt(pg_timeb[0].innerText) + 3)
			$(v_timeb).text(parseInt(v_timeb[0].innerText) + 1)
			$(d_timea).text(parseInt(d_timea[0].innerText) + 1)
			$(sg_timeb).text(parseInt(sg_timeb[0].innerText) + (placarb - placara))
			$(sg_timea).text(parseInt(sg_timea[0].innerText) - (placarb - placara))
		}
		
	ordenar()
	
}

function ordenar() {
	var valores = $('.ord').find('tr').get();

	valores.sort(function (a, b) {
		valor1 = (parseInt($(a).children('td').eq(1).text().toUpperCase() + 10000)) + (parseInt($(a).children('td').eq(3).text().toUpperCase() + 1000)) + (parseInt($(a).children('td').eq(8).text().toUpperCase() + 500)) + (parseInt($(a).children('td').eq(6).text().toUpperCase()))
		valor2 = (parseInt($(b).children('td').eq(1).text().toUpperCase() + 10000)) + (parseInt($(b).children('td').eq(3).text().toUpperCase() + 1000)) + (parseInt($(b).children('td').eq(8).text().toUpperCase() + 500)) + (parseInt($(b).children('td').eq(6).text().toUpperCase()))
		return valor1 < valor2 ? 1 : valor1 > valor2 ? -1 : 0;
	});
	$.each(valores, (indice, elemento) => {
		$('.ord').append(elemento)
	})
	numera()
}

function numera() {
	var valores = $('.ord').find('tr').get()

	valores.forEach(function (v, i) {
		$(v).children('th').text(i + 1)
		if (i < 8) {
=======
$(function(){
    $('.jg').change((e)=>{
        xuxu = e.target
		// capturar o campo
		el_timea = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.timea')
		id_timea = $(el_timea).attr('id')

		el_timeb = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.timeb')
		id_timeb = $(el_timeb).attr('id')

		
		el_placara = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.placara')
		el_placarb = $(xuxu.parentNode.parentNode.parentNode.parentNode.children[0]).find('.placarb')

        timea = (el_timea.text().trim()).split(' ', 1)
		timeb = (el_timeb.text().trim()).split(' ', 1)

        placara_form = !isNaN(el_placara.val().trim()) ? el_placara.val().trim() : "erro"
        placarb_form = !isNaN(el_placarb.val().trim()) ? el_placarb.val().trim() : "erro"
		
		class_timea = $('#'+id_timea)
		class_timeb = $('#'+id_timeb)
		
		placara = parseInt(placara_form)
		placarb = parseInt(placarb_form)
		el_placara.val(parseInt(el_placara.val()))
		el_placara.val(parseInt(el_placara.val()))
		
		if ((placara > -1 && placara < 30) && (placarb > -1 && placarb < 30)){
			
			int_placara = parseInt(placara)
			el_placara.val(parseInt(el_placara.val()))
			el_placara.attr('disabled', 'disabled')
			el_placarb.attr('disabled', 'disabled')
			el_placara.val(placara)
			el_placarb.val(placarb)
			pontos(class_timea, class_timeb, placara, placarb )
		}
		else if (isNaN(placara) || isNaN(placarb)){
			if (isNaN(placara)){
				el_placara.val("")
				el_placara.focus()
			} 
			else {
				el_placarb.val("")
				el_placarb.focus()
			}
				
			
		}

		else{
			el_placara.val("")
			el_placarb.val("")
			el_placara.focus()
		}
    })
})

function pontos(class_timea, class_timeb, placara, placarb){
	// timea 
	pg_timea = class_timea[0].childNodes[4]
	j_timea = class_timea[0].childNodes[6]
	v_timea = class_timea[0].childNodes[8]
	e_timea = class_timea[0].childNodes[10]
	d_timea = class_timea[0].childNodes[12]
	gp_timea = class_timea[0].childNodes[14]
	gc_timea = class_timea[0].childNodes[16]
	sg_timea = class_timea[0].childNodes[18]
	// timeb 
	pg_timeb = class_timeb[0].childNodes[4]
	j_timeb = class_timeb[0].childNodes[6]
	v_timeb = class_timeb[0].childNodes[8]
	e_timeb = class_timeb[0].childNodes[10]
	d_timeb = class_timeb[0].childNodes[12]
	gp_timeb = class_timeb[0].childNodes[14]
	gc_timeb = class_timeb[0].childNodes[16]
	sg_timeb = class_timeb[0].childNodes[18]
	
	placara - placarb
	
	j_timea.innerText = parseInt(j_timea.innerText) + 1
	j_timeb.innerText = parseInt(j_timeb.innerText) + 1
	
	gp_timea.innerText = parseInt(gp_timea.innerText) + placara
	gc_timeb.innerText = parseInt(gc_timeb.innerText) + placara
	gc_timea.innerText = parseInt(gc_timea.innerText) + placarb
	gp_timeb.innerText = parseInt(gp_timeb.innerText) + placarb
	
	if (placara > placarb) {
		pg_timea.innerText = parseInt(pg_timea.innerText) + 3
		v_timea.innerText = parseInt(v_timea.innerText) + 1
		d_timeb.innerText = parseInt(d_timeb.innerText) + 1
		sg_timea.innerText = parseInt(sg_timea.innerText) + (placara - placarb)
		sg_timeb.innerText = parseInt(sg_timeb.innerText) - (placara - placarb)
	
	} else if (placara == placarb) {
		pg_timea.innerText = parseInt(pg_timea.innerText) + 1
		pg_timeb.innerText = parseInt(pg_timeb.innerText) + 1
		e_timea.innerText = parseInt(e_timea.innerText) + 1
		e_timeb.innerText = parseInt(e_timeb.innerText) + 1

	} else if (placarb > placara) {
		pg_timeb.innerText = parseInt(pg_timeb.innerText) + 3
		v_timeb.innerText = parseInt(v_timeb.innerText) + 1
		d_timea.innerText = parseInt(d_timea.innerText) + 1
		sg_timeb.innerText = parseInt(sg_timeb.innerText) + (placarb - placara)
		sg_timea.innerText = parseInt(sg_timea.innerText) - (placarb - placara)
	}
	ordenar()
}


function ordenar(){
	var valores = $('.ord').find('tr').get();
		
		valores.sort(function(a, b){

			valor1 = (parseInt($(a).children('td').eq(1).text().toUpperCase() + 10000)) + (parseInt($(a).children('td').eq(3).text().toUpperCase() + 1000)) + (parseInt($(a).children('td').eq(8).text().toUpperCase() + 500)) + (parseInt($(a).children('td').eq(6).text().toUpperCase()))
			valor2 = (parseInt($(b).children('td').eq(1).text().toUpperCase() + 10000)) + (parseInt($(b).children('td').eq(3).text().toUpperCase() + 1000)) + (parseInt($(b).children('td').eq(8).text().toUpperCase() + 500)) + (parseInt($(b).children('td').eq(6).text().toUpperCase()))
			return valor1 < valor2 ? 1 : valor1 > valor2 ? -1 : 0;
		});
		$.each(valores, (indice, elemento)=>{
			$('.ord').append(elemento)
		})
		numera()
}

function numera () {
	var valores = $('.ord').find('tr').get()
	
	valores.forEach(function(v, i) {
		$(v).children('th').text(i + 1)
		if (i < 8){
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
			$(v).css("backgroundColor", "E0FFFF")
		} else {
			$(v).css("backgroundColor", "fff")
		}
<<<<<<< HEAD
	})
}





=======

			
	}) 
}
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
