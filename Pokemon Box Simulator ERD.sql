CREATE TABLE `Ability` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL,
  `description` varchar2 UNIQUE NOT NULL,
  `is_hidden` bool NOT NULL
);

CREATE TABLE `CanLearn` (
  `species_id` integer,
  `move_id` integer,
  PRIMARY KEY (`species_id`, `move_id`)
);

CREATE TABLE `CaughtPokemon` (
  `id` integer PRIMARY KEY,
  `nickname` varchar2,
  `species_id` integer NOT NULL,
  `height` integer NOT NULL,
  `weight` integer NOT NULL,
  `exp` integer NOT NULL,
  `level` integer NOT NULL,
  `has_pokerus` boolean NOT NULL,
  `immune_to_pokerus` boolean NOT NULL,
  `nature_id` integer NOT NULL,
  `form_id` integer NOT NULL
);

CREATE TABLE `CaughtPokemonEffortValues` (
  `caught_pokemon_id` integer PRIMARY KEY,
  `hit_point_effort_value` integer NOT NULL,
  `attack_effort_value` integer NOT NULL,
  `defense_effort_value` integer NOT NULL,
  `special_attack_effort_value` integer NOT NULL,
  `special_defense_effort_value` integer NOT NULL,
  `speed_effort_value` integer NOT NULL
);

CREATE TABLE `CaughtPokemonIndividualValues` (
  `caught_pokemon_id` integer PRIMARY KEY,
  `hit_point_individual_value` integer NOT NULL,
  `attack_individual_value` integer NOT NULL,
  `defense_individual_value` integer NOT NULL,
  `special_attack_individual_value` integer NOT NULL,
  `special_defense_individual_value` integer NOT NULL,
  `speed_individual_value` integer NOT NULL
);

CREATE TABLE `CaughtPokemonStats` (
  `caught_pokemon_id` integer PRIMARY KEY,
  `max_hit_points` integer NOT NULL,
  `current_hit_points` integer NOT NULL,
  `attack` integer NOT NULL,
  `defense` integer NOT NULL,
  `special_attack` integer NOT NULL,
  `special_defense` integer NOT NULL,
  `speed` integer NOT NULL
);

CREATE TABLE `CurrentTrainer` (
  `caught_id` integer,
  `move_id` integer,
  PRIMARY KEY (`caught_id`, `move_id`)
);

CREATE TABLE `DamageCategory` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `Form` (
  `id` integer PRIMARY KEY,
  `species_id` integer NOT NULL,
  `name` varchar2 NOT NULL
);

CREATE TABLE `FormAbility` (
  `form_id` integer,
  `ability_id` integer,
  PRIMARY KEY (`form_id`, `ability_id`)
);

CREATE TABLE `FormType` (
  `form_id` integer,
  `type_id` integer,
  PRIMARY KEY (`form_id`, `type_id`)
);

CREATE TABLE `Gender` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `Item` (
  `id` integer PRIMARY KEY,
  `item_category_id` integer,
  `name` varchar2 UNIQUE NOT NULL,
  `description` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `ItemCategory` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `Moves` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL,
  `description` varchar2 UNIQUE,
  `type_id` integer NOT NULL,
  `damage_category_id` integer NOT NULL,
  `default_power_points` integer NOT NULL,
  `max_power_points` integer NOT NULL,
  `power` integer NOT NULL,
  `accuracy` float NOT NULL
);

CREATE TABLE `Nature` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `Sex` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `Species` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL,
  `base_hit_points` integer NOT NULL,
  `base_attack` integer NOT NULL,
  `base_defense` integer NOT NULL,
  `base_special_attack` integer NOT NULL,
  `base_special_defense` integer NOT NULL,
  `base_speed` integer NOT NULL,
  `average_height` integer NOT NULL,
  `average_weight` integer NOT NULL,
  `has_alternate_forms` bool NOT NULL
);

CREATE TABLE `SpeciesAbility` (
  `species_id` integer,
  `ability_id` integer,
  PRIMARY KEY (`species_id`, `ability_id`)
);

CREATE TABLE `SpeciesMaxEffortValue` (
  `species_id` integer PRIMARY KEY,
  `max_hit_point_effort_value` integer NOT NULL,
  `max_attack_effort_value` integer NOT NULL,
  `max_defense_effort_value` integer NOT NULL,
  `max_special_attack_effort_value` integer NOT NULL,
  `max_special_defense_effort_value` integer NOT NULL,
  `max_speed_effort_value` integer NOT NULL
);

