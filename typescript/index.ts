/**
 * Generic dictionary
 */
export interface I18NDictionary<T> {
  generatedAt: Date;
  /**
   * string that indicate version (e.g. "0.0.1", "1,0.0")
   */
  version: string;
  /**
   * Translate entries
   */
  data: T[];
}

/**
 * LANG: en, ja, it, es, fr, de, kr, zh_cn, zh_tw ...
 */
export type I18NEntry = { [lang: string] : string };

/**
 * Basic dictionary entry.
 */
export interface BasicEntry {
  /**
   * Text entry of each country.
   */
  i18n: I18NEntry;
}

/**
 * Simple dictionary.
 */
export type BasicDictionary = I18NDictionary<BasicEntry>;

/**
 * Pokemon name dictionary.
 */
export type PokemonDictionary = I18NDictionary<PokemonEntry>;

/**
 * Pokemon name dictionary entry.
 */
export interface PokemonEntry extends BasicEntry {
  /**
   * Picture book number of Pokemon
   */
  number: number;
}

/**
 * Pokemon moves dictionary entry.
 */
export type PokemonMovesDictionary = I18NDictionary<BasicEntry>;
