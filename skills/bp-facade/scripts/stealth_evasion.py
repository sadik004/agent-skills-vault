"""
Autonomous 10-Layer Hardened Evasion Module (Pure Python Self-Contained)
Automatically injected into any Playwright, Patchright, Selenium, or Undetected-Chromedriver session.
Zero external file dependencies.
"""
import inspect
from typing import Any

# =========================================================================
# COMPLETE 10-LAYER INLINE JAVASCRIPT PAYLOAD (Zero external file dependencies)
# =========================================================================
STEALTH_EVASION_JS = r"""/**
 * Universal Multi-Layer Evasion Payload
 * Reusable across any browser automation project (Playwright, Patchright, Puppeteer, Selenium, Undetected ChromeDriver).
 * Injected before any page script executes via CDP Page.addScriptToEvaluateOnNewDocument / page.add_init_script.
 */
(() => {
    'use strict';

    // =========================================================================
    // CORE UTILITY: Native Registry & Function Tampering Masking
    // =========================================================================
    const originalToString = Function.prototype.toString;
    const nativeRegistry = new Map();

    window.makeNative = (fn, name) => {
        Object.defineProperty(fn, 'name', {
            value: name,
            configurable: true,
            enumerable: false,
            writable: false
        });

        Object.defineProperty(fn, 'length', {
            value: 0,
            configurable: true,
            enumerable: false,
            writable: false
        });

        nativeRegistry.set(fn, `function ${name}() { [native code] }`);
        return fn;
    };

    const customToString = function() {
        if (nativeRegistry.has(this)) {
            return nativeRegistry.get(this);
        }
        if (this === Function.prototype.toString) {
            return 'function toString() { [native code] }';
        }
        return originalToString.apply(this, arguments);
    };

    nativeRegistry.set(customToString, 'function toString() { [native code] }');

    Object.defineProperty(Function.prototype, 'toString', {
        value: customToString,
        writable: true,
        configurable: true,
        enumerable: false
    });

    // =========================================================================
    // LAYER 1: Navigator Webdriver Concealment
    // =========================================================================
    try {
        const webdriverGetter = () => undefined;
        window.makeNative(webdriverGetter, 'get webdriver');

        Object.defineProperty(Navigator.prototype, 'webdriver', {
            get: webdriverGetter,
            set: undefined,
            enumerable: true,
            configurable: true
        });

        // Hardened prepareStackTrace: Clean internal CDP/Playwright callstack traces
        const originalPrepare = Error.prepareStackTrace;
        Object.defineProperty(Error, 'prepareStackTrace', {
            configurable: true,
            enumerable: false,
            get: () => {
                return window.makeNative((err, s) => {
                    const filtered = s.filter(frame => {
                        const file = frame.getFileName() || '';
                        return !file.includes('playwright') && !file.includes('CDP') && !file.includes('binding');
                    });
                    if (originalPrepare) {
                        return originalPrepare(err, filtered);
                    }
                    return err.toString() + '\n' + filtered.map(f => '    at ' + f.toString()).join('\n');
                }, 'prepareStackTrace');
            },
            set: () => {}
        });
    } catch (err) {
        // Silent catch to prevent execution stop
    }

    // =========================================================================
    // LAYER 2: Chrome Runtime Simulation
    // =========================================================================
    try {
        if (!window.chrome) {
            window.chrome = {};
        }

        // 1. window.chrome.csi()
        const csi = function() {
            const perf = window.performance;
            const timing = perf && perf.timing;
            const startE = timing ? timing.navigationStart : Date.now();
            const onloadT = timing ? timing.loadEventEnd : Date.now() + 45;
            const pageT = (onloadT - startE);

            return {
                startE: startE,
                onloadT: onloadT,
                pageT: pageT,
                tran: 15
            };
        };
        window.makeNative(csi, 'csi');

        // 2. window.chrome.loadTimes()
        const loadTimes = function() {
            const now = Date.now() / 1000;
            return {
                requestTime: now - 0.45,
                startLoadTime: now - 0.38,
                commitLoadTime: now - 0.25,
                finishDocumentLoadTime: now - 0.10,
                finishLoadTime: now,
                firstPaintTime: now - 0.18,
                firstPaintAfterLoadTime: 0,
                navigationType: 'Other',
                wasFetchedViaSpdy: true,
                wasNpnNegotiated: true,
                npnNegotiatedProtocol: 'h2',
                connectionInfo: 'h2'
            };
        };
        window.makeNative(loadTimes, 'loadTimes');

        // 3. window.chrome.runtime Extension Bridge
        const runtime = {
            connect: window.makeNative(function connect() {
                throw new TypeError("Error in invocation of runtime.connect(optional string extensionId, optional object connectInfo): chrome.runtime.connect() called from a webpage must specify an Extension ID (string) for its first parameter.");
            }, 'connect'),
            sendMessage: window.makeNative(function sendMessage() {
                throw new TypeError("Error in invocation of runtime.sendMessage(optional string extensionId, any message, optional object options, optional function responseCallback): Error at parameter 'message': Value must be specified.");
            }, 'sendMessage'),
            PlatformOs: { MAC: 'mac', WIN: 'win', ANDROID: 'android', CROS: 'cros', LINUX: 'linux', OPENBSD: 'openbsd' },
            PlatformArch: { ARM: 'arm', X86_32: 'x86-32', X86_64: 'x86-64', MIPS: 'mips' }
        };

        // Attach safely to window.chrome
        Object.defineProperty(window.chrome, 'csi', { value: csi, writable: true, configurable: true, enumerable: true });
        Object.defineProperty(window.chrome, 'loadTimes', { value: loadTimes, writable: true, configurable: true, enumerable: true });
        Object.defineProperty(window.chrome, 'runtime', { value: runtime, writable: true, configurable: true, enumerable: true });

    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 3: Permissions Query Neutralization
    // =========================================================================
    try {
        if (navigator.permissions && navigator.permissions.query) {
            const originalQuery = navigator.permissions.query;

            const neutralizedQuery = function query(parameters) {
                if (!parameters || typeof parameters !== 'object') {
                    return originalQuery.apply(this, arguments);
                }

                // When notifications or geolocation permission is checked
                if (parameters.name === 'notifications') {
                    // Standard desktop Chrome returns 'prompt' for ungranted origins
                    const mockStatus = {
                        state: (window.Notification && window.Notification.permission === 'granted') ? 'granted' : 'prompt',
                        onchange: null,
                        name: 'notifications',
                        addEventListener: window.makeNative(function addEventListener() {}, 'addEventListener'),
                        removeEventListener: window.makeNative(function removeEventListener() {}, 'removeEventListener'),
                        dispatchEvent: window.makeNative(function dispatchEvent() { return true; }, 'dispatchEvent')
                    };

                    // Inherit prototype from PermissionStatus if available
                    if (window.PermissionStatus) {
                        Object.setPrototypeOf(mockStatus, window.PermissionStatus.prototype);
                    }

                    return Promise.resolve(mockStatus);
                }

                return originalQuery.apply(this, arguments);
            };

            window.makeNative(neutralizedQuery, 'query');

            Object.defineProperty(navigator.permissions, 'query', {
                value: neutralizedQuery,
                writable: true,
                configurable: true,
                enumerable: true
            });
        }
    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 4: Canvas & WebGL Sub-Pixel Pseudo-Random Noise Injection
    // =========================================================================
    try {
        const sessionNoiseSeed = Math.floor(Math.random() * 10) + 1; // 1 to 10 session seed

        if (window.CanvasRenderingContext2D) {
            const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;

            const noiseGetImageData = function getImageData(sx, sy, sw, sh) {
                const imageData = originalGetImageData.apply(this, arguments);
                const data = imageData.data;
                const len = data.length;

                // Sub-pixel jitter: shift least significant bit on 1-2% of pixels
                for (let i = 0; i < len; i += 24) {
                    const noise = (i % 2 === 0 ? 1 : -1) * (sessionNoiseSeed % 2 === 0 ? 1 : 0);
                    // Safe clamp 0-255
                    data[i] = Math.max(0, Math.min(255, data[i] + noise));
                }
                return imageData;
            };

            window.makeNative(noiseGetImageData, 'getImageData');
            Object.defineProperty(CanvasRenderingContext2D.prototype, 'getImageData', {
                value: noiseGetImageData,
                writable: true,
                configurable: true,
                enumerable: true
            });
        }

        if (window.HTMLCanvasElement) {
            const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;

            const noiseToDataURL = function toDataURL() {
                const context = this.getContext('2d');
                if (context && this.width > 0 && this.height > 0) {
                    try {
                        const imgData = context.getImageData(0, 0, Math.min(this.width, 16), Math.min(this.height, 16));
                        // Jitter first pixel minimally
                        imgData.data[0] = Math.max(0, Math.min(255, imgData.data[0] ^ 1));
                        context.putImageData(imgData, 0, 0);
                    } catch (e) {}
                }
                return originalToDataURL.apply(this, arguments);
            };

            window.makeNative(noiseToDataURL, 'toDataURL');
            Object.defineProperty(HTMLCanvasElement.prototype, 'toDataURL', {
                value: noiseToDataURL,
                writable: true,
                configurable: true,
                enumerable: true
            });
        }
    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 5: AudioContext Micro-Frequency Noise Injection
    // =========================================================================
    try {
        const audioJitterSeed = (Math.random() * 0.0000002) - 0.0000001; // Tiny float jitter

        if (window.AudioBuffer) {
            const originalGetChannelData = AudioBuffer.prototype.getChannelData;

            const noiseGetChannelData = function getChannelData(channel) {
                const buffer = originalGetChannelData.apply(this, arguments);
                const len = buffer.length;

                // Micro-frequency modulation: inject tiny float jitter on periodic samples
                for (let i = 0; i < len; i += 50) {
                    buffer[i] += audioJitterSeed;
                }
                return buffer;
            };

            window.makeNative(noiseGetChannelData, 'getChannelData');
            Object.defineProperty(AudioBuffer.prototype, 'getChannelData', {
                value: noiseGetChannelData,
                writable: true,
                configurable: true,
                enumerable: true
            });
        }

        if (window.AnalyserNode) {
            const originalGetFloatFrequencyData = AnalyserNode.prototype.getFloatFrequencyData;

            const noiseGetFloatFrequencyData = function getFloatFrequencyData(array) {
                originalGetFloatFrequencyData.apply(this, arguments);
                for (let i = 0; i < array.length; i += 30) {
                    array[i] += audioJitterSeed * 100;
                }
            };

            window.makeNative(noiseGetFloatFrequencyData, 'getFloatFrequencyData');
            Object.defineProperty(AnalyserNode.prototype, 'getFloatFrequencyData', {
                value: noiseGetFloatFrequencyData,
                writable: true,
                configurable: true,
                enumerable: true
            });
        }
    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 6: Plugin & MimeType Array Spoofing
    // =========================================================================
    try {
        const rawPluginsData = [
            {
                name: 'PDF Viewer',
                filename: 'internal-pdf-viewer',
                description: 'Portable Document Format',
                mimeTypes: [{ type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format' }]
            },
            {
                name: 'Chrome PDF Viewer',
                filename: 'internal-pdf-viewer',
                description: 'Portable Document Format',
                mimeTypes: [{ type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format' }]
            },
            {
                name: 'Chromium PDF Viewer',
                filename: 'internal-pdf-viewer',
                description: 'Portable Document Format',
                mimeTypes: [{ type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format' }]
            },
            {
                name: 'Microsoft Edge PDF Viewer',
                filename: 'internal-pdf-viewer',
                description: 'Portable Document Format',
                mimeTypes: [{ type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format' }]
            },
            {
                name: 'WebKit built-in PDF',
                filename: 'internal-pdf-viewer',
                description: 'Portable Document Format',
                mimeTypes: [{ type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format' }]
            }
        ];

        const pluginsList = [];
        const mimeTypesList = [];

        rawPluginsData.forEach((pData, pIdx) => {
            const pluginObj = Object.create(Plugin.prototype || Object.prototype);
            Object.defineProperties(pluginObj, {
                name: { value: pData.name, enumerable: true },
                filename: { value: pData.filename, enumerable: true },
                description: { value: pData.description, enumerable: true },
                length: { value: pData.mimeTypes.length, enumerable: true }
            });

            pData.mimeTypes.forEach((mData, mIdx) => {
                const mimeObj = Object.create(MimeType.prototype || Object.prototype);
                Object.defineProperties(mimeObj, {
                    type: { value: mData.type, enumerable: true },
                    suffixes: { value: mData.suffixes, enumerable: true },
                    description: { value: mData.description, enumerable: true },
                    enabledPlugin: { value: pluginObj, enumerable: true }
                });

                pluginObj[mIdx] = mimeObj;
                pluginObj[mData.type] = mimeObj;

                mimeTypesList.push(mimeObj);
                mimeTypesList[mData.type] = mimeObj;
            });

            pluginsList.push(pluginObj);
            pluginsList[pData.name] = pluginObj;
        });

        // Wrap item & namedItem
        pluginsList.item = window.makeNative(function item(index) { return pluginsList[index] || null; }, 'item');
        pluginsList.namedItem = window.makeNative(function namedItem(name) { return pluginsList[name] || null; }, 'namedItem');
        pluginsList.refresh = window.makeNative(function refresh() {}, 'refresh');

        mimeTypesList.item = window.makeNative(function item(index) { return mimeTypesList[index] || null; }, 'item');
        mimeTypesList.namedItem = window.makeNative(function namedItem(name) { return mimeTypesList[name] || null; }, 'namedItem');

        Object.defineProperty(Navigator.prototype, 'plugins', {
            get: window.makeNative(() => pluginsList, 'get plugins'),
            enumerable: true,
            configurable: true
        });

        Object.defineProperty(Navigator.prototype, 'mimeTypes', {
            get: window.makeNative(() => mimeTypesList, 'get mimeTypes'),
            enumerable: true,
            configurable: true
        });

    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 7: Battery & Network API Spoofing
    // =========================================================================
    try {
        // 1. Battery Status API Emulation
        if (navigator.getBattery || window.BatteryManager) {
            const batteryLevel = +(0.78 + (Math.random() * 0.18)).toFixed(2); // 78% to 96%
            const isCharging = Math.random() > 0.4; // 60% probability charging

            const mockBattery = {
                charging: isCharging,
                chargingTime: isCharging ? Math.floor(1800 + Math.random() * 1200) : Infinity,
                dischargingTime: isCharging ? Infinity : Math.floor(12000 + Math.random() * 8000),
                level: batteryLevel,
                onchargingchange: null,
                onchargingtimechange: null,
                ondischargingtimechange: null,
                onlevelchange: null,
                addEventListener: window.makeNative(function addEventListener() {}, 'addEventListener'),
                removeEventListener: window.makeNative(function removeEventListener() {}, 'removeEventListener'),
                dispatchEvent: window.makeNative(function dispatchEvent() { return true; }, 'dispatchEvent')
            };

            if (window.BatteryManager) {
                Object.setPrototypeOf(mockBattery, window.BatteryManager.prototype);
            }

            const getBattery = function getBattery() {
                return Promise.resolve(mockBattery);
            };
            window.makeNative(getBattery, 'getBattery');

            Object.defineProperty(Navigator.prototype, 'getBattery', {
                value: getBattery,
                writable: true,
                configurable: true,
                enumerable: true
            });
        }

        // 2. Network Information API Emulation
        const mockConnection = {
            downlink: 10.0, // 10 Mbps broadband / LTE
            effectiveType: '4g',
            rtt: 50, // 50ms realistic round trip time
            saveData: false,
            onchange: null,
            addEventListener: window.makeNative(function addEventListener() {}, 'addEventListener'),
            removeEventListener: window.makeNative(function removeEventListener() {}, 'removeEventListener'),
            dispatchEvent: window.makeNative(function dispatchEvent() { return true; }, 'dispatchEvent')
        };

        if (window.NetworkInformation) {
            Object.setPrototypeOf(mockConnection, window.NetworkInformation.prototype);
        }

        Object.defineProperty(Navigator.prototype, 'connection', {
            get: window.makeNative(() => mockConnection, 'get connection'),
            enumerable: true,
            configurable: true
        });

    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 8: Screen & Hardware Concurrency Spoofing
    // =========================================================================
    try {
        // 1. CPU Hardware Concurrency (Standard Consumer Octa-core)
        Object.defineProperty(Navigator.prototype, 'hardwareConcurrency', {
            get: window.makeNative(() => 8, 'get hardwareConcurrency'),
            enumerable: true,
            configurable: true
        });

        // 2. RAM Memory Tier (8 GB Standard Consumer Device)
        Object.defineProperty(Navigator.prototype, 'deviceMemory', {
            get: window.makeNative(() => 8, 'get deviceMemory'),
            enumerable: true,
            configurable: true
        });

        // 3. Screen Dimensions & Desktop Geometry Alignment
        if (window.screen) {
            Object.defineProperty(Screen.prototype, 'width', {
                get: window.makeNative(() => 1920, 'get width'),
                enumerable: true,
                configurable: true
            });

            Object.defineProperty(Screen.prototype, 'height', {
                get: window.makeNative(() => 1080, 'get height'),
                enumerable: true,
                configurable: true
            });

            // Accounting for authentic OS taskbar / desktop dock reservation
            Object.defineProperty(Screen.prototype, 'availWidth', {
                get: window.makeNative(() => 1920, 'get availWidth'),
                enumerable: true,
                configurable: true
            });

            Object.defineProperty(Screen.prototype, 'availHeight', {
                get: window.makeNative(() => 1040, 'get availHeight'),
                enumerable: true,
                configurable: true
            });

            Object.defineProperty(Screen.prototype, 'colorDepth', {
                get: window.makeNative(() => 24, 'get colorDepth'),
                enumerable: true,
                configurable: true
            });

            Object.defineProperty(Screen.prototype, 'pixelDepth', {
                get: window.makeNative(() => 24, 'get pixelDepth'),
                enumerable: true,
                configurable: true
            });
        }
    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 9: DevTools Detection Shield
    // =========================================================================
    try {
        // 1. Console Profiling & Getter Trap Shield
        const originalTable = console.table;
        const originalDir = console.dir;

        const sanitizeConsoleArg = (arg) => {
            if (arg && typeof arg === 'object') {
                try {
                    const descriptors = Object.getOwnPropertyDescriptors(arg);
                    for (const key in descriptors) {
                        if (descriptors[key].get) {
                            return `[Shielded Getter: ${key}]`;
                        }
                    }
                } catch (e) {}
            }
            return arg;
        };

        const shieldedTable = function table(tabularData, properties) {
            try {
                if (Array.isArray(tabularData)) {
                    const safeData = tabularData.map(sanitizeConsoleArg);
                    return originalTable.call(this, safeData, properties);
                }
            } catch (e) {}
            return originalTable.apply(this, arguments);
        };
        window.makeNative(shieldedTable, 'table');
        console.table = shieldedTable;

        const shieldedDir = function dir(item, options) {
            try {
                return originalDir.call(this, sanitizeConsoleArg(item), options);
            } catch (e) {}
            return originalDir.apply(this, arguments);
        };
        window.makeNative(shieldedDir, 'dir');
        console.dir = shieldedDir;

        // 2. Disarm eval/Function 'debugger' Timing Traps
        const originalFunction = window.Function;
        const patchedFunction = function(...args) {
            const body = args[args.length - 1];
            if (typeof body === 'string' && body.includes('debugger')) {
                // Strip the debugger call to prevent microtask pauses and timing analysis
                args[args.length - 1] = body.replace(/debugger\s*;?/g, '/* disarmed */');
            }
            return originalFunction.apply(this, args);
        };
        patchedFunction.prototype = originalFunction.prototype;
        window.makeNative(patchedFunction, 'Function');
        window.Function = patchedFunction;

    } catch (err) {
        // Silent catch
    }

    // =========================================================================
    // LAYER 10: WebRTC Leak Prevention (STUN/TURN Candidate Sanitization)
    // =========================================================================
    try {
        if (window.RTCPeerConnection) {
            const originalCreateOffer = RTCPeerConnection.prototype.createOffer;
            const originalSetLocalDescription = RTCPeerConnection.prototype.setLocalDescription;

            // IP pattern to detect and sanitize local/host IPs
            const ipRegex = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/g;

            // 1. Sanitize SDP in createOffer
            const sanitizedCreateOffer = function createOffer(options) {
                return originalCreateOffer.apply(this, arguments).then(offer => {
                    if (offer && offer.sdp) {
                        offer.sdp = offer.sdp.replace(ipRegex, '0.0.0.0');
                    }
                    return offer;
                });
            };
            window.makeNative(sanitizedCreateOffer, 'createOffer');
            RTCPeerConnection.prototype.createOffer = sanitizedCreateOffer;

            // 2. Sanitize SDP in setLocalDescription
            const sanitizedSetLocalDescription = function setLocalDescription(desc) {
                if (desc && desc.sdp) {
                    desc.sdp = desc.sdp.replace(ipRegex, '0.0.0.0');
                }
                return originalSetLocalDescription.apply(this, arguments);
            };
            window.makeNative(sanitizedSetLocalDescription, 'setLocalDescription');
            RTCPeerConnection.prototype.setLocalDescription = sanitizedSetLocalDescription;

            // 3. Filter and sanitize ICE candidate dispatches
            const originalAddEventListener = RTCPeerConnection.prototype.addEventListener;
            const sanitizedAddEventListener = function addEventListener(type, listener, options) {
                if (type === 'icecandidate' && typeof listener === 'function') {
                    const wrappedListener = function(event) {
                        if (event && event.candidate && event.candidate.candidate) {
                            const sanitizedCandidateStr = event.candidate.candidate.replace(ipRegex, '0.0.0.0');
                            try {
                                Object.defineProperty(event.candidate, 'candidate', {
                                    value: sanitizedCandidateStr,
                                    configurable: true
                                });
                            } catch (e) {}
                        }
                        return listener.apply(this, arguments);
                    };
                    return originalAddEventListener.call(this, type, wrappedListener, options);
                }
                return originalAddEventListener.apply(this, arguments);
            };
            window.makeNative(sanitizedAddEventListener, 'addEventListener');
            RTCPeerConnection.prototype.addEventListener = sanitizedAddEventListener;
        }
    } catch (err) {
        // Silent catch
    }
})();
"""

