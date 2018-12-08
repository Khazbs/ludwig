#!/usr/bin/env python3

import random

def union(iterable, start=set()):
	for item in iterable:
		start |= item
	return start

def intersect(iterable, start=set()):
	for item in iterable:
		start &= item
	return start

class World:
	'''Мир'''
	facts = set()  # Целокупность фактов (1.1)
	existing_events = set()  # Целокупность существующих событий (2.04)
	substance = objects = set()  # Объекты образуют субстанцию мира (2.021)
	def __init__(self, facts):
		self.facts |= set(facts)
		for fact in facts:
			self.existing_events |= fact.events
		self.substance |= union(union(set(event.structure.keys()) for event in fact.events) for fact in facts)

class Fact:
	'''Факт'''
	events = set()  # Со-бытия, существование которых характеризует факт
	def __init__(self, events):
		self.events |= set(events)

class Event:
	'''Со-бытие'''
	structure = relations = dict()  # Структура события, то есть способ соотношения объектов в со-бытии (2.032, 2.031)
	def __init__(self, relations):
		for relation in relations:
			relation.first_object.form |= {self}  # Если объект участвует в событии, то его форма содержит возможность этого события
			relation.second_object.form |= {self}  # Если объект участвует в событии, то его форма содержит возможность этого события
			if relation.first_object in self.structure:
				self.structure[relation.first_object] += [relation]
			else:
				self.structure[relation.first_object] = [relation]
			if relation.second_object in self.structure:
				self.structure[relation.second_object] += [relation ** -1]
			else:
				self.structure[relation.second_object] = [relation ** -1]

class Object:
	'''Объект, предмет, вещь'''
	form = possible_events = set()  # Возможность объекта вхождения в со-бытия - его форма (2.0141)
	def __init__(self, possible_events=set()):
		self.form |= possible_events

class LogicalRepresentation():
	'''Логическое представление, которое по умолчанию с некоторой вероятностью, зависящей от "точности", может оказаться ложным'''
	source = None
	correct = None
	def __init__(self, entity, correct=None):
		self.source = entity
		if correct is None:
			correct = exactness > random.random()
		self.correct = correct

class Interaction:
	'''Способ взаимодействия между предметами'''
	interaction = None
	inverse = None  # Является ли способ взаимодействия обратным (то есть взаимодействием от B к A вместо от A к B)
	def __init__(self, interaction, inverse=False):
		self.interaction = str(interaction)
		self.inverse = inverse
	def __pow__(self, power):  # Оператор для определения обратного взаимодействия
		if power not in (-1, 1):
			raise NotImplementedError
		elif power == -1:
			return Interaction(self.interaction, not self.inverse)
	def __repr__(self):
		return ("inverse of " if self.inverse else "") + self.interaction

class Relation:
	'''Соотношение между объектами'''
	first_object = None
	second_object = None
	interaction = None  # Способ соотношения между объектами
	def __init__(self, first_object, second_object, interaction):
		self.first_object = first_object
		self.second_object = second_object
		self.interaction = interaction
	def __pow__(self, power):  # Оператор для определения обратного соотношения
		if power not in (-1, 1):
			raise NotImplementedError
		elif power == -1:
			return Relation(self.second_object, self.first_object, self.interaction ** -1)

class Picture(Fact):  # Картина - факт
	'''Картина'''
	elements = set()  # Объектам в картине соответствуют элементы картины
	representation = None
	meaning = None  # Смысл картины
	correct = None
	def __init__(self, entity, correct=None):
		self.meaning = entity  # Смысл картины - то, что она изображает
		self.representation = LogicalRepresentation(entity, correct)
		element_correct = True if correct else None
		if type(entity) is World:
			self.events |= set(entity.existing_events)
			self.elements |= set((LogicalRepresentation(obj, element_correct) for obj in entity.substance))
		elif type(entity) is Event:
			self.events |= {entity}
			self.elements |= set((LogicalRepresentation(obj, element_correct) for obj in entity.structure.keys()))
		elif type(entity) is Object:
			self.events |= set(entity.form)
			self.elements |= {LogicalRepresentation(entity, element_correct)}
		else:
			raise NotImplementedError
		if correct is None:
			correct = self.representation.correct and intersect((element.correct for element in self.elements), True)
		self.correct = correct

class Thought:
	'''Мысль'''
	thought = None
	def __init__(self, fact):
		if type(fact) is Fact:
			self.thought = LogicalRepresentation(fact)
		else:
			raise TypeError


class Language:
	'''Язык'''
	sentences = list()  # Целокупность предложений
	def __init__(self, sentences):
		self.sentences = sentences

class Sentence:  # Предложение
	pass

class Symtence:  # Знак-предложение
	pass

# Волшебные константы
exactness = 1  # "Точность" мыслящего, то есть вероятность истинности его логического представления

print('--- Ludwig module has been loaded ---')
