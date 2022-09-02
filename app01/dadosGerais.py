# -*- coding: utf-8 -*-

from django.http import HttpResponse,HttpResponseRedirect
import pyodbc as p
import openpyxl
from . import funcoes_mysql
import os
import sys
import mysql.connector
import datetime
import csv
from . import stringConnexao
#from openpyxl.styles import NamedStyle


def incluir(planilha,iduser):
                mysql=stringConnexao.strMySql() 
		lote = str(datetime.datetime.now().today())[0:19]
		funcoes_mysql.ler_plan_pastas(planilha, lote, iduser, 'view002')


                cnx1.mysql.connector.connect(user=mysql.get('user'),password=mysql.get('password'),host=mysql.get('host'),database=mysql.get('database'))
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="dadosDoProcesso2.csv"'
		try:
			cursor = cnx1.cursor()

			stmt="""
			select g.chave,d.*,g.id_seq from tab_dadosGerais g left join view017_py_dadosGerais d on g.chave=d.pasta
			                    where g.lote=%s order by g.id_seq
			"""
			cursor.execute(stmt, (lote,))

			row = cursor.fetchone()

			writer = csv.writer(response, delimiter=';')
			response.write(u'\ufeff'.encode('utf8'))
            
			while row is not None:
				writer.writerow((
					row[0],row[1],row[2],
						row[0],row[1],row[2]
				))
				row = cursor.fetchone() 
			cursor.close()
			cnx1.close()
                
		except p.IntegrityError:
			print ("Erro na inclusao")
                
		return response