def get_stealth_payload() -> str:
    """Returns the self-contained 10-layer evasion JavaScript payload."""
    return STEALTH_EVASION_JS

async def apply_stealth_async(page_or_context: Any) -> None:
    """
    Automatically injects all 10 stealth evasion layers into a Playwright/Patchright page or context.
    Must be called before page.goto().
    """
    if hasattr(page_or_context, 'add_init_script'):
        res = page_or_context.add_init_script(STEALTH_EVASION_JS)
        if inspect.isawaitable(res):
            await res

def apply_stealth_sync(driver_or_page: Any) -> None:
    """
    Automatically injects all 10 stealth evasion layers into Selenium, Undetected-ChromeDriver,
    or Sync Playwright.
    """
    # Selenium / UC via CDP
    if hasattr(driver_or_page, 'execute_cdp_cmd'):
        driver_or_page.execute_cdp_cmd(
            'Page.addScriptToEvaluateOnNewDocument',
            {'source': STEALTH_EVASION_JS}
        )
    # Sync Playwright
    elif hasattr(driver_or_page, 'add_init_script'):
        driver_or_page.add_init_script(STEALTH_EVASION_JS)

# Universal auto-detecting wrapper
async def auto_stealth(target: Any) -> None:
    """
    Universal one-line auto-shield:
    Usage:
        await auto_stealth(page)   # Playwright/Patchright
        auto_stealth_sync(driver)  # Selenium/UC
    """
    await apply_stealth_async(target)

def auto_stealth_sync(target: Any) -> None:
    apply_stealth_sync(target)
