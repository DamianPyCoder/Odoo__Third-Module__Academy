## Correcciones:

La parte 2 tiene da un pequeño problema. El error que genera es debido a hacer copia/pega de dos funciones que calculaban los mismos campos pero que no he cambiado el nombre y se llaman igual:

    @api.depends('class_id')
    def _compute_number_of_seats(self):
        for record in self:
            _logger.info('_compute_number_of_seats number ='+str(self.class_id.number_of_seats))
            if self.class_id:
                self.number_of_seats = self.class_id.number_of_seats
            else:
                self.number_of_seats = 0

    @api.depends('number_of_seats','attendee_ids')
    def _compute_number_of_seats(self):
        for record in self:
            if self.number_of_seats and self.number_of_seats > 0:
                self.taken_seats = len(self.attendee_ids)*100/self.number_of_seats
            else:
                self.taken_seats = 0
