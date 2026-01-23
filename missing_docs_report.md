# Documentation Coverage Report

**Analysis Target:** `C:/GitHub/MidiKobold/xml`

- **Total Classes Found:** 397

## 📉 Missing Documentation
| Class Name | Missing Items |
| :--- | :--- |
| `AckNackMessageHandler` | Member: `MAX_PENDING_ACKS`<br>Member: `m_pending_acks`<br>Member: `m_next_message_id`<br>Member: `m_acks_mutex`<br>Member: `m_comms`<br>...and 1 more |
| `AdvertisedDeviceCallbacks` | Member: `advDevice`<br>Member: `doConnect`<br>Member: `scanDone`<br>Member: `specificTarget`<br>Member: `enableConnection`<br>...and 2 more |
| `AppGridView` | Member: `MAX_APPS`<br>Member: `m_apps`<br>Member: `COLS`<br>Member: `ROWS`<br>Member: `CELL_WIDTH`<br>...and 2 more |
| `ArpOverflowTest` | Class Description<br>Member: `mock_transport`<br>Member: `mock_system_model`<br>Member: `mock_chord_processor`<br>Member: `mock_scale_quantizer`<br>...and 9 more |
| `ArpScaleBugTest` | Class Description<br>Member: `mock_chord_provider`<br>Member: `mock_system_model`<br>Member: `mock_transport`<br>Member: `mock_midi_router`<br>...and 12 more |
| `ArpTest` | Class Description<br>Member: `m_modulation_dispatcher`<br>Member: `m_mock_entropy_pool`<br>Member: `mock_chord_provider`<br>Member: `mock_system_model`<br>...and 10 more |
| `Arpeggiator` | Member: `ArpDirection`<br>Member: `ArpTest`<br>Member: `m_settings`<br>Member: `m_note_input_buffer`<br>Member: `m_note_input_buffer_count`<br>...and 30 more |
| `ArpeggiatorAdapter` | Member: `m_arpeggiator` |
| `ArpeggiatorView` | Member: `m_ball_y`<br>Member: `m_ball_velocity`<br>Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset`<br>...and 5 more |
| `AsyncFileIO` | Member: `m_request_queue`<br>Member: `m_response_queue`<br>Member: `operator=`<br>Member: `fileIOTask` |
| `AsyncRhythmGenerator` | Member: `m_task_handle`<br>Member: `m_request_queue`<br>Member: `m_status`<br>Member: `m_cancel_requested`<br>Member: `m_progress`<br>...and 6 more |
| `AudioProcessor` | Member: `operator=` |
| `BLEMIDI_ArduinoBLE` | Class Description<br>Member: `_bleMidiTransport`<br>Member: `_central`<br>Member: `mRxBuffer`<br>Member: `begin`<br>...and 9 more |
| `BLEMIDI_Client_ESP32` | Member: `_client`<br>Member: `_advertising`<br>Member: `_characteristic`<br>Member: `pSvc`<br>Member: `firstTimeSend`<br>...and 19 more |
| `BLEMIDI_ESP32` | Class Description<br>Member: `_server`<br>Member: `_advertising`<br>Member: `_characteristic`<br>Member: `_bleMidiTransport`<br>...and 11 more |
| `BLEMIDI_ESP32_NimBLE` | Class Description<br>Member: `_server`<br>Member: `_advertising`<br>Member: `_characteristic`<br>Member: `_bleMidiTransport`<br>...and 11 more |
| `BLEMIDI_Transport` | Class Description<br>Member: `Settings`<br>Member: `mRxBuffer`<br>Member: `mRxIndex`<br>Member: `mTxBuffer`<br>...and 20 more |
| `BLEMIDI_nRF52` | Class Description<br>Member: `_bleMidiTransport`<br>Member: `MyServerCallbacks`<br>Member: `MyCharacteristicCallbacks`<br>Member: `begin`<br>...and 7 more |
| `BaseModule` | Member: `begin`<br>Member: `handleMidiEvent`<br>Member: `processTick`<br>Member: `onTransportCommand`<br>Member: `applyModulation`<br>...and 2 more |
| `BaseView` | Member: `m_view_manager`<br>Member: `m_display` |
| `BasicMidiMapper` | Member: `m_mappings`<br>Member: `m_mapping_count` |
| `BleManager` | Class Description<br>Member: `_deviceName`<br>Member: `getInstance`<br>Member: `begin`<br>Member: `operator=` |
| `BoidHarmonizer` | Class Description<br>Member: `MAX_AGENTS`<br>Member: `m_settings`<br>Member: `m_midi_router`<br>Member: `m_quantizer`<br>...and 5 more |
| `BoidsSettingsProvider` | Class Description<br>Member: `getBoidsSettings`<br>Member: `setBoidsSettings` |
| `BoidsView` | Member: `m_cached_settings` |
| `BooleanPatchDataProvider` | Class Description<br>Member: `get_patch_parameter` |
| `BootModeManager` | Member: `operator=` |
| `CcEnvelopeFollower` | Member: `MAX_ENVELOPES`<br>Member: `m_envelopes`<br>Member: `m_settings`<br>Member: `m_transport_manager`<br>Member: `m_midi_router`<br>...and 7 more |
| `CcEnvelopeFollowerSettingsProvider` | Class Description<br>Member: `getCcEnvelopeFollowerSettings`<br>Member: `setCcEnvelopeFollowerSettings` |
| `CcEnvelopeFollowerTest` | Class Description<br>Member: `m_follower`<br>Member: `m_expander_stub`<br>Member: `m_comms_stub`<br>Member: `m_midi_output_mock`<br>...and 2 more |
| `CcEnvelopeFollowerView` | Member: `m_cached_settings`<br>Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset` |
| `ChordProcessorAdapter` | Member: `m_chord_processor` |
| `ChordProcessorView` | Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_cached_settings` |
| `ChordProcessorVoiceLeadingTest` | Class Description<br>Member: `chord_processor` |
| `CommonDataLibrary` | Class Description<br>Member: `_fs`<br>Member: `_rootPath`<br>Member: `init`<br>Member: `createDirectory`<br>...and 7 more |
| `CommunicationManager` | Member: `s_instance`<br>Member: `MESSAGE_POOL_SIZE`<br>Member: `MAX_MESSAGE_HANDLERS`<br>Member: `m_task_handle`<br>Member: `m_outgoing_queue`<br>...and 16 more |
| `CommunicationService` | Member: `getMessage`<br>Member: `returnMessage`<br>Member: `addPeer` |
| `ConcreteMicroOsc` | Class Description<br>Member: `beginMessage`<br>Member: `endMessage`<br>Member: `readyToSendMessage`<br>Member: `onOscMessageReceived`<br>...and 1 more |
| `ConcreteMicroOscSecurity` | Class Description<br>Member: `beginMessage`<br>Member: `endMessage`<br>Member: `readyToSendMessage`<br>Member: `onOscMessageReceived`<br>...and 1 more |
| `CoreThreadingTest` | Class Description<br>Member: `mock_time_source`<br>Member: `transport_manager` |
| `CreativeModuleTestFixture` | Class Description<br>Member: `mock_midi_router`<br>Member: `mock_transport_manager`<br>Member: `mock_entropy_pool`<br>Member: `SetUp`<br>...and 1 more |
| `CvOutputDispatcher` | Member: `m_settings`<br>Member: `m_ledcService` |
| `CvOutputEditView` | Member: `m_mappingIndex`<br>Member: `m_selectedField`<br>Member: `m_isEditing`<br>Member: `m_cached_settings`<br>Member: `s_mapping_index` |
| `CvOutputListView` | Member: `m_cached_settings` |
| `CvParamSelectView` | Member: `m_mappingIndex`<br>Member: `m_definition`<br>Member: `m_param_indices`<br>Member: `m_param_indices_count`<br>Member: `m_selectedIndex`<br>...and 1 more |
| `DashboardView` | Member: `m_selected_index`<br>Member: `drawTempoWidget`<br>Member: `drawScaleWidget`<br>Member: `drawPinnedWidgets`<br>Member: `getTransportManager`<br>...and 1 more |
| `DefaultsWarningView` | Member: `m_time_source`<br>Member: `m_enter_time`<br>Member: `m_timeout_seconds`<br>Member: `m_scroll_offset` |
| `DefinitionLoader` | Member: `m_deviceDefinitionManager`<br>Member: `m_settings`<br>Member: `operator=` |
| `DesignGeneratorsMenuView` | Class Description |
| `DesignMenuView` | Class Description |
| `DesignModulationMenuView` | Class Description |
| `DesignProcessorsMenuView` | Class Description |
| `DeviceDefinitionManager` | Class Description<br>Member: `m_definitions`<br>Member: `m_definition_count`<br>Member: `m_loaded`<br>Member: `getInstance`<br>...and 4 more |
| `DisplayManager` | Member: `m_display`<br>Member: `m_task_handle`<br>Member: `m_context` |
| `ESP32TimeSource` | Class Description |
| `EchoChamber` | Member: `m_transport_manager`<br>Member: `m_midi_router`<br>Member: `m_settings_provider`<br>Member: `m_random_generator`<br>Member: `m_echo_buffer`<br>...and 9 more |
| `EchoChamberAdapter` | Member: `m_echo_chamber` |
| `EchoChamberSettingsProvider` | Class Description<br>Member: `getEchoChamberSettings`<br>Member: `setEchoChamberSettings` |
| `EchoChamberView` | Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset`<br>Member: `m_cached_settings` |
| `EntropyPoolRTTest` | Class Description<br>Member: `SetUp`<br>Member: `TearDown` |
| `EntropySource` | Member: `getRandomUint32`<br>Member: `getRandomUint8` |
| `Esp32Gpio` | Class Description |
| `Esp32I2sAudioDriver` | Class Description |
| `Esp32I2sOutput` | Class Description<br>Member: `begin`<br>Member: `end`<br>Member: `write` |
| `Esp32InputHardware` | Class Description<br>Member: `encoder_`<br>Member: `last_count_` |
| `Esp32LedController` | Class Description<br>Member: `HalFactory`<br>Member: `getInstance` |
| `Esp32Ssd1306Display` | Member: `_display` |
| `EspNowTransport` | Member: `s_instance`<br>Member: `m_recv_cb`<br>Member: `m_recv_context`<br>Member: `m_peers`<br>Member: `m_peer_count` |
| `EuclideanGeneratorView` | Member: `State`<br>Member: `m_animation_angle`<br>Member: `m_state` |
| `EuclideanSequencer` | Member: `m_steps`<br>Member: `m_pulses`<br>Member: `m_rotation` |
| `EuclideanSequencerTest` | Class Description<br>Member: `sequencer` |
| `ExpanderManager` | Member: `ExpanderManagerTest`<br>Member: `m_time_source`<br>Member: `m_connected_expanders`<br>Member: `m_expander_count`<br>Member: `operator=` |
| `ExpanderManagerTest` | Class Description<br>Member: `timeSource`<br>Member: `SetUp`<br>Member: `createManager` |
| `ExpanderSync` | Member: `operator=` |
| `ExpanderSyncTest` | Class Description<br>Member: `SetUp` |
| `ExpanderTransport` | Class Description<br>Member: `RecvCallback`<br>Member: `begin`<br>Member: `sendMessage`<br>Member: `addPeer`<br>...and 3 more |
| `ExpanderTransportManager` | Class Description<br>Member: `SYNC_INTERVAL_MS`<br>Member: `SYNC_LOSS_TIMEOUT_US`<br>Member: `CLOCK_SYNC_ALPHA`<br>Member: `m_last_sync_time`<br>...and 11 more |
| `FastRandom` | Member: `m_state`<br>Member: `next`<br>Member: `next`<br>Member: `next` |
| `Fifo` | Class Description<br>Member: `size`<br>Member: `numberOfElements`<br>Member: `nextIn`<br>Member: `nextOut`<br>...and 6 more |
| `File` | Class Description<br>Member: `impl`<br>Member: `write`<br>Member: `write`<br>Member: `close`<br>...and 2 more |
| `FilePatchIO` | Member: `m_file`<br>Member: `write`<br>Member: `read` |
| `FileSelectView` | Member: `State`<br>Member: `m_state`<br>Member: `m_items`<br>Member: `m_titleBuffer`<br>Member: `s_channel` |
| `FileSync::BootRequestManager` | Member: `m_request`<br>Member: `m_loaded`<br>Member: `NVS_NAMESPACE`<br>Member: `NVS_KEY_BOOT`<br>Member: `BootRequestManager`<br>...and 2 more |
| `FileSync::ChangeDetector` | Member: `m_pending`<br>Member: `m_pending_count`<br>Member: `ChangeDetector`<br>Member: `ChangeDetector`<br>Member: `operator=`<br>...and 1 more |
| `FileSync::HashStorage` | Member: `m_database`<br>Member: `m_storage_manager`<br>Member: `m_loaded`<br>Member: `HASH_DB_PATH`<br>Member: `HashStorage`<br>...and 2 more |
| `FileSync::SettingsStore` | Member: `m_settings`<br>Member: `m_loaded`<br>Member: `NVS_NAMESPACE`<br>Member: `NVS_KEY`<br>Member: `SettingsStore`<br>...and 2 more |
| `FluxCapacitor` | Member: `FluxCapacitorTest`<br>Member: `MAX_DELAYED_NOTES`<br>Member: `DRIFT_WALK_MIN`<br>Member: `DRIFT_WALK_MAX`<br>Member: `PROBABILITY_MAX`<br>...and 23 more |
| `FluxCapacitorAdapter` | Member: `m_flux_capacitor` |
| `FluxCapacitorTest` | Class Description<br>Member: `flux`<br>Member: `mock_transport`<br>Member: `mock_random`<br>Member: `mock_router`<br>...and 5 more |
| `FluxCapacitorView` | Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset`<br>Member: `m_cached_settings`<br>Member: `m_flux_capacitor` |
| `FxSequencer` | Member: `m_settings`<br>Member: `m_global_tick_counter`<br>Member: `m_current_step`<br>Member: `m_last_midi_event`<br>Member: `m_playing_notes`<br>...and 18 more |
| `FxSequencerAdapter` | Member: `m_fx_sequencer`<br>Member: `m_sequencer`<br>Member: `process` |
| `FxSequencerMainView` | Member: `m_selected_param`<br>Member: `m_is_editing` |
| `FxSequencerStepListView` | Member: `m_cached_settings` |
| `FxSequencerTest` | Class Description<br>Member: `mock_midi_router`<br>Member: `mock_transport`<br>Member: `fx_sequencer`<br>Member: `fx_seq`<br>...and 3 more |
| `GenrePresetTest` | Class Description<br>Member: `chord_processor`<br>Member: `SetUp` |
| `GravityWell` | Member: `GravityWellTest`<br>Member: `MAX_BALLS`<br>Member: `MIN_MIDI_VELOCITY`<br>Member: `MAX_MIDI_VELOCITY`<br>Member: `MIN_MIDI_NOTE`<br>...and 20 more |
| `GravityWellAdapter` | Member: `m_gravityWell` |
| `GravityWellSettingsProvider` | Class Description<br>Member: `getGravityWellSettings`<br>Member: `setGravityWellSettings` |
| `GravityWellTest` | Class Description<br>Member: `gw`<br>Member: `SetUp`<br>Member: `TearDown`<br>Member: `noteOn`<br>...and 1 more |
| `GravityWellView` | Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset`<br>Member: `m_cached_settings` |
| `GrooveHumanizer` | Member: `m_midi_router`<br>Member: `m_transport_manager`<br>Member: `m_settings`<br>Member: `m_scheduler`<br>Member: `m_note_delay_map`<br>...and 3 more |
| `GrooveHumanizerView` | Member: `m_cached_settings` |
| `HalFactory` | Member: `operator=` |
| `HarmonizerOptimizationTest` | Class Description<br>Member: `engine` |
| `HarmonyProcessor` | Member: `_scaleManager`<br>Member: `m_quantizer`<br>Member: `_root_note` |
| `HeartbeatMessageHandler` | Member: `m_time_source` |
| `HeavyProcessor` | Class Description<br>Member: `getInstance`<br>Member: `process`<br>Member: `onNoteOn`<br>Member: `onNoteOff`<br>...and 4 more |
| `HumanizerSettingsProvider` | Class Description<br>Member: `getHumanizerSettings`<br>Member: `setHumanizerSettings` |
| `HybridStrategy` | Class Description<br>Member: `OutputMode`<br>Member: `m_output_mode`<br>Member: `m_pitchbend_strategy`<br>Member: `m_mpe_strategy`<br>...and 9 more |
| `IAudioDriver` | Class Description |
| `IAudioOutput` | Class Description<br>Member: `begin`<br>Member: `end`<br>Member: `write` |
| `IDisplay` | Class Description<br>Member: `DISPLAY_BLACK`<br>Member: `DISPLAY_WHITE`<br>Member: `DISPLAY_INVERSE`<br>Member: `clearDisplay`<br>...and 17 more |
| `IFile` | Class Description<br>Member: `read`<br>Member: `write`<br>Member: `seek`<br>Member: `position`<br>...and 3 more |
| `IFileStream` | Member: `file_`<br>Member: `write`<br>Member: `write`<br>Member: `availableForWrite`<br>Member: `flush`<br>...and 4 more |
| `IFileSystem` | Class Description<br>Member: `open`<br>Member: `listDir`<br>Member: `exists`<br>Member: `mkdir`<br>...and 3 more |
| `IGpio` | Member: `PinMode` |
| `ILedController` | Class Description |
| `IMidiOutput` | Class Description<br>Member: `sendMidiMessage`<br>Member: `sendSysEx` |
| `ISystemModel` | Class Description<br>Member: `lock`<br>Member: `unlock`<br>Member: `getChordProcessorSettings`<br>Member: `setChordProcessorSettings`<br>...and 32 more |
| `ITransportManager` | Class Description<br>Member: `sendCommand`<br>Member: `start`<br>Member: `stop`<br>Member: `setTempo`<br>...and 11 more |
| `InputHardware` | Class Description<br>Member: `begin`<br>Member: `readEncoder`<br>Member: `readButton` |
| `LFO` | Member: `m_settings`<br>Member: `m_phase`<br>Member: `m_current_value`<br>Member: `m_euclidean_pattern`<br>Member: `m_euclidean_step_index`<br>...and 2 more |
| `LedcManager` | Member: `operator=` |
| `LocalSystemModelStub` | Class Description<br>Member: `m_global_settings`<br>Member: `m_arp_settings`<br>Member: `getChordProcessorSettings`<br>Member: `setChordProcessorSettings`<br>...and 32 more |
| `Logger` | Member: `operator=` |
| `Looper` | Member: `m_state`<br>Member: `m_current_tick`<br>Member: `m_loop_length_ticks`<br>Member: `m_event_count`<br>Member: `m_playback_index`<br>...and 4 more |
| `LooperAdapter` | Member: `m_looper` |
| `MIDIMapper` | Member: `m_settings`<br>Member: `m_settings`<br>Member: `applyMapping`<br>Member: `calculateVelocity` |
| `MIDIMapperAdapter` | Class Description<br>Member: `m_mapper`<br>Member: `process` |
| `MIDIRouter` | Member: `m_task_handle`<br>Member: `m_midi_queue`<br>Member: `m_high_res_parser`<br>Member: `m_sysex_subscribers`<br>Member: `m_processors`<br>...and 4 more |
| `MPEPitchBendTest` | Class Description<br>Member: `calc` |
| `MPEStrategy` | Class Description<br>Member: `MPE_MASTER_CHANNEL`<br>Member: `MPE_FIRST_MEMBER`<br>Member: `MPE_LAST_MEMBER`<br>Member: `MPE_MAX_VOICES`<br>...and 14 more |
| `MainController` | Member: `m_modules`<br>Member: `m_usb_midi_handler`<br>Member: `m_ble_midi_handler`<br>Member: `m_midi_clock`<br>Member: `m_expander_sync`<br>...and 40 more |
| `MainMenuView` | Member: `m_model` |
| `MapToScaleTest` | Class Description<br>Member: `calc` |
| `MemoryPatchIO` | Member: `m_buffer`<br>Member: `m_capacity`<br>Member: `m_pos`<br>Member: `write`<br>Member: `read`<br>...and 3 more |
| `MemoryWatermarkTest` | Class Description<br>Member: `setup` |
| `MenuLayoutSettingView` | Member: `m_selected_index` |
| `MenuStructureTest` | Class Description<br>Member: `viewManager`<br>Member: `display`<br>Member: `displayManager`<br>Member: `timeSource`<br>...and 3 more |
| `MicroOsc` | Class Description<br>Member: `tOscCallbackFunction`<br>Member: `bundle`<br>Member: `message`<br>Member: `callback`<br>...and 38 more |
| `MicroOscMessage` | Class Description<br>Member: `MicroOsc`<br>Member: `source`<br>Member: `format`<br>Member: `marker`<br>...and 16 more |
| `MicroOscSecurityTest` | Class Description<br>Member: `mockPrint`<br>Member: `osc`<br>Member: `SetUp`<br>Member: `TearDown` |
| `MicroOscSlip` | Class Description<br>Member: `slip`<br>Member: `inputBuffer`<br>Member: `beginMessage`<br>Member: `endMessage`<br>...and 3 more |
| `MicroOscTest` | Class Description<br>Member: `mockPrint`<br>Member: `osc`<br>Member: `SetUp`<br>Member: `TearDown` |
| `MicroOscUdp` | Class Description<br>Member: `udp`<br>Member: `inputBuffer`<br>Member: `destinationIp`<br>Member: `destinationPort`<br>...and 6 more |
| `MicrotonalEngine` | Member: `m_hybrid_strategy`<br>Member: `m_settings_provider`<br>Member: `m_initialized`<br>Member: `m_scale_buffer`<br>Member: `s_instance`<br>...and 8 more |
| `MicrotonalPitchCalculator` | Member: `m_scale_tuning`<br>Member: `m_scale_size`<br>Member: `loadScale`<br>Member: `mapToScale` |
| `MidiClock` | Member: `operator=` |
| `MidiDelayChorus` | Member: `m_settings`<br>Member: `m_settings_provider`<br>Member: `m_transport_manager`<br>Member: `m_events`<br>Member: `m_current_tick`<br>...and 22 more |
| `MidiDelayChorusAdapter` | Member: `m_module` |
| `MidiDelayChorusSettingsProvider` | Class Description<br>Member: `getMidiDelayChorusSettings` |
| `MidiGoblinInputHardware` | Member: `m_encoder_count`<br>Member: `m_last_read`<br>Member: `m_last_encoder_state`<br>Member: `ADDR_MASK`<br>Member: `SIG_MASK`<br>...and 3 more |
| `MidiInputHandlerMock` | Class Description<br>Member: `MOCK_METHOD` |
| `MidiLfo` | Class Description<br>Member: `m_waveform`<br>Member: `m_rateHz`<br>Member: `m_phase`<br>Member: `init`<br>...and 2 more |
| `MidiLfoManager` | Class Description<br>Member: `m_settings`<br>Member: `m_lfos`<br>Member: `m_ppqnCounter`<br>Member: `m_lastTickMicros`<br>...and 3 more |
| `MidiLfoManagerTest` | Class Description<br>Member: `mock_time`<br>Member: `transport_manager`<br>Member: `listener`<br>Member: `manager`<br>...and 2 more |
| `MidiLfoTest` | Class Description<br>Member: `lfo`<br>Member: `settings`<br>Member: `mock_transport`<br>Member: `mock_listener`<br>...and 1 more |
| `MidiModifier` | Member: `m_global_settings_provider`<br>Member: `m_quantizer`<br>Member: `m_settings`<br>Member: `operator=` |
| `MidiModifierAdapter` | Member: `m_midi_modifier` |
| `MidiProcessorMock` | Class Description<br>Member: `MOCK_METHOD` |
| `MockActiveChordProvider` | Class Description<br>Member: `m_active_chords`<br>Member: `MOCK_METHOD`<br>Member: `setActiveChords` |
| `MockArpeggiatorSettingsProvider` | Class Description<br>Member: `m_settings` |
| `MockAudioDriver` | Class Description<br>Member: `is_initialized`<br>Member: `is_started`<br>Member: `last_written_buffer`<br>Member: `reset` |
| `MockChordProcessorSettingsProvider` | Class Description<br>Member: `m_settings` |
| `MockDisplay` | Class Description<br>Member: `display`<br>Member: `clearDisplay`<br>Member: `drawPixel`<br>Member: `setTextColor`<br>...and 41 more |
| `MockEntropyPool` | Class Description<br>Member: `m_next_value`<br>Member: `m_next_values`<br>Member: `m_seed`<br>Member: `getRandomUint32`<br>...and 9 more |
| `MockExpanderTransport` | Class Description<br>Member: `send_message_called`<br>Member: `begin`<br>Member: `sendMessage`<br>Member: `addPeer`<br>...and 3 more |
| `MockFile` | Class Description<br>Member: `m_content`<br>Member: `m_position`<br>Member: `read`<br>Member: `write`<br>...and 5 more |
| `MockFileImpl` | Class Description<br>Member: `data`<br>Member: `position`<br>Member: `valid` |
| `MockFileSystem` | Class Description<br>Member: `files`<br>Member: `m_files`<br>Member: `m_dirs`<br>Member: `reset`<br>...and 27 more |
| `MockGlobalPatchSettingsProvider` | Class Description<br>Member: `m_settings`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD` |
| `MockLedController` | Class Description |
| `MockMIDIRouter` | Class Description<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>...and 6 more |
| `MockMidiLfoOutputListener` | Class Description<br>Member: `messages`<br>Member: `MOCK_METHOD`<br>Member: `captureMessage` |
| `MockMidiProcessor` | Class Description<br>Member: `MOCK_METHOD` |
| `MockMidiRouter` | Class Description<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>...and 32 more |
| `MockModulationOutputListener` | Class Description<br>Member: `message_count`<br>Member: `last_message`<br>Member: `last_message`<br>Member: `reset`<br>...and 3 more |
| `MockPatchDataProvider` | Class Description<br>Member: `get_patch_parameter` |
| `MockPrint` | Class Description<br>Member: `write`<br>Member: `write` |
| `MockPrintSecurity` | Class Description<br>Member: `write`<br>Member: `write` |
| `MockScaleManager` | Class Description<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>...and 9 more |
| `MockStorage` | Class Description<br>Member: `getInstance` |
| `MockTimeSource` | Class Description<br>Member: `m_millis`<br>Member: `m_timestamp`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>...and 7 more |
| `MockTransportListener` | Class Description<br>Member: `command_count`<br>Member: `last_command`<br>Member: `command_received_count`<br>Member: `lastCommand`<br>...and 2 more |
| `MockTransportManager` | Class Description<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>Member: `MOCK_METHOD`<br>...and 102 more |
| `ModalInterchangeTest` | Class Description<br>Member: `m_testable_chord_processor`<br>Member: `SetUp` |
| `ModulationDispatcher` | Member: `MAX_MODULATION_RECEIVERS`<br>Member: `m_receivers`<br>Member: `m_receiver_count`<br>Member: `operator=` |
| `ModulationMatrix` | Class Description<br>Member: `applySettings` |
| `ModulationMatrixTest` | Class Description<br>Member: `matrix`<br>Member: `listener`<br>Member: `setup`<br>Member: `SetUp` |
| `MscManager` | Member: `m_blockDevice`<br>Member: `m_ejected`<br>Member: `begin` |
| `MyCharacteristicCallbacks` | Class Description<br>Member: `_bluetoothEsp32`<br>Member: `_bluetoothEsp32`<br>Member: `onWrite`<br>Member: `onWrite` |
| `MyClientCallbacks` | Member: `_bluetoothEsp32`<br>Member: `onPassKeyRequest`<br>Member: `onConnect`<br>Member: `onDisconnect`<br>Member: `onConnParamsUpdateRequest` |
| `MyServerCallbacks` | Class Description<br>Member: `_bluetoothEsp32`<br>Member: `_bluetoothEsp32`<br>Member: `onConnect`<br>Member: `onDisconnect`<br>...and 2 more |
| `NativeDisplay` | Class Description<br>Member: `clearDisplay`<br>Member: `display`<br>Member: `drawPixel`<br>Member: `drawLine`<br>...and 16 more |
| `NativeGpio` | Class Description<br>Member: `MAX_PINS`<br>Member: `pin_states_`<br>Member: `analog_values_`<br>Member: `pin_modes_`<br>...and 3 more |
| `NativeInputHardware` | Class Description<br>Member: `MAX_ENCODERS`<br>Member: `MAX_BUTTONS`<br>Member: `encoder_deltas_`<br>Member: `button_states_`<br>...and 2 more |
| `NativeTimeSource` | Class Description<br>Member: `m_start` |
| `NativeTimeSourceStub` | Class Description |
| `NoteScheduler` | Member: `m_events`<br>Member: `process`<br>Member: `clear` |
| `OrchestrationConfigView` | Member: `s_device_index`<br>Member: `m_selected_parameter_index` |
| `OrchestrationManager` | Class Description<br>Member: `m_midi_modifier`<br>Member: `m_midi_router`<br>Member: `m_transport_manager`<br>Member: `m_mapper`<br>...and 23 more |
| `OrchestrationManagerTest` | Class Description<br>Member: `mock_router`<br>Member: `mock_transport`<br>Member: `mock_scale_manager`<br>Member: `mock_global_settings`<br>...and 5 more |
| `OrchestrationView` | Member: `m_selected_device_index` |
| `PatchCompactTask` | Class Description<br>Member: `m_task_handle`<br>Member: `m_compact_queue`<br>Member: `m_current_slot`<br>Member: `getInstance`<br>...and 6 more |
| `PatchConverter` | Member: `m_patchLoader` |
| `PatchIO` | Member: `write`<br>Member: `read`<br>Member: `writeU8`<br>Member: `writeI8`<br>Member: `writeU16`<br>...and 15 more |
| `PatchProtection` | Class Description<br>Member: `_dataLib`<br>Member: `MAX_BACKUPS`<br>Member: `FIRMWARE_VERSION`<br>Member: `MINIMUM_SUPPORTED_PATCH_VERSION`<br>...and 2 more |
| `PatchProtectionTest` | Class Description<br>Member: `mockFs`<br>Member: `dataLib`<br>Member: `patchProtection` |
| `PatchSerializer` | Class Description<br>Member: `m_global_settings_provider`<br>Member: `m_sequencer_settings_provider`<br>Member: `m_arpeggiator_settings_provider`<br>Member: `m_chord_processor_settings_provider`<br>...and 10 more |
| `PatchSlotManager` | Class Description<br>Member: `m_mutex`<br>Member: `m_sd_fs`<br>Member: `m_spiffs_fs`<br>Member: `m_active_slot`<br>...and 37 more |
| `PatternStreamer` | Member: `m_track_states`<br>Member: `m_track_states_mutex`<br>Member: `m_load_request_queue`<br>Member: `m_task_handle`<br>Member: `m_sequencer`<br>...and 8 more |
| `PitchBendStrategy` | Member: `DEFAULT_CHANNEL`<br>Member: `PITCH_BEND_RANGE_SEMITONES`<br>Member: `CENTS_PER_SEMITONE`<br>Member: `PITCH_BEND_CENTER`<br>Member: `PITCH_BEND_RANGE_CENTS`<br>...and 8 more |
| `PlayMenuView` | Class Description |
| `Prism` | Member: `m_settings`<br>Member: `m_round_robin_counter`<br>Member: `m_active_notes`<br>Member: `m_last_chord_notes`<br>Member: `m_last_chord_size`<br>...and 9 more |
| `PrismAdapter` | Member: `m_prism` |
| `PrismTest` | Class Description<br>Member: `prism`<br>Member: `setup`<br>Member: `noteOn`<br>Member: `noteOff` |
| `PrismView` | Class Description<br>Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset`<br>Member: `m_cached_settings` |
| `RFEntropyGenerator` | Class Description<br>Member: `m_is_enabled`<br>Member: `m_last_random_value`<br>Member: `getRandomUint32`<br>Member: `getRandomUint8`<br>...and 5 more |
| `RandomGeneratorAdapter` | Member: `m_generator` |
| `RandomWalk` | Member: `m_value`<br>Member: `m_min`<br>Member: `m_max`<br>Member: `getValue`<br>Member: `setValue` |
| `ResourceProfileLoader` | Class Description<br>Member: `json_string_pool`<br>Member: `_currentProfile`<br>Member: `getInstance`<br>Member: `loadProfile`<br>...and 2 more |
| `ResourceProfileLoaderTest` | Class Description<br>Member: `SetUp` |
| `RhythmDiamondEngine` | Class Description<br>Member: `MAX_GRID_SIZE`<br>Member: `_width`<br>Member: `_height`<br>Member: `_gems`<br>...and 4 more |
| `RhythmPermutationUtilTest` | Class Description<br>Member: `pattern`<br>Member: `SetUp` |
| `RssiPollingEntropySource` | Member: `m_task_handle` |
| `SDCardDataLibraryTest` | Class Description<br>Member: `dataLibrary` |
| `SDClass` | Class Description<br>Member: `open`<br>Member: `exists`<br>Member: `mkdir`<br>Member: `begin` |
| `ScalaParser` | Class Description<br>Member: `parse` |
| `ScalaParserBugTest` | Class Description<br>Member: `fs`<br>Member: `parser`<br>Member: `SetUp`<br>Member: `parseContent` |
| `ScalaParserTest` | Class Description<br>Member: `fs`<br>Member: `parser`<br>Member: `SetUp`<br>Member: `parseContent` |
| `ScalaSerializer` | Class Description<br>Member: `saveBinary`<br>Member: `loadBinary` |
| `ScaleManager` | Member: `_dist_down`<br>Member: `_dist_up`<br>Member: `getStyleCount`<br>Member: `getStyleName`<br>Member: `getScalesInStyle`<br>...and 1 more |
| `ScalePresets` | Class Description |
| `ScaleQuantizer` | Member: `m_scale_manager`<br>Member: `m_gsp`<br>Member: `isInScaleGlobal`<br>Member: `isInScaleModule`<br>Member: `getNextScaleNoteGlobal`<br>...and 1 more |
| `ScaleRunner` | Member: `MAX_ACTIVE_RUNS`<br>Member: `MAX_HELD_NOTES`<br>Member: `m_runs`<br>Member: `m_held_notes`<br>Member: `m_settings`<br>...and 11 more |
| `ScaleRunnerAdapter` | Member: `m_scale_runner` |
| `ScaleRunnerTest` | Class Description<br>Member: `runner`<br>Member: `mockQuantizer`<br>Member: `mockTransport`<br>Member: `mockRouter`<br>...and 5 more |
| `ScaleRunnerView` | Class Description<br>Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_scroll_offset`<br>Member: `m_cached_settings` |
| `ScaleStorageManager` | Class Description<br>Member: `m_fs`<br>Member: `m_builtinFile`<br>Member: `m_userFile`<br>Member: `m_totalCount`<br>...and 16 more |
| `Sequencer` | Member: `SequencerSwingLogicTest`<br>Member: `SequencerComprehensiveTest`<br>Member: `SequencerWrapAroundTest`<br>Member: `s_instance`<br>Member: `m_settings`<br>...and 17 more |
| `SequencerComprehensiveTest` | Class Description<br>Member: `sequencer`<br>Member: `setup` |
| `SequencerInversionTest` | Class Description<br>Member: `sequencer`<br>Member: `SetUp`<br>Member: `TearDown` |
| `SequencerSwingLogicTest` | Class Description<br>Member: `sequencer`<br>Member: `mockSystemModel`<br>Member: `mockRouter`<br>Member: `mockTransport`<br>...and 2 more |
| `SequencerWrapAroundTest` | Class Description<br>Member: `sequencer`<br>Member: `mockSystemModel`<br>Member: `mockRouter`<br>Member: `mockTransport`<br>...and 2 more |
| `SignalFlowSubMenuView` | Class Description<br>Member: `m_title`<br>Member: `m_items`<br>Member: `m_items_count` |
| `SimpleLFO` | Member: `Waveform`<br>Member: `m_phase`<br>Member: `m_phase_inc`<br>Member: `m_last_rand`<br>Member: `m_waveform`<br>...and 2 more |
| `SlotNameEditView` | Member: `QWERTY_ROW1`<br>Member: `QWERTY_ROW2`<br>Member: `QWERTY_ROW3`<br>Member: `QWERTY_NUMS` |
| `SmartSubstitutionEngine` | Member: `m_settings`<br>Member: `m_random_seed`<br>Member: `m_last_sub_time`<br>Member: `m_last_sub_desc`<br>Member: `getSettings` |
| `SmartSubstitutionView` | Class Description<br>Member: `FocusItem`<br>Member: `m_focus`<br>Member: `m_settings` |
| `StdRandomGenerator` | Member: `m_generator` |
| `StepRingBuffer` | Member: `buffer_`<br>Member: `head_`<br>Member: `tail_`<br>Member: `mutex_`<br>Member: `items_available_`<br>...and 5 more |
| `StorageManager` | Member: `_fs`<br>Member: `is_ready`<br>Member: `s_instance` |
| `StreamSLIPEncoder` | Member: `_stream`<br>Member: `SLIP_END`<br>Member: `SLIP_ESC`<br>Member: `SLIP_ESC_END`<br>Member: `SLIP_ESC_ESC`<br>...and 4 more |
| `StrumHumanizationTest` | Class Description<br>Member: `chord_processor` |
| `StubTimeSource` | Class Description |
| `StubTransportManager` | Class Description<br>Member: `sendCommand`<br>Member: `start`<br>Member: `stop`<br>Member: `setTempo`<br>...and 11 more |
| `SubMenuView` | Class Description<br>Member: `m_title`<br>Member: `m_items`<br>Member: `m_items_count` |
| `SyncCheckView` | Member: `ViewManager`<br>Member: `m_progress_queue`<br>Member: `m_task_handle`<br>Member: `m_progress_percent`<br>Member: `m_current_file`<br>...and 3 more |
| `SyncConfirmView` | Member: `Option`<br>Member: `m_selected_option`<br>Member: `m_pending_index`<br>Member: `getActionDescription` |
| `SyncConflictView` | Member: `Choice`<br>Member: `m_selected_choice`<br>Member: `m_pending_index`<br>Member: `setPendingIndex` |
| `SyncProgressView` | Member: `m_progress_queue`<br>Member: `m_task_handle`<br>Member: `m_progress_percent`<br>Member: `m_current_file`<br>Member: `m_current_item`<br>...and 5 more |
| `SyncRequiredView` | Member: `Action`<br>Member: `m_selected_action`<br>Member: `m_selected_file_index`<br>Member: `m_scroll_offset` |
| `SyncSettingsView` | Member: `Field`<br>Member: `m_selected_field`<br>Member: `m_editing`<br>Member: `m_local_settings`<br>Member: `m_scroll_offset`<br>...and 2 more |
| `SynthDefinitionConverter` | Class Description<br>Member: `convertFromJSON`<br>Member: `convertFromCSV` |
| `SystemIOSetupMenuView` | Class Description |
| `SystemInitializer` | Member: `m_main_controller`<br>Member: `m_midi_router`<br>Member: `m_transport_manager`<br>Member: `m_midi_output_manager`<br>Member: `m_midi_lfo_manager`<br>...and 25 more |
| `SystemLibraryMenuView` | Class Description |
| `SystemMenuView` | Class Description |
| `SystemModelMockTest` | Class Description<br>Member: `SetUp`<br>Member: `TearDown` |
| `SystemModelStub` | Class Description<br>Member: `m_global_settings`<br>Member: `m_arp_settings`<br>Member: `getChordProcessorSettings`<br>Member: `setChordProcessorSettings`<br>...and 28 more |
| `SystemModelTest` | Class Description<br>Member: `SetUp`<br>Member: `TearDown` |
| `TapTempoManager` | Member: `m_time_source`<br>Member: `m_settings`<br>Member: `m_tap_times`<br>Member: `m_tap_count`<br>Member: `m_tap_index`<br>...and 2 more |
| `TapTempoSettingsProvider` | Member: `getTapTempoSettings`<br>Member: `setTapTempoSettings` |
| `TestableChordProcessor` | Class Description<br>Member: `m_mock_global_settings_provider`<br>Member: `m_mock_chord_processor_settings_provider`<br>Member: `m_stub_transport_manager`<br>Member: `m_modulation_dispatcher`<br>...and 3 more |
| `TransportManager` | Member: `s_instance`<br>Member: `m_listeners`<br>Member: `m_listener_count`<br>Member: `m_time`<br>Member: `m_tap_tempo_manager`<br>...and 9 more |
| `UnifiedMemoryArena` | Member: `MAX_ALLOCATIONS`<br>Member: `m_allocations`<br>Member: `m_allocation_count`<br>Member: `operator=` |
| `UnifiedMemoryArenaTest` | Class Description<br>Member: `SetUp` |
| `UnifiedSmartChordGenerator` | Class Description<br>Member: `m_settings`<br>Member: `init`<br>Member: `generateChord` |
| `UnifiedSmartChordGeneratorAdapter` | Class Description<br>Member: `m_generator`<br>Member: `process` |
| `UsbDeviceTaskWrapper` | Member: `m_task_handle`<br>Member: `setTaskHandle` |
| `UsbModeManager` | Member: `preferences`<br>Member: `NVS_NAMESPACE`<br>Member: `USB_MODE_KEY`<br>Member: `operator=` |
| `VelocityCurveView` | Class Description<br>Member: `Param`<br>Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `m_shape`<br>...and 6 more |
| `ViewInitializer` | Class Description |
| `ViewManager` | Class Description<br>Member: `m_time_source`<br>Member: `m_display`<br>Member: `m_storage`<br>Member: `m_current_view`<br>...and 7 more |
| `ViewManagerTest` | Class Description<br>Member: `m_mock_display`<br>Member: `m_mock_file_system`<br>Member: `m_mock_time_source`<br>Member: `m_display_manager`<br>...and 3 more |
| `VirtualMidiMapper` | Class Description |
| `app::ConnectionManager` | Member: `transport`<br>Member: `transport_type`<br>Member: `connected`<br>Member: `schema`<br>Member: `lock`<br>...and 16 more |
| `ble_native::BleNativeTransport` | Member: `buffer`<br>Member: `client`<br>Member: `message_queue`<br>Member: `on_notify`<br>Member: `__init__`<br>...and 6 more |
| `doxygen_mcp::server::DoxygenConfig` | Member: `project_name`<br>Member: `project_number`<br>Member: `project_brief`<br>Member: `project_logo`<br>Member: `output_directory`<br>...and 31 more |
| `fs::File` | Class Description<br>Member: `write`<br>Member: `read`<br>Member: `peek`<br>Member: `available`<br>...and 11 more |
| `midikobold::CvToMidiConverter` | Member: `cv_hardware`<br>Member: `settings`<br>Member: `midi_output`<br>Member: `last_sent_value`<br>Member: `HYSTERESIS_THRESHOLD`<br>...and 2 more |
| `midikobold::IPatchDataProvider` | Class Description<br>Member: `get_patch_parameter` |
| `midikobold::MidiKoboldSuperSaw` | Member: `midi_output_`<br>Member: `time_source_`<br>Member: `detuneLUT`<br>Member: `densityLUT`<br>Member: `voices_`<br>...and 10 more |
| `midikobold::MidiToCvConverter` | Member: `cv_hardware`<br>Member: `m_settings`<br>Member: `m_note_indices`<br>Member: `m_note_count`<br>Member: `m_gate_indices`<br>...and 8 more |
| `midikobold::MockCvHardware` | Class Description<br>Member: `last_voltage`<br>Member: `last_channel`<br>Member: `cv_input` |
| `midikobold::MorphController` | Member: `slots`<br>Member: `m_morph_position_linear`<br>Member: `m_morph_position_x`<br>Member: `m_morph_position_y`<br>Member: `m_morph_position_linear_hires`<br>...and 12 more |
| `midikobold::MorphPatchSelectView` | Member: `MORPH_MAX_PATCH_FILES`<br>Member: `MORPH_MAX_FILENAME_LEN`<br>Member: `s_target_slot`<br>Member: `m_files`<br>Member: `m_file_count` |
| `midikobold::MorphSettingsView` | Member: `m_cached_settings`<br>Member: `m_selected_param`<br>Member: `m_is_editing`<br>Member: `s_pending_patch_slot` |
| `midikobold::hal::SDCardFile` | Class Description<br>Member: `_file`<br>Member: `SDCardFile`<br>Member: `write`<br>Member: `read`<br>...and 5 more |
| `midikobold::hal::SDCardFileSystem` | Class Description<br>Member: `_sd`<br>Member: `_initialized`<br>Member: `SDCardFileSystem`<br>Member: `mount`<br>...and 6 more |
| `midikobold::hal::SpiffsFile` | Member: `_file`<br>Member: `SpiffsFile`<br>Member: `read`<br>Member: `write`<br>Member: `close`<br>...and 4 more |
| `midikobold::hal::SpiffsFileSystem` | Member: `_initialized` |
| `mock_device::MockDevice` | Member: `mode`<br>Member: `port`<br>Member: `running`<br>Member: `ser`<br>Member: `__init__`<br>...and 4 more |
| `test_app::BackendTestCase` | Class Description<br>Member: `app`<br>Member: `setUp`<br>Member: `tearDown`<br>Member: `test_list_transports`<br>...and 4 more |
| `test_security_headers::TestSecurityHeaders` | Class Description<br>Member: `app`<br>Member: `setUp`<br>Member: `test_security_headers_presence` |
| `test_security_regressions::SecurityRegressionTestCase` | Class Description<br>Member: `app`<br>Member: `setUp`<br>Member: `tearDown`<br>Member: `test_path_traversal_prevention`<br>...and 1 more |
| `test_security_static::SecurityStaticAnalysisTest` | Class Description<br>Member: `test_no_insecure_origins` |
| `test_server::TestDoxygenConfig` | Member: `test_default_config`<br>Member: `test_config_serialization`<br>Member: `test_language_optimization` |
| `test_server::TestLanguageDetection` | Member: `test_cpp_language_config`<br>Member: `test_python_language_config`<br>Member: `test_c_language_config` |
| `usb_serial::UsbSerialTransport` | Member: `ser`<br>Member: `__init__`<br>Member: `send_osc`<br>Member: `disconnect`<br>Member: `receive_osc` |
| `wifi_hybrid::WifiHybridTransport` | Member: `tcp_sock`<br>Member: `udp_sock`<br>Member: `device_addr`<br>Member: `rx_buffer`<br>Member: `__init__`<br>...and 7 more |

**Summary:** Found **312** classes with missing documentation, totaling **2454** undocumented items.
