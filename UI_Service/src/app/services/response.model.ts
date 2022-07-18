import { JsonObject, JsonProperty } from 'json2typescript';

@JsonObject('Response')
export class Response<T> {
  data: T = undefined;

  @JsonProperty('returncode', Number)
  returncode: number = undefined;

  @JsonProperty('timestamp', Number)
  timestamp: number = undefined;
}