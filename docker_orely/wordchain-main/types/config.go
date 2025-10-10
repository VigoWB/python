/*
Copyright © 2021 SuperOrbital, LLC <info@superorbital.io>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package types

type Preferences struct {
	WordFile string
	Length   int64    `json:"length"`
	Divider  string   `json:"divider"`
	Prepend  string   `json:"prepend"`
	Postpend string   `json:"postpend"`
	Seed     string   `json:"seed"`
	Type     []string `json:"type"`
}

type Listener struct {
	Port int
}

type Chain struct {
	Chain string `json:"chain"`
}
