![वन लाइन पायथन](../imgs/banner.png)

---

<a href="./index.md"><img src="../imgs/lang.gif" width=40% align="right"></a>

अपने कोड में अनेक पंक्तियों का उपयोग करना भूल जाइए। हर चीज़ को संक्षिप्त करें और उसे केवल एक पंक्ति में पूरा करें। ऐरे आपके सहयोगी हैं, जो आपको वे सभी कार्य करने में सक्षम बनाते हैं जो आप पहले करते थे, अब केवल एक पंक्ति में।

# परिचय
वन लाइन पायथन रिपॉजिटरी में आपका स्वागत है! यहां, हम कोड की एक पंक्ति के भीतर कार्यों को पूरा करने के लिए खुद को चुनौती देकर संक्षिप्त पायथन कोड लिखने की कला का पता लगाते हैं। इस रिपॉजिटरी का उद्देश्य विभिन्न प्रोग्रामिंग समस्याओं के रचनात्मक और कुशल समाधान प्रदर्शित करना है, जो सभी एक ही पंक्ति में संक्षिप्त हैं।

# विषयसूची

- [परिचय](#परिचय)
- [विषयसूची](#विषयसूची)
- [नियम](#नियम)
- [कोड अवधारणाएँ](#कोड-अवधारणाएँ)
  - [चर](#चर)
    - [`सूची` डेटा प्रकार का उपयोग करना।](#सूची-डेटा-प्रकार-का-उपयोग-करना)
      - [मान संशोधित करना.](#मान-संशोधित-करना)
    - [`dict` डेटा प्रकार का उपयोग करना।](#dict-डेटा-प्रकार-का-उपयोग-करना)
      - [मान संशोधित करना.](#मान-संशोधित-करना-1)
    - [वैश्विक चर को संशोधित करना।](#वैश्विक-चर-को-संशोधित-करना)
      - [मान संशोधित करना.](#मान-संशोधित-करना-2)
  - [स्थितियाँ](#स्थितियाँ)
    - [यदि कथनों का क्रम](#यदि-कथनों-का-क्रम)
  - [कार्य](#कार्य)
  - [मॉड्यूल](#मॉड्यूल)
  - [घुमाव के दौरान](#घुमाव-के-दौरान)
  - [कक्षाएं](#कक्षाएं)
- [योगदान](#योगदान)
- [लाइसेंस](#लाइसेंस)

# नियम

1. सभी कोड केवल एक पंक्ति में लिखे जाने चाहिए, जिसमें कोई भी आयातित फ़ाइल (मानक और बाहरी मॉड्यूल/पुस्तकालयों के अपवाद के साथ) शामिल है।
2. लाइन विभाजक के रूप में `;` का उपयोग न करें।
3. `exec()` का प्रयोग न करें।

नीचे, आपको एक-पंक्ति प्रारूप में लागू विभिन्न अवधारणाएँ मिलेंगी। ध्यान रखें कि ये समाधान हमेशा हर परिदृश्य के लिए सबसे कुशल या उपयुक्त नहीं हो सकते हैं। वे इन विशेष मामलों के लिए पाए गए विशिष्ट समाधान हैं।

# कोड अवधारणाएँ

## चर

मुझे वेरिएबल्स को परिभाषित करने और संशोधित करने के लिए कुछ समाधान मिले हैं:

### `सूची` डेटा प्रकार का उपयोग करना।

अनुशंसित जब आपको केवल एक वैरिएबल का उपयोग करने की आवश्यकता होती है।

**वाक्य - विन्यास**
```py
[... for variable in [value]]
```

आप अधिक मान जोड़ने का प्रयास कर सकते हैं, लेकिन आमतौर पर इसकी अनुशंसा नहीं की जाती है।

#### मान संशोधित करना.

वैरिएबल मान को संशोधित करने के लिए मुझे जो समाधान मिला वह अपरंपरागत लेकिन कार्यात्मक है:

**वाक्य - विन्यास**
```py
[variable.replace(variable, new_value) for variable in [value]]
```

### `dict` डेटा प्रकार का उपयोग करना।

बढ़िया जब आपको एकाधिक वेरिएबल्स का उपयोग करने की आवश्यकता हो।

**वाक्य - विन्यास**
```py
[... for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

#### मान संशोधित करना.

परिवर्तनीय मानों को बदलने के लिए `.update` विधि का उपयोग करें।

**वाक्य - विन्यास**
```py
[variables.update({'variable_A': 'new value'}) for variables in [{'variable_A': 'value', 'variable_B': 'value', ...}]]
```

### वैश्विक चर को संशोधित करना।

पिछली विधि के समान, हम अपने स्वयं के वेरिएबल जोड़ने के लिए वैश्विक वेरिएबल्स को अपडेट कर सकते हैं। यह विधि अधिक दिलचस्प है क्योंकि यह हमें वेरिएबल का उपयोग करने की अनुमति देती है जैसे कि इसे पारंपरिक रूप से परिभाषित किया गया हो।

**वाक्य - विन्यास**
```py
[globals().update({'variable':'value'})]
```

#### मान संशोधित करना.

चूँकि हम अपने वेरिएबल के मान को बदलने के लिए `=` का उपयोग नहीं कर सकते हैं, हम `dict` वेरिएबल को संशोधित करने के लिए प्रस्तुत उसी विधि का उपयोग कर सकते हैं।

**वाक्य - विन्यास**
```py
[globals().update({'variable':'new_value'})]
```

## स्थितियाँ

यदि आप पहले से ही सरणियों के भीतर `if-else` कथनों का उपयोग करने के आदी हैं तो इस विषय को छोड़ा जा सकता है क्योंकि कार्यान्वयन में कोई महत्वपूर्ण परिवर्तन नहीं हुए हैं।

किसी अन्य की आवश्यकता के बिना एक स्टैंडअलोन `if` स्टेटमेंट को `for` स्टेटमेंट के बाद जोड़ा जा सकता है:

**वाक्य - विन्यास**
```py
[for variable in [value] if condition]
```

यदि `अन्य` कथन की आवश्यकता है, तो आप `for` कथन से पहले शर्त जोड़ सकते हैं:

**वाक्य - विन्यास**
```py
[... if condition else ... for variable in [value] ]
```

यदि `elif` कथन की आवश्यकता है, तो आप `else` अनुभाग के भीतर अतिरिक्त `if` कथन जोड़ सकते हैं:

**वाक्य - विन्यास**
```py
[... if condition else (... if condition else ...)  for variable in [value] ]
```

> कोष्ठक वैकल्पिक हैं; उन्हें बेहतर विज़ुअलाइज़ेशन के लिए जोड़ा गया था।

### यदि कथनों का क्रम

विभिन्न उद्देश्यों वाले विभिन्न परिदृश्य हैं। ऐसे परिदृश्य में जहां आपको `if` कथनों के अनुक्रम की आवश्यकता है जो `else` का उपयोग किए बिना अलग-अलग मान लौटाते हैं, आप `else` स्थिति को `None` के रूप में प्रस्तुत कर सकते हैं:

**वाक्य - विन्यास**
```py
[[... if condition else None, ... if condition else None] for variable in [value] ]
```

इस दृष्टिकोण का उपयोग करने में समस्या यह है कि `कोई नहीं` मान सरणी में मौजूद हैं। यदि यह समस्याग्रस्त है, तो आप इन 'कोई नहीं' मानों को हटाने के लिए 'सूची' के साथ 'फ़िल्टर' का उपयोग कर सकते हैं:

**वाक्य - विन्यास**
```py
[list(filter(lambda condition_result: condition_result != None, [... if condition else None, ... if condition else None])) for variable in [value] ]
```

**उदाहरण**

```py
[list(filter(lambda condition_result: condition_result != None, ['Greater than 10' if number > 10 else None, 'Greater than 20' if number > 20 else None])) for number in [11]]
```

**के बराबर**
```py
number = 40
if number > 10: print('Greater than 10')
if number > 20: print('Greater than 20')
```

## कार्य

एक-पंक्ति फ़ंक्शंस का समाधान `लैम्ब्डा` का उपयोग करना है। `रिटर्न` का उपयोग करने की कोई आवश्यकता नहीं है। वेरिएबल्स को परिभाषित करने की सभी विधियाँ यहाँ लागू की जा सकती हैं।

**वाक्यविन्यास** *(सूची)*
```py
[function() for function in [lambda parameter: ...]]
```
**वाक्यविन्यास** *(तानाशाही)*
```py
[variables['function']() for variables in [{'function': lambda parameter: ...}]]
```
**सिंटेक्स** *(वैश्विक)*
```py
[globals().update({'function': lambda parameter: ...})]
```

**उदाहरण**

```py
[[odd(number) for number in [2,11,5]] for odd in [lambda number: "Is even" if number % 2 == 0 else "Is odd"]]
```

**के बराबर**
```py
def odd(number):
    if number % 2 == 0: return "Is even"
    return "Is odd"

odd(2) # Is even
odd(11) # Is odd
odd(5) # Is odd
```

## मॉड्यूल

मॉड्यूल आयात करने के लिए, हम `__आयात__` फ़ंक्शन को परिभाषित करने और उपयोग करने के लिए समान अवधारणाओं का उपयोग कर सकते हैं। इस तरह, हम मॉड्यूल को पूरी तरह से आयात कर सकते हैं:

**वाक्य - विन्यास**
```py
[... for module in [__import__('module_name')]]
```

**उदाहरण**

```py
[os.listdir('./') for os in [__import__('os')]]
```

**के बराबर**

```py
import os
os.listdir('./')
```

## घुमाव के दौरान

`जबकि` लूप बनाने के लिए, हमें रिकर्सन का उपयोग करने की आवश्यकता है:

**वाक्य - विन्यास**
```py
[while_loop(while_loop) for while_loop in [lambda cycle: [..., cycle(cycle) if condition else None][1]]]
```

**उदाहरण**

```py
[globals().update({'i':0}), [while_loop(while_loop) for while_loop in [lambda cycle: [[print(i), globals().update({'i':i+1})], cycle(cycle) if i <= 5 else None][1]]]]
```

**के बराबर**

```py
i = 0
while i <= 5:
    print(i)
    i += 1
```

यहाँ एक और उदाहरण है:

**उदाहरण**

```py
[[while_loop(while_loop) for while_loop in [lambda cycle: [[print(odd(number)) for number in [int(input('Number: '))]], cycle(cycle)][1]]] for odd in [lambda number: "Is odd" if number % 2 == 0 else "Is even"]]
```

**के बराबर**
```py
def odd(number):
    if number % 2 == 0: return "Is even"
    return "Is odd"

while True:
    number = int(input("Number: "))
    print(odd(number))
```

## कक्षाएं

`क्लास` बनाने के लिए मैंने जो दृष्टिकोण सोचा वह `लैम्ब्डा` और `सिंपलनेमस्पेस` का उपयोग करना है:

**वाक्य - विन्यास**
```py
[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'class_name': lambda parameters: [<init code>, SimpleNamespace(**{'method': lambda parameters: ...})][1]})]
```

**उदाहरण**
```py
[globals().update({'SimpleNamespace': __import__('types').SimpleNamespace}), globals().update({'Cat': lambda name: [print(f"Your cat's name is {name}."), SimpleNamespace(**{'meow': lambda: print(f'{name}: Meow!')})][1]}), Cat('Tom').meow()]
```

**के बराबर**
```py
class Cat:
     def __init__(self, name) -> None:
         self.name = name
         print(f"Your cat's name is {self.name}.")
    
     def meow(self) -> None:
         print(f'{self.name}: Meow!')

Cat('Tom').meow()
```

# योगदान

वन लाइन पायथन रिपॉजिटरी में योगदान की अत्यधिक सराहना की जाती है! यदि आपके पास साझा करने के लिए कोई रचनात्मक वन-लाइनर समाधान है या आप मौजूदा कोड में सुधार करना चाहते हैं, तो कृपया इन चरणों का पालन करें:

1. रिपॉजिटरी को फोर्क करें।
2. अपनी सुविधा या बग फिक्स के लिए एक नई शाखा बनाएं।
3. स्पष्ट और संक्षिप्त संदेशों के साथ अपने परिवर्तन करें।
4. अपने परिवर्तनों को अपने फोर्कड रिपॉजिटरी में पुश करें।
5. अपने परिवर्तनों का विस्तार से वर्णन करते हुए एक पुल अनुरोध सबमिट करें।

# लाइसेंस
वन लाइन पायथन रिपॉजिटरी को एमआईटी लाइसेंस के तहत लाइसेंस प्राप्त है।
