L’exercici està basat en el tutorial d’odoo: 
https://www.odoo.com/documentation/16.0/developer/tutorials/backend.html

# ODOO

## Creació del mòdul. Model i vista per defecte (openacademy-1)
- [x] Creació de l’estructura de carpetes del mòdul fent servir l’utilitat odoo scaffold.
- [x] Creem el model course amb els camps name i description.
- [x] Reanomenem el fitxer models.py a course.py.
- [x] Dividim el fitxer views.xml en course.xml i menu.xml
- [x] Actualitzem el fitxer de la carpeta security i el manifest.py
- [x] Instal·lació del mòdul des de l’aplicació web d’odoo.
- [x] Visualització dels menús del mòdul.

## Actions. Vistes customizades form i search (openacademy-2)
- [x] Creem una vista formulari fent servir elements estructurals de tipus sheet, group i notebook.
- [x] Creem una vista search per poder buscar per nom i description.

## Camps relacionals (openacademy-3)
- [x] Creem un nou model session. Una sessió és l'ocurrència d'un curs impartit en un moment determinat per a un públic determinat. El model session tindrà els següents camps: name, start_date, duration and number_of_seats. 
- [x] Creem una vista pel nou model i l’afegim al menú de l’aplicació.
- [x] Relacions Many2one: Modificar els models i vistes necessàries per tenir en compte les relacions següents:
- [x] Un curs té un responsable (responsible_id) que pertany al model res.users.
- [x] Una sessió té un instructor (instructor_id) que pertany al model res.partner.
- [x] Una sessió sempre té associat un curs.
- [x] Relacions One2many:
- [x] Afegir al model i a la vista course les sessions associates (session_ids)
- [x] Relacions Many2many:
- [x] Afegir al model i a la vista session els assistents a la sessió. Els assistents (attendee_ids) pertanyen al model res.partner

## Computed fields i onchange (openacademy-4)
- [x] Movem duration a Course, és més correcte que tenir-lo a Session.
- [x] Creem el model classroom amb els següents camps: name, number_of_seats, has_screen i screen_size (big: 86IN, medium: 75IN i small: 65IN).
- [x] Afegim el camp relacional classroom_id al model session (Many2one).
- [x] Calculem el camp number_of_seats del model session copiant el valor number_of_seats del model classroom. (calculated field).
- [x] Calculem el camp taken_seats del model session a partir dels camps number_of_seats i attendee_ids. (calculated field). Buscar com fer servir el widget progressbar.
- [x] Quan canviem el valor del camp has_screen to True al model classroom, s’ha d’assignar el valor 75IN (medium) en screen_size. (onchange).

## Actions. Default values (openacademy-5)
- [ ] Afegim un camp state al model i a la vista formulari de session.
- [ ] En crear una sessió, aquesta es crearà en estat New (default value).
- [ ] Les sessions poden canviar d’estat. Per això farem servir dos botons a la vista formulari de session: Cancel i Done. Els canvis d’estat permesos seran:
- [ ] De New a Planned quan afegim la data d’inici (start_date) (onchange).
- [ ] De Planned a Done quan cliquem el botó Done (action done). 
- [ ] De Planned o New a Cancel quan cliquem el botó Cancel (action cancel).
- [ ] La resta de transicions no són permeses, per exemple de New a Done o de Done a Cancel.
- [ ] Buscar com fer servir el widget statusbar.

## Actions. Constrains (openacademy-6)
- [ ] No es permet que hi hagi menys d’un seient a una classe (sql constraint)
- [ ] Obrirem una nova entrada al menú horitzontal que es dirà Settings.
- [ ] D’aquesta entrada penjarà una acció ‘Course tags’ associada a un nou model course_tag 
- [ ] El model course_tag només tindrà un camp name. Els valors del camp name seran únics, és a dir, no podrà haver-hi dos tags amb el mateix nom (sql constraint).
- [ ] Afegirem course_tag_ids al model i a la vista course. Buscar com fer servir el widget many2many_tags.
- [ ] No es permetrà que hi hagin més participants que seients a una sessió (python constrain)

## Actions. Herència (openacademy-7)
- [ ] No es podran esborrar les sessions amb estat Planned. (herencia en python)
- [ ] Modificar el model res.partner per afegir un camp booleà que indiqui si aquest partner és instructor o no. Afegiu el camp a la vista. (herencia model i vista)
- [ ] Afegiu també a la vista formulari de res.partner les sessions que ha impartit un instructor. Poseu-les a una pàgina nova del notebook. (herencia model i vista)
- [ ] En seleccionar l'instructor per una sessió només els partners que tinguin el valor True al camp instructor es mostraran. (dominis)