CREATE TABLE `SpeciesMinEffortValue` (
  `species_id` integer PRIMARY KEY,
  `min_hit_point_effort_value` integer NOT NULL,
  `min_attack_effort_value` integer NOT NULL,
  `min_defense_effort_value` integer NOT NULL,
  `min_special_attack_effort_value` integer NOT NULL,
  `min_special_defense_effort_value` integer NOT NULL,
  `min_speed_effort_value` integer NOT NULL
);

CREATE TABLE `SpeciesType` (
  `species_id` integer,
  `type_id` integer,
  PRIMARY KEY (`species_id`, `type_id`)
);

CREATE TABLE `Team` (
  `id` integer PRIMARY KEY,
  `trainer_id` integer UNIQUE NOT NULL
);

CREATE TABLE `Trainer` (
  `id` integer PRIMARY KEY,
  `name` varchar2 NOT NULL,
  `adventure_start_datetime` datetime NOT NULL,
  `trainer_class_id` integer,
  `money` integer NOT NULL
);

CREATE TABLE `TrainerClass` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

CREATE TABLE `Type` (
  `id` integer PRIMARY KEY,
  `name` varchar2 UNIQUE NOT NULL
);

ALTER TABLE `Species` ADD FOREIGN KEY (`id`) REFERENCES `CanLearn` (`species_id`);

ALTER TABLE `Moves` ADD FOREIGN KEY (`id`) REFERENCES `CanLearn` (`move_id`);

ALTER TABLE `CaughtPokemon` ADD FOREIGN KEY (`species_id`) REFERENCES `Species` (`id`);

ALTER TABLE `CaughtPokemon` ADD FOREIGN KEY (`nature_id`) REFERENCES `Nature` (`id`);

ALTER TABLE `CaughtPokemon` ADD FOREIGN KEY (`form_id`) REFERENCES `Form` (`id`);

ALTER TABLE `CaughtPokemonEffortValues` ADD FOREIGN KEY (`caught_pokemon_id`) REFERENCES `CaughtPokemon` (`id`);

ALTER TABLE `CaughtPokemonIndividualValues` ADD FOREIGN KEY (`caught_pokemon_id`) REFERENCES `CaughtPokemon` (`id`);

ALTER TABLE `CaughtPokemonStats` ADD FOREIGN KEY (`caught_pokemon_id`) REFERENCES `CaughtPokemon` (`id`);

ALTER TABLE `Species` ADD FOREIGN KEY (`id`) REFERENCES `CurrentTrainer` (`caught_id`);

ALTER TABLE `Moves` ADD FOREIGN KEY (`id`) REFERENCES `CurrentTrainer` (`move_id`);

ALTER TABLE `Form` ADD FOREIGN KEY (`species_id`) REFERENCES `Species` (`id`);

ALTER TABLE `Form` ADD FOREIGN KEY (`id`) REFERENCES `FormAbility` (`form_id`);

ALTER TABLE `Ability` ADD FOREIGN KEY (`id`) REFERENCES `FormAbility` (`ability_id`);

ALTER TABLE `Form` ADD FOREIGN KEY (`id`) REFERENCES `FormType` (`form_id`);

ALTER TABLE `Type` ADD FOREIGN KEY (`id`) REFERENCES `FormType` (`type_id`);

ALTER TABLE `Item` ADD FOREIGN KEY (`item_category_id`) REFERENCES `ItemCategory` (`id`);

ALTER TABLE `Moves` ADD FOREIGN KEY (`type_id`) REFERENCES `Type` (`id`);

ALTER TABLE `Moves` ADD FOREIGN KEY (`damage_category_id`) REFERENCES `DamageCategory` (`id`);

ALTER TABLE `Species` ADD FOREIGN KEY (`id`) REFERENCES `SpeciesAbility` (`species_id`);

ALTER TABLE `Ability` ADD FOREIGN KEY (`id`) REFERENCES `SpeciesAbility` (`ability_id`);

ALTER TABLE `SpeciesMaxEffortValue` ADD FOREIGN KEY (`species_id`) REFERENCES `Species` (`id`);

ALTER TABLE `SpeciesMinEffortValue` ADD FOREIGN KEY (`species_id`) REFERENCES `Species` (`id`);

ALTER TABLE `Species` ADD FOREIGN KEY (`id`) REFERENCES `SpeciesType` (`species_id`);

ALTER TABLE `Type` ADD FOREIGN KEY (`id`) REFERENCES `SpeciesType` (`type_id`);

ALTER TABLE `Team` ADD FOREIGN KEY (`trainer_id`) REFERENCES `Trainer` (`id`);

ALTER TABLE `Trainer` ADD FOREIGN KEY (`trainer_class_id`) REFERENCES `TrainerClass` (`id`);
