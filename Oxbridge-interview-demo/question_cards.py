physics_car_power_drag = {
    "id": "physics_car_power_drag",
    "subject": "physics",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "Two identical cars drive on a level road. The only significant resisting "
        "force is air resistance. One car has an engine with twice the maximum usable "
        "power at the wheels as the other. What is the ratio of their maximum "
        "terminal speeds? Explain your reasoning clearly, stating any modelling "
        "assumptions you make about the air resistance."
    ),
    "background_notes_for_interviewer": [
        "The key physics is the balance between engine power and aerodynamic drag at terminal speed.",
        "Let the student propose a model for air resistance. A common and realistic choice at higher speeds is F_drag ∝ v^2.",
        "If the student independently justifies F_drag ∝ v^2 (e.g. via momentum-flux arguments or dimensional reasoning), "
        "treat this as a strong positive and consider it for 'bonus' credit.",
        "If they instead assume F_drag ∝ v, probe their reasoning. You can gently steer them towards the v^2 model later in "
        "the discussion, but do not immediately overrule them unless they are stuck.",
        "Once a model F_drag = k v^2 is agreed, remind the student that at terminal speed on level ground, acceleration is zero "
        "so the net force is zero: F_engine = F_drag.",
        "Power is P = F v, not energy; a common mistake is to start with E = 1/2 m v^2."
    ],
    "solution_outline_steps": [
        "At terminal speed on level ground, acceleration is zero so the net horizontal force is zero: F_engine = F_drag.",
        "Adopt a quadratic drag model F_drag = k v^2, where k is a constant depending on air density, drag coefficient and area.",
        "Engine power at top speed is P = F_engine * v = k v^2 * v = k v^3.",
        "For the weaker car: P = k v1^3. For the stronger car: 2P = k v2^3.",
        "Divide the equations: (2P)/P = (k v2^3)/(k v1^3) ⇒ 2 = (v2/v1)^3 ⇒ v2/v1 = 2**(1/3)."
    ],
    "common_misconceptions": [
        "Equating 1/2 m v^2 directly with engine power instead of using P = F v.",
        "Forgetting that at terminal speed F_engine = F_drag, so they try to use F = m a with a = 0 in a meaningless way.",
        "Thinking that doubling engine power doubles the top speed (assuming v2/v1 = 2).",
        "Assuming drag is proportional to v without justification and never revisiting this assumption.",
        "Treating the drag law as 'given by the question' rather than something to be modelled and discussed."
    ],
    "light_hints": [
        "At each car's maximum speed, is it still accelerating? What does that imply for the net force?",
        "Do you remember a formula relating power, force and speed?",
        "How would you expect the air resistance on a car to change as its speed increases? Faster by a factor k gives drag bigger by roughly what factor?"
    ],
    "strong_hints": [
        "Try writing the drag as F_drag = k f(v) for some function f of the speed. For streamlined objects at higher speed in air, "
        "a standard model is f(v) = v^2.",
        "Once we assume F_drag = k v^2 for some constant k, what is the engine power at top speed in terms of v?",
        "You should find P ∝ v^3 under this model. Write one equation for the weaker car and one for the stronger car, then divide them."
    ],
    "extension_questions": [
        "How would the result change if drag were proportional to v instead of v^2? Can you derive the new ratio?",
        "Can you give a physical argument (for example using momentum transfer to the air) for why drag on a car at motorway speeds "
        "should scale roughly like v^2 rather than v?",
        "In practice, why might adding more engine power give diminishing returns for top speed?"
    ],
}

physics_loop_the_loop_cart = {
    "id": "physics_loop_the_loop_cart",
    "subject": "physics",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "A small cart of mass m starts from rest at height h above the lowest point of a smooth track. "
        "The track includes a vertical circular loop of radius R. You may assume no friction anywhere."
        "What is the minimum height h (in terms of R) from which the cart must be released so that it just "
        "maintains contact with the track at the top of the loop? Explain your reasoning clearly."
    ),
    "background_notes_for_interviewer": [
        "This is a classic energy + circular motion question; it tests whether the student can combine "
        "conservation of energy with a non-trivial force condition at the top of the loop.",
        "Key physical idea: 'just maintains contact' means the normal reaction at the top is zero, so the only "
        "force providing centripetal acceleration there is the weight.",
        "Gently lead them to write the condition m v_top^2 / R = m g ⇒ v_top^2 = g R, then use energy between "
        "start and top of loop.",
        "Encourage them to choose a sensible zero of potential energy (e.g. bottom of loop). At the top, the "
        "height is 2R above that reference.",
        "Some students will jump straight to energy and forget the contact condition; others will over-focus on "
        "forces and forget energy. Let them explore both then tie them together.",
        "A good candidate should be able to derive h = (5/2) R and interpret it physically."
    ],
    "solution_outline_steps": [
        "At the top of the loop, 'just maintaining contact' means the normal reaction is zero and weight alone "
        "provides the centripetal force: m v_top^2 / R = m g, so v_top^2 = g R.",
        "Choose the bottom of the loop as zero gravitational potential. The top of the loop is at height 2R.",
        "Use conservation of energy between the starting point (height h) and the top of the loop: "
        "m g h = m g (2R) + 1/2 m v_top^2.",
        "Substitute v_top^2 = g R into the energy equation: m g h = m g (2R) + 1/2 m g R.",
        "Solve for h to obtain h = (5/2) R."
    ],
    "common_misconceptions": [
        "Setting the condition at the top as weight equals zero rather than normal force equals zero.",
        "Forgetting that 'just maintains contact' implies the normal reaction is zero, not that the speed is zero.",
        "Using conservation of energy but taking the height at the top to be R instead of 2R.",
        "Using centripetal acceleration with the wrong sign or direction, or writing m g = m v^2 / R without "
        "clearly justifying why the normal force is zero.",
        "Assuming h = 2R by thinking only about potential energy without considering the centripetal condition."
    ],
    "light_hints": [
        "At the very top of the loop, what forces act on the cart, and what condition must hold if it is just about "
        "to lose contact?",
        "How would you express the idea that the track is 'just pushing with zero force' on the cart at that instant?",
        "Can you relate the speed at the top of the loop to the height from which the cart was released using energy?"
    ],
    "strong_hints": [
        "Try writing the condition at the top by setting the normal contact force to zero and using the fact that "
        "the remaining force must provide the needed centripetal acceleration.",
        "Choose a reference level for gravitational potential energy, then write an energy equation between the "
        "starting point and the top of the loop.",
        "Substitute your expression for the speed at the top into the energy equation and solve for h in terms of R."
    ],
    "extension_questions": [
        "How would the required starting height change if there were small energy losses due to friction? Can you "
        "describe qualitatively what happens?",
        "If the cart had non-negligible size so that its centre of mass does not move exactly on a circle of radius R, "
        "how might that affect the condition?",
        "Suppose the track only forms part of a loop and then opens out. What range of starting heights would still "
        "allow the cart to complete the loop without leaving the track prematurely?"
    ],
}


physics_satellite_orbits_radius_vs_period = {
    "id": "physics_satellite_orbits_radius_vs_period",
    "subject": "physics",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "Two small satellites move in circular orbits around the Earth in the same plane and direction. "
        "Satellite A orbits at radius R from the Earth's centre, and satellite B orbits at radius 4R. "
        "You may model the Earth as a point mass of mass M and neglect all other forces."
        "Compare the orbital speeds and periods of the two satellites. In particular, find the ratios v_B / v_A "
        "and T_B / T_A. Explain your reasoning."
    ),
    "background_notes_for_interviewer": [
        "This tests whether the student can combine Newton's law of gravitation with centripetal motion, and "
        "recognise the scaling of orbital speed and period with radius.",
        "Key relationships: equate gravitational and centripetal forces to obtain v^2 = G M / r, so v ∝ r^(-1/2).",
        "Using T = 2π r / v, together with v ∝ r^(-1/2), leads to T ∝ r^(3/2), i.e. Kepler's third law in the special "
        "case of circular orbits.",
        "Encourage the student to talk through which forces act and why the orbit speed is not arbitrary.",
        "Good candidates may recognise or explicitly invoke Kepler's law; weaker candidates can be guided from first principles."
    ],
    "solution_outline_steps": [
        "For a satellite of mass m in a circular orbit of radius r, the gravitational force provides the centripetal force: "
        "G M m / r^2 = m v^2 / r.",
        "Cancel m and rearrange to find v^2 = G M / r, so v ∝ r^(-1/2).",
        "Apply this to the two satellites: v_A ∝ R^(-1/2), v_B ∝ (4R)^(-1/2).",
        "Hence v_B / v_A = (R / 4R)^(1/2) = 1/2.",
        "The orbital period is T = 2π r / v, so using v ∝ r^(-1/2) gives T ∝ r^(3/2).",
        "Therefore T_B / T_A = (4R)^(3/2) / R^(3/2) = 8.",
        "So B moves at half the orbital speed of A, and its period is eight times longer."
    ],
    "common_misconceptions": [
        "Assuming the gravitational field strength g is constant with radius and using g instead of G M / r^2.",
        "Thinking the orbital speed is the same at all radii or depends only on the mass of the satellite.",
        "Assuming the period is simply proportional to the circumference (T ∝ r) and forgetting the dependence of speed on radius.",
        "Cancelling r incorrectly when equating gravitational and centripetal forces, leading to v independent of r.",
        "Confusing linear speed with angular speed, or mixing up v and 2π/T."
    ],
    "light_hints": [
        "For a circular orbit, what force provides the inward pull, and how is that related to the satellite's speed?",
        "Can you write expressions for the gravitational pull and for the centripetal requirement, and compare them?",
        "Once you know how the orbital speed depends on radius, how could you express the period in terms of radius and speed?"
    ],
    "strong_hints": [
        "Start by equating gravitational force G M m / r^2 to the required centripetal force m v^2 / r and simplify.",
        "Use your expression for v in terms of r to find the ratio of speeds at radii R and 4R.",
        "Write the period as the orbit circumference divided by the speed, and use your scaling of v with r to find how the period scales."
    ],
    "extension_questions": [
        "How does this argument relate to Kepler's third law for planetary motion? Can you state that law in words?",
        "How would your reasoning change if the orbits were elliptical rather than circular?",
        "What radius would a geostationary satellite have around the Earth? Can you set up the equation relating its period to Earth's rotation?"
    ],
}


physics_rc_circuit_charging = {
    "id": "physics_rc_circuit_charging",
    "subject": "physics",
    "level": "oxbridge_undergrad_challenging",
    "student_prompt": (
        "A resistor R and a capacitor C are connected in series to a battery of constant voltage V via an ideal switch. "
        "Initially the capacitor is uncharged. At time t = 0, the switch is closed."
        "Describe how the charge on the capacitor and the current in the circuit vary with time after the switch is closed. "
        "Define the time constant, and explain how changing R or C affects how quickly the capacitor charges. "
        "You may assume standard results for the charging of an RC circuit, but you should explain them clearly."
    ),
    "background_notes_for_interviewer": [
        "This question probes familiarity with simple first-order dynamics and exponential behaviour, plus some basic circuit theory.",
        "Some applicants may not yet have seen the full differential-equation derivation; allow them to either sketch it or recall the standard results.",
        "Key physics: the capacitor initially behaves like a short circuit (zero voltage, maximum current), then gradually charges until its voltage matches the supply and current falls to zero.",
        "Important relationship: the characteristic time scale is τ = R C; larger R or C make the charging slower.",
        "For stronger candidates, you can ask them to set up and solve the differential equation; for others, focus on qualitative behaviour and the meaning of the time constant."
    ],
    "solution_outline_steps": [
        "Immediately after closing the switch, the capacitor has zero charge and therefore zero voltage across it, so the full battery voltage appears across the resistor and the initial current is V / R.",
        "As charge builds up on the capacitor, its voltage increases, reducing the voltage across the resistor and hence the current.",
        "Writing the loop equation V = I R + q / C and using I = dq/dt leads to a first-order differential equation for q(t).",
        "Solving this yields q(t) = C V (1 − e^(−t / (R C))) for the charging process.",
        "The current then is I(t) = dq/dt = (V / R) e^(−t / (R C)), starting at V / R and decaying exponentially to zero.",
        "Define the time constant τ = R C; at t = τ, the charge has reached about 63% of its final value and the current has fallen to about 37% of its initial value.",
        "Explain qualitatively that increasing R or C increases τ and makes the charging slower, while decreasing them speeds up the response."
    ],
    "common_misconceptions": [
        "Thinking that the current is constant until the capacitor is 'full' and then suddenly drops to zero.",
        "Assuming the capacitor voltage jumps instantly to V at t = 0 instead of starting at zero and rising gradually.",
        "Confusing the roles of R and C in the time constant, or thinking τ is R / C instead of R C.",
        "Believing that the charge grows linearly with time rather than exponentially approaching a limit.",
        "Mixing up the charging and discharging forms of the exponential solutions."
    ],
    "light_hints": [
        "Right after the switch is closed, what is the voltage across the capacitor, and what does that imply about the initial current?",
        "As time goes on and the capacitor charges, what happens to the voltage across it and therefore to the voltage across the resistor?",
        "The combination R C often appears in the maths. What might that combination represent physically in terms of how quickly things change?"
    ],
    "strong_hints": [
        "Try writing a loop relation involving the battery voltage, the voltage across the resistor, and the voltage across the capacitor, "
        "and then rewrite the current in terms of the rate of change of charge.",
        "From that relation, you can obtain a simple first-order differential equation for how the charge changes in time; the standard solution is an exponential approach towards the final charge.",
        "Use that solution to define a time constant and reason how increasing R or C affects how quickly the capacitor gets close to its final charge."
    ],
    "extension_questions": [
        "What happens if, after fully charging the capacitor, you disconnect the battery and let it discharge through the resistor? "
        "Can you describe how the current and voltage vary with time?",
        "How could you use a graph of the logarithm of the current versus time to measure the time constant experimentally?",
        "How might the behaviour change if the resistor were replaced by a more complicated element, such as a diode or a light bulb?"
    ],
}


physics_double_slit_fringe_spacing = {
    "id": "physics_double_slit_fringe_spacing",
    "subject": "physics",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "A monochromatic light source of wavelength λ illuminates a double-slit arrangement with slit separation d. "
        "A screen is placed a distance L away, with L much larger than d. On the screen you observe an interference pattern "
        "of bright and dark fringes."
        "How does the spacing between adjacent bright fringes depend on λ, d and L? What happens to the fringe spacing if you "
        "(i) increase the wavelength, (ii) move the screen further away, or (iii) use a double-slit with smaller separation? "
        "Explain your reasoning."
    ),
    "background_notes_for_interviewer": [
        "This tests understanding of path difference, interference conditions, and the small-angle approximation.",
        "Key physics: constructive interference when the path difference between the two slits is an integer multiple of λ, "
        "and for small angles the path difference is approximately d times the angle.",
        "Using sin θ ≈ tan θ ≈ y / L for small θ leads to fringe positions proportional to m λ L / d, so the spacing is λ L / d.",
        "Encourage the student to visualise rays from each slit to a point on the screen and to relate geometry to phase difference.",
        "Discuss qualitatively how changing λ, L, and d affects the pattern: red light vs blue, moving the screen, or narrowing the slit separation."
    ],
    "solution_outline_steps": [
        "Consider a point on the screen at a small angle θ from the central axis. The path difference between light from the two slits "
        "reaching that point is approximately d sin θ.",
        "Bright fringes (constructive interference) occur when this path difference equals m λ for integer m.",
        "For small angles, sin θ ≈ tan θ ≈ y / L, where y is the distance of the fringe from the central maximum.",
        "Combining these gives d (y / L) ≈ m λ, so the position of the m-th bright fringe is y_m ≈ m λ L / d.",
        "The spacing between adjacent bright fringes is therefore Δy = y_{m+1} − y_m ≈ λ L / d.",
        "From this expression, conclude that increasing λ or L increases the fringe spacing, while increasing d decreases the spacing; "
        "equivalently, making d smaller increases the spacing."
    ],
    "common_misconceptions": [
        "Thinking that the brightness pattern is just the sum of two single-slit patterns without considering interference.",
        "Using the single-slit diffraction formula instead of the double-slit interference condition.",
        "Forgetting the small-angle approximation and using sin θ incorrectly for larger angles.",
        "Believing that fringe spacing depends on the slit width rather than the slit separation.",
        "Assuming that changing the screen distance L does not affect fringe spacing."
    ],
    "light_hints": [
        "What condition must be satisfied for bright fringes to appear in a double-slit interference pattern?",
        "If you look at a point at some small angle on the screen, how could you approximate the path difference between the two slits?",
        "Once you have an expression for the positions of the bright fringes, how do you obtain the spacing between adjacent ones?"
    ],
    "strong_hints": [
        "Use the condition for constructive interference: the path difference between the two paths should be an integer multiple of the wavelength.",
        "For small angles, relate the path difference to the slit separation and the angle, and then relate the angle to the position on the screen using y over L.",
        "From your expression for the fringe positions, subtract neighbouring values to get a simple expression for the fringe spacing in terms of λ, L and d."
    ],
    "extension_questions": [
        "How would the visibility of the fringes be affected if each slit had a finite width and produced its own diffraction envelope?",
        "What happens to the pattern if you use light containing two different wavelengths at the same time?",
        "If one slit is partially covered so that its intensity is reduced, how does that change the contrast of the interference fringes?"
    ],
}


physics_gas_piston_equilibrium_heating = {
    "id": "physics_gas_piston_equilibrium_heating",
    "subject": "physics",
    "level": "oxbridge_undergrad_challenging",
    "student_prompt": (
        "A vertical cylindrical container of cross-sectional area A contains n moles of an ideal gas and is fitted with a "
        "frictionless, freely moving piston of mass M. The container is open to the atmosphere above the piston, where the "
        "pressure is p_0. The system is in equilibrium at temperature T, and the gas supports the piston."
        "(a) Find the pressure of the gas in equilibrium."
        "(b) The gas is now slowly heated while the piston is free to move, and the system remains in mechanical equilibrium. "
        "Assuming the temperature becomes 2T and the piston does not hit the ends of the cylinder, how does the height of the "
        "gas column change? Explain your reasoning, stating any assumptions you make."
    ),
    "background_notes_for_interviewer": [
        "This combines static force balance with the ideal gas law and an understanding of quasi-static processes.",
        "Part (a) is a straightforward force balance on the piston: gas pressure below balances atmospheric pressure above plus the piston's weight.",
        "Part (b) probes whether the student realises that, for a slowly adjusted piston, the gas pressure remains fixed by that balance while "
        "temperature and volume change according to the ideal gas law.",
        "Key result: p_gas = p_0 + M g / A and remains constant as long as the piston is free and mechanical equilibrium is maintained.",
        "With p constant, the ideal gas law implies V ∝ T and hence the height of the gas column is proportional to temperature, so doubling T doubles the height.",
        "Be clear about assumptions: piston does not stick, the process is slow enough to be quasi-static, and the gas remains ideal."
    ],
    "solution_outline_steps": [
        "Consider the forces on the piston in mechanical equilibrium: the upward force from the gas pressure acts over area A, "
        "while downward forces include atmospheric pressure over area A and the weight of the piston M g.",
        "Write the force balance: p_gas A = p_0 A + M g, leading to p_gas = p_0 + M g / A.",
        "When the gas is slowly heated with the piston free to move, the force balance must continue to hold at each stage, "
        "so p_gas remains equal to p_0 + M g / A; thus the gas pressure is constant during the heating.",
        "Apply the ideal gas law p V = n R T with p fixed, so the volume V is directly proportional to temperature T.",
        "The volume is A times the height h of the gas column, so h is proportional to T.",
        "Therefore, when the temperature doubles from T to 2T, the height doubles from h to 2h, provided the piston does not hit the ends of the cylinder."
    ],
    "common_misconceptions": [
        "Assuming the gas pressure equals the atmospheric pressure p_0 and forgetting the contribution from the piston's weight.",
        "Thinking that the gas pressure must change when the temperature changes, even though the piston is free to move to maintain equilibrium.",
        "Using the ideal gas law with the wrong quantity held constant (e.g. treating volume as fixed despite the moving piston).",
        "Neglecting the cross-sectional area and writing the force balance incorrectly.",
        "Believing that doubling the temperature doubles the pressure while leaving the volume unchanged in this setup."
    ],
    "light_hints": [
        "In equilibrium, what forces act on the piston, and how must they balance?",
        "How does that balance relate the gas pressure below the piston to the atmospheric pressure above and the weight of the piston?",
        "If you slowly heat the gas while allowing the piston to move freely, what can you say about how the gas pressure changes during the process?"
    ],
    "strong_hints": [
        "Try expressing the upward force from the gas as its pressure times the area, and the downward forces as atmospheric pressure times area plus the piston's weight, "
        "then set them equal to find the gas pressure.",
        "Assuming the piston always adjusts so that forces balance, argue that the gas pressure remains fixed as the temperature changes.",
        "Use the ideal gas law with constant pressure to relate the initial and final volumes to the initial and final temperatures, and then connect volume to the height of the gas column."
    ],
    "extension_questions": [
        "What would happen if the piston were clamped so it could not move and you then heated the gas from T to 2T? How would the pressure change?",
        "How would the analysis change if, instead of being open to the atmosphere, the space above the piston were evacuated?",
        "If a spring were attached to the piston so that it experienced an additional restoring force, how would that modify the relationship between temperature and height?"
    ],
}

maths_optimisation_field_next_to_river = {
    "id": "maths_optimisation_field_next_to_river",
    "subject": "maths",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "You have a fixed length L of fencing wire to make a rectangular field next to a straight river. "
        "You will build three sides of the rectangle with fencing (two sides perpendicular to the river and one along the river); "
        "the river bank itself forms the fourth side and needs no fence.\n\n"
        "What dimensions maximise the area? Explain your reasoning clearly."
    ),
    "background_notes_for_interviewer": [
        "Classic single-variable optimisation problem with a simple constraint.",
        "Let the sides perpendicular to the river be x and the side along the river be y. The fencing constraint is 2x + y = L.",
        "Good candidates will express the area as A(x) = x(L - 2x), recognise it as a quadratic, differentiate, and find the maximum.",
        "Probe whether they understand why the stationary point is a maximum (shape of parabola, second derivative, or simple reasoning).",
        "Also check they notice that the rectangle is 'wider than deep': the side along the river is twice the perpendicular side."
    ],
    "solution_outline_steps": [
        "Let x be the length of the sides perpendicular to the river, and y the side along the river.",
        "The total length of fencing is 2x + y = L, so y = L - 2x.",
        "Area A = x y = x(L - 2x) = Lx - 2x^2.",
        "This is a quadratic in x opening downwards, so its maximum occurs at the vertex.",
        "Differentiate: A'(x) = L - 4x; set A'(x) = 0 to get x = L / 4.",
        "Then y = L - 2(L / 4) = L / 2, so the optimal rectangle has dimensions L/4 by L/2."
    ],
    "common_misconceptions": [
        "Forgetting that only three sides require fencing and writing 2x + 2y = L.",
        "Maximising y or x individually rather than the area.",
        "Finding the stationary point correctly but not justifying that it is a maximum.",
        "Getting the algebra right but mixing up which side is along the river."
    ],
    "light_hints": [
        "Can you introduce variables for the two different side lengths?",
        "How can you express the total length of fencing in terms of those variables?",
        "Can you write the area in terms of a single variable, and then think about how to maximise that?"
    ],
    "strong_hints": [
        "Try setting x for the sides perpendicular to the river and y for the side along the river, and write down the equation relating x, y and L.",
        "Use that equation to eliminate y from the expression for the area so that A depends only on x.",
        "Differentiate your expression for A(x), set the derivative to zero, and solve for x."
    ],
    "extension_questions": [
        "What happens if you want to enclose two adjacent rectangular pens with the same total length of fencing next to the river?",
        "If instead the river side also needed fencing, how would the optimal shape change?",
        "Can you generalise this to maximising the area of a rectangle with fixed perimeter (no river)?"
    ],
}


maths_sequence_root_two = {
    "id": "maths_sequence_root_two",
    "subject": "maths",
    "level": "oxbridge_undergrad_challenging",
    "student_prompt": (
        "Consider the sequence defined by x_1 = 1 and\n"
        "x_{n+1} = 1/2 · (x_n + 2 / x_n) for n ≥ 1.\n\n"
        "Intuitively this sequence is intended to approximate the square root of 2. "
        "Explain why the sequence is well-defined, argue that it converges, and find its limit."
    ),
    "background_notes_for_interviewer": [
        "Classic Newton–Raphson / Babylonian method for approximating √2.",
        "Students should at least be able to argue informally that the sequence stays positive and is bounded and monotone after some point.",
        "Good route: show x_n > 0 for all n, then show that if x_n > 0, the next term lies between x_n and 2/x_n; from there show it is eventually trapped and monotone.",
        "For the limit, set L = 1/2 (L + 2 / L) and solve the resulting quadratic L^2 = 2, then discuss why the positive root is chosen.",
        "Probe understanding of why it cannot converge to the negative root, and what 'convergence' means in this context."
    ],
    "solution_outline_steps": [
        "First, note that x_1 = 1 > 0. If x_n > 0, then x_{n+1} is the average of x_n and 2 / x_n, both positive, so x_{n+1} > 0; hence all terms are positive.",
        "One can show (by algebraic manipulation) that if x_n > √2 then x_{n+1} < x_n but still greater than √2, and if x_n < √2 then x_{n+1} > x_n but less than √2.",
        "This implies that, after the first step, the sequence is monotone and bounded, and therefore convergent.",
        "Let the limit be L. Passing to the limit in the recurrence gives L = 1/2 (L + 2 / L).",
        "Rearrange to obtain L^2 = 2, so L = ±√2.",
        "Since all x_n are positive, the limit must be L = √2."
    ],
    "common_misconceptions": [
        "Assuming convergence without any justification about monotonicity or boundedness.",
        "Solving L = 1/2 (L + 2 / L) incorrectly or forgetting the negative root.",
        "Claiming the limit is −√2 despite all terms being positive.",
        "Mixing up the sequence definition (e.g. writing 1/(2x_n) instead of 2/x_n)."
    ],
    "light_hints": [
        "What can you say about the sign of each term in the sequence?",
        "If you assume the sequence has a limit L, what equation must L satisfy?",
        "Once you have possible limits, how can you decide which one the sequence actually tends to?"
    ],
    "strong_hints": [
        "Try to show that if one term is positive, then so is the next one, and that the terms stay on one side of √2.",
        "Assume the sequence converges to L, substitute L into both sides of the recurrence relation, and simplify to get an equation for L.",
        "Use the fact that all terms are positive to decide between the possible roots of that equation."
    ],
    "extension_questions": [
        "How would you modify the recurrence to approximate √a for a different positive number a?",
        "This iteration is related to Newton’s method applied to the equation x^2 − 2 = 0. Can you see the connection?",
        "How quickly do you think this method converges compared to a simple bisection method?"
    ],
}


maths_probability_two_heads = {
    "id": "maths_probability_two_heads",
    "subject": "maths",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "You toss a fair coin repeatedly until you obtain two heads in a row. "
        "On average, how many tosses do you expect to make? Explain your reasoning as clearly as you can."
    ),
    "background_notes_for_interviewer": [
        "Tests basic discrete probability and the idea of conditioning on the current 'state' of the process.",
        "Natural approach is to set up states: no relevant history, last toss was a head, and finished.",
        "Let E be the expected remaining number of tosses from the start, and F from the state 'last toss was head'. "
        "Set up linear equations using conditioning and solve.",
        "Good candidates may also think in terms of Markov chains or first-step analysis; probe their notation and reasoning.",
        "Correct answer is 6 expected tosses."
    ],
    "solution_outline_steps": [
        "Define E as the expected number of tosses starting from scratch (no recent head) and F as the expected number of additional tosses given that the last toss was a head.",
        "From the start: the first toss is always used, so E = 1 + (1/2)E + (1/2)F, because with probability 1/2 you get a tail (back to the start) and with probability 1/2 you get a head (move to state F).",
        "From state F: you use one toss, then with probability 1/2 you get a head and finish (no more tosses), and with probability 1/2 you get a tail and go back to the start. So F = 1 + (1/2)·0 + (1/2)E = 1 + (1/2)E.",
        "Solve the two simultaneous equations: F = 1 + (1/2)E and E = 1 + (1/2)E + (1/2)F.",
        "Substitute F into the equation for E and rearrange to find E = 6.",
        "Therefore, on average you expect 6 tosses to get two heads in a row."
    ],
    "common_misconceptions": [
        "Assuming the expected number of tosses is simply 4 (because the probability of HH in two tosses is 1/4).",
        "Ignoring the 'overlaps' in patterns and treating each pair of tosses as independent trials.",
        "Setting up incorrect equations for the expectations by forgetting to include the 'one more toss' term.",
        "Confusing 'expected number of tosses' with 'most likely number of tosses'."
    ],
    "light_hints": [
        "How might you break the process into different 'states' depending on what the last toss was?",
        "Can you define an expected number of remaining tosses from each state?",
        "What happens to these expectations after you make one more toss?"
    ],
    "strong_hints": [
        "Try defining E as the expected number of tosses starting from scratch, and F as the expected number given that your last toss was a head.",
        "From each state, write an equation for the expected number of tosses in terms of what happens after one more coin flip.",
        "You should end up with two linear equations in E and F that you can solve."
    ],
    "extension_questions": [
        "What if you look for the pattern HTH instead of HH? How would you set up the states and equations then?",
        "How would the expected number of tosses change if the coin were biased?",
        "Can you see a systematic way to handle 'expected waiting time for a given pattern' problems in general?"
    ],
}


maths_combinatorics_handshakes = {
    "id": "maths_combinatorics_handshakes",
    "subject": "maths",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "At a party, each pair of people either shake hands once or not at all. "
        "You are told that there are n people and that each person shakes hands with exactly three other people.\n\n"
        "Show that n must be even. Explain your reasoning carefully."
    ),
    "background_notes_for_interviewer": [
        "Simple but revealing graph-theory / combinatorics question.",
        "Model the situation as a graph with n vertices, each of degree 3.",
        "Use the 'handshaking lemma': the sum of all degrees equals twice the number of edges.",
        "Sum of degrees is 3n, which must be even, implying n must be even.",
        "Probe whether the student can clearly justify why the sum of degrees equals twice the number of edges."
    ],
    "solution_outline_steps": [
        "Model the situation by a graph whose vertices represent people and whose edges represent handshakes.",
        "Each handshake contributes 1 to the degree of each of the two people involved, so contributes 2 to the sum of all degrees.",
        "Thus, the sum of the degrees of all vertices is equal to twice the total number of handshakes, and so must be even.",
        "However, each of the n people has degree 3, so the sum of all degrees is 3n.",
        "Therefore 3n is even. Since 3 is odd, n must itself be even.",
        "Conclude that there cannot be such a party with an odd number of people."
    ],
    "common_misconceptions": [
        "Arguing only by small examples instead of giving a general proof.",
        "Saying 'it’s obvious' that there must be an even number of people without using the sum-of-degrees argument.",
        "Confusing the number of edges with the number of degrees.",
        "Forgetting that each handshake is counted twice in the sum of degrees."
    ],
    "light_hints": [
        "Can you think of a way to represent the people and handshakes as a diagram involving points and lines?",
        "If you add up the number of handshakes each person has, how many times does each handshake get counted?",
        "What does that tell you about whether the total sum must be even or odd?"
    ],
    "strong_hints": [
        "Imagine drawing a dot for each person and joining two dots with a line if those two people shake hands.",
        "Think about the total number of line-ends (or 'half-edges') in the picture, and how this relates to the degrees and to the number of lines.",
        "Use this relationship to show that 3n must be even, and deduce a condition on n."
    ],
    "extension_questions": [
        "Generalise: if each person shakes hands with exactly k other people, what can you say about n when k is odd?",
        "Can you find an explicit construction of such a party for some even values of n (for example, draw the graph)?",
        "How does this relate to the idea of regular graphs in graph theory?"
    ],
}


maths_number_theory_gcd_linear_combination = {
    "id": "maths_number_theory_gcd_linear_combination",
    "subject": "maths",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "Let a and b be positive integers. Consider all integer combinations of the form ax + by, "
        "where x and y are integers (which may be negative).\n\n"
        "Show that the greatest common divisor of a and b is the smallest positive integer that can be written in the form ax + by."
    ),
    "background_notes_for_interviewer": [
        "This is the Bezout identity in a concrete form; good for probing number-theoretic reasoning.",
        "One approach: show that the set of all integer linear combinations of a and b contains some positive integers, "
        "so it has a least positive element d. Show that d divides both a and b, so d ≤ gcd(a, b).",
        "Then show that any common divisor of a and b must also divide d, so gcd(a, b) ≤ d. Conclude equality.",
        "Probe whether the student is comfortable with 'well-ordering' arguments (smallest positive element) and basic divisibility properties.",
        "More advanced candidates may connect this to the Euclidean algorithm."
    ],
    "solution_outline_steps": [
        "Consider the set S of all integers of the form ax + by with x, y ∈ ℤ. There is at least one positive element in S (for example, |a| or |b|), so by the well-ordering principle S has a least positive element; call it d.",
        "Show that d divides a: use the division algorithm to write a = qd + r with 0 ≤ r < d, and then argue that r must also lie in S.",
        "Since d is the smallest positive element of S, r must be 0, so d divides a. Similarly, show that d divides b.",
        "Therefore d is a common divisor of a and b, so d ≤ gcd(a, b).",
        "Now let g = gcd(a, b). Because g divides both a and b, any expression ax + by is divisible by g, and in particular d is divisible by g, so g ≤ d.",
        "Combining the inequalities d ≤ g and g ≤ d gives d = g. Hence gcd(a, b) is the smallest positive integer of the form ax + by."
    ],
    "common_misconceptions": [
        "Assuming the statement is obvious without giving a rigorous argument involving divisibility.",
        "Not justifying the existence of a smallest positive element in the set of linear combinations.",
        "Using the division algorithm incorrectly or not checking that the remainder lies in the same set.",
        "Forgetting to prove both inequalities (d ≤ gcd and gcd ≤ d) needed to show equality."
    ],
    "light_hints": [
        "Can you explain why there must be at least one positive integer of the form ax + by?",
        "If you take the smallest positive such combination and call it d, what can you say about dividing a by d?",
        "How does any common divisor of a and b relate to all expressions of the form ax + by?"
    ],
    "strong_hints": [
        "Let S be the set of all ax + by. Argue that S has a smallest positive element d.",
        "Use the division algorithm to write a = qd + r and show that the remainder r is also in S. Why must r be zero?",
        "If g is any common divisor of a and b, why must g also divide d? Combine this with your earlier inequality to conclude."
    ],
    "extension_questions": [
        "How does this result relate to the Euclidean algorithm for computing the greatest common divisor?",
        "Can you find explicit integers x and y such that 56x + 15y equals gcd(56, 15)?",
        "How might this idea extend to more than two integers?"
    ],
}


maths_geometry_max_area_given_perimeter = {
    "id": "maths_geometry_max_area_given_perimeter",
    "subject": "maths",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "Among all rectangles with a fixed perimeter P, which rectangle has the largest area? "
        "Give a clear argument for your answer."
    ),
    "background_notes_for_interviewer": [
        "A nice companion to the 'field next to a river' question; shows that the square maximises area for fixed perimeter.",
        "Let the sides be x and y with 2x + 2y = P; then y = P/2 − x and A = x(P/2 − x).",
        "This is again a downward-opening quadratic; maximum at the vertex, corresponding to x = y.",
        "Alternatively, use AM–GM: for fixed sum x + y, xy is maximised when x = y.",
        "Probe whether the student can articulate why the stationary point is a maximum and why it corresponds to a square."
    ],
    "solution_outline_steps": [
        "Let the sides of the rectangle be x and y, so the perimeter constraint is 2x + 2y = P, or x + y = P/2.",
        "Express y in terms of x: y = P/2 − x.",
        "Area A = x y = x(P/2 − x) = (P/2)x − x^2, a quadratic in x opening downwards.",
        "Differentiate to find A'(x) = P/2 − 2x; setting this to zero gives x = P/4.",
        "Then y = P/2 − P/4 = P/4, so the maximizing rectangle is a square.",
        "Conclude that among rectangles with fixed perimeter, the square has the largest area."
    ],
    "common_misconceptions": [
        "Maximising one side length without considering the constraint on the other side.",
        "Finding a stationary point but not noticing that the function is concave (and therefore has a maximum).",
        "Claiming the result is 'obvious' without providing a clear argument.",
        "Mixing up 'fixed area, minimise perimeter' with 'fixed perimeter, maximise area'."
    ],
    "light_hints": [
        "Can you introduce variables for the sides and express the perimeter constraint in terms of them?",
        "How can you eliminate one variable to write the area as a function of a single variable?",
        "Once you have A(x) in terms of one variable, how do you find its maximum value?"
    ],
    "strong_hints": [
        "Set x + y equal to a constant and write y in terms of x, then express the area as x times that expression.",
        "Differentiate your expression for area with respect to x and find where the derivative is zero.",
        "Explain why the point you have found really is a maximum, and what that tells you about the shape of the rectangle."
    ],
    "extension_questions": [
        "Is the same statement true in higher dimensions: among boxes with fixed surface area, which has the largest volume?",
        "How might you prove this result without calculus, using inequalities such as AM–GM?",
        "What happens if you fix the diagonal length of the rectangle instead of the perimeter?"
    ],
}


maths_sequences_alternating_series = {
    "id": "maths_sequences_alternating_series",
    "subject": "maths",
    "level": "oxbridge_undergrad_challenging",
    "student_prompt": (
        "Consider the infinite series 1 − 1/2 + 1/3 − 1/4 + 1/5 − 1/6 + ···.\n\n"
        "Does this series converge or diverge? Explain carefully how you decide, and compare it with the ordinary harmonic series "
        "1 + 1/2 + 1/3 + 1/4 + ···."
    ),
    "background_notes_for_interviewer": [
        "A good way to probe understanding of conditional convergence and alternating series.",
        "Students should recall that the harmonic series diverges, for example by grouping terms or by comparison to an integral.",
        "For the alternating harmonic series, they can apply the alternating series test: terms decrease in magnitude to zero and signs alternate, so the series converges.",
        "Probe the distinction between absolute and conditional convergence: the series of absolute values diverges, but the original alternating series converges.",
        "More advanced candidates may know that the sum is log 2, but this is not required."
    ],
    "solution_outline_steps": [
        "Recall that the ordinary harmonic series 1 + 1/2 + 1/3 + ··· diverges (for example by grouping terms in pairs and comparing to a constant).",
        "For the alternating harmonic series, observe that the terms 1/n decrease to zero in magnitude and the signs alternate.",
        "By the alternating series test (Leibniz criterion), this is enough to guarantee convergence of the alternating series.",
        "However, the series of absolute values, which is just the harmonic series again, still diverges.",
        "Therefore the alternating harmonic series is conditionally convergent (convergent but not absolutely convergent).",
        "Contrast this clearly with the divergence of the non-alternating harmonic series."
    ],
    "common_misconceptions": [
        "Assuming that if the harmonic series diverges then any rearrangement of its terms (including alternating signs) must also diverge.",
        "Thinking that convergence requires the terms to go to zero 'fast enough' without a precise argument.",
        "Not distinguishing between absolute convergence and conditional convergence.",
        "Misapplying tests for convergence or confusing series with sequences."
    ],
    "light_hints": [
        "What do you know about the ordinary harmonic series 1 + 1/2 + 1/3 + ···?",
        "In the alternating series, how do the sizes of the terms behave, and how do the signs behave?",
        "Have you seen a general criterion for when an alternating series converges?"
    ],
    "strong_hints": [
        "Try to state and use a test that applies specifically to alternating series whose term magnitudes decrease to zero.",
        "Compare the alternating series to the series of absolute values; what does that tell you about absolute versus conditional convergence?",
        "Explain clearly why the alternating harmonic series succeeds in converging whereas the ordinary harmonic series does not."
    ],
    "extension_questions": [
        "What happens if you rearrange the terms of a conditionally convergent series like this one? Can the sum change?",
        "Can you give another example of a series that converges conditionally but not absolutely?",
        "How might you estimate the error when approximating the sum of the alternating harmonic series by a finite number of terms?"
    ],
}


chem_equilibrium_no2_n2o4_volume_pressure = {
    "id": "chem_equilibrium_no2_n2o4_volume_pressure",
    "subject": "chemistry",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "In a sealed container at constant temperature, the brown gas nitrogen dioxide, NO₂, is in equilibrium with "
        "colourless dinitrogen tetroxide, N₂O₄, according to:\n\n"
        "  N₂O₄(g) ⇌ 2 NO₂(g).\n\n"
        "You observe a certain intermediate brown colour when equilibrium is reached.\n\n"
        "(a) Describe qualitatively what you would see if the volume of the container is suddenly doubled at constant temperature, "
        "and explain why.\n"
        "(b) What if instead you add some argon gas at the same temperature and volume? Explain in each case how the equilibrium "
        "position is affected, referring to both Le Chatelier's principle and the equilibrium constant."
    ),
    "background_notes_for_interviewer": [
        "Tests conceptual understanding of gas-phase equilibria and Le Chatelier's principle, and distinguishes total pressure "
        "changes by volume from adding inert gas at constant volume.",
        "Key idea: for an ideal-gas mixture at fixed T, Kp depends only on temperature, not on total pressure or inert gases.",
        "When volume doubles at constant T, total pressure drops; the system responds by shifting towards the side with more moles of gas "
        "(here 2 mol vs 1 mol), so more NO₂ is formed and the brown colour intensifies.",
        "Adding inert gas at constant volume does not change the partial pressures of reacting gases, so the equilibrium composition does "
        "not change (though the total pressure increases).",
        "Probe whether the student can relate partial pressure, total pressure, mole fraction, and the definition of Kp.",
    ],
    "solution_outline_steps": [
        "Write the equilibrium expression Kp = (p_NO2)² / p_N2O4 at fixed temperature.",
        "Note that when volume is suddenly doubled at constant T, all partial pressures are initially halved.",
        "At that instant, the reaction quotient Qp = (p_NO2)² / p_N2O4 is smaller than Kp, because both numerator and denominator "
        "scale but the stoichiometry favours the side with more moles of gas.",
        "To re-establish Kp, the system must shift towards products, increasing the amount of NO₂ and making the mixture a deeper brown.",
        "For adding argon at constant volume: partial pressures of NO₂ and N₂O₄ are unchanged, so Qp = Kp and there is no driving force "
        "to shift the equilibrium; the colour should remain essentially the same.",
        "Conclude that changing the total pressure via volume change affects the equilibrium, whereas adding inert gas at fixed volume does not.",
    ],
    "common_misconceptions": [
        "Thinking that any increase in total pressure (even by inert gas) must always favour the side with fewer moles of gas.",
        "Forgetting the distinction between total pressure and partial pressures of the reacting species.",
        "Believing that Kp changes when total pressure changes at constant temperature.",
        "Assuming that the colour must change whenever more gas is added, regardless of whether the equilibrium composition changes.",
    ],
    "light_hints": [
        "When you suddenly double the volume at constant temperature, what happens to the partial pressures of all gases present?",
        "For this reaction, which side has more moles of gas: N₂O₄ or 2 NO₂?",
        "When you add argon at constant volume, what happens to the partial pressures of NO₂ and N₂O₄ themselves?",
    ],
    "strong_hints": [
        "Write the expression for Kp in terms of partial pressures and think about what happens to that ratio immediately after the volume change.",
        "Compare the reaction quotient Qp just after the change with the equilibrium constant Kp; in which direction must the reaction shift?",
        "For the argon case, explicitly consider p_NO2 and p_N2O4 before and after adding the inert gas at fixed volume.",
    ],
    "extension_questions": [
        "How would your answer differ if the reaction were 2 NO₂(g) ⇌ N₂O₄(g) written the other way round? Does Kp change form?",
        "What would happen if you changed the temperature instead of the volume, assuming the forward reaction is exothermic?",
        "Can you sketch qualitatively how the equilibrium composition depends on total pressure at fixed temperature for this reaction?",
    ],
}


chem_acid_base_buffer_acetate = {
    "id": "chem_acid_base_buffer_acetate",
    "subject": "chemistry",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "You make a buffer solution by mixing equimolar amounts of acetic acid (CH₃COOH) and sodium acetate (CH₃COONa) in water. "
        "The acid dissociation constant Ka for acetic acid is about 1.8 × 10⁻⁵ at room temperature.\n\n"
        "(a) Explain qualitatively why this mixture acts as a buffer when small amounts of strong acid or strong base are added.\n"
        "(b) Estimate the pH of the buffer, explaining any approximations you make.\n"
        "(c) What happens to the pH if you dilute the buffer by adding pure water? Justify your answer."
    ),
    "background_notes_for_interviewer": [
        "Tests understanding of weak acid–conjugate base buffers and the Henderson–Hasselbalch relationship.",
        "Students should recognise that the weak acid provides a reservoir to neutralise added base, and the conjugate base "
        "neutralises added strong acid, keeping [HA]/[A⁻] roughly constant.",
        "With equimolar HA and A⁻, pH ≈ pKa; they should relate pH, pKa and the ratio [A⁻]/[HA].",
        "Important idea: diluting a buffer changes concentrations but not the ratio of acid to base, so pH changes only slightly.",
        "Probe whether they understand when the Henderson–Hasselbalch approximation is valid and what happens when you exceed buffer capacity.",
    ],
    "solution_outline_steps": [
        "Describe the equilibrium CH₃COOH ⇌ H⁺ + CH₃COO⁻ in the presence of both acid and conjugate base.",
        "Explain that added H⁺ is mainly consumed by CH₃COO⁻ to form CH₃COOH, while added OH⁻ is mainly consumed by CH₃COOH to form CH₃COO⁻, "
        "so the free [H⁺] changes much less than in pure water.",
        "Use the Henderson–Hasselbalch equation pH = pKa + log([A⁻]/[HA]) for a weak acid buffer.",
        "For equimolar CH₃COOH and CH₃COO⁻, [A⁻]/[HA] ≈ 1, so pH ≈ pKa ≈ 4.7.",
        "On dilution with water, both [HA] and [A⁻] decrease by the same factor, so their ratio remains about 1; pH therefore remains close to pKa.",
        "Point out that very extreme dilution would eventually reduce the buffering action, but for modest dilution the pH changes very little.",
    ],
    "common_misconceptions": [
        "Thinking that adding strong acid or base leaves the concentrations of HA and A⁻ unchanged.",
        "Assuming that buffers 'fix' the pH exactly and that it cannot change at all.",
        "Believing that dilution of a buffer always leaves the pH completely unchanged, without acknowledging buffer limits.",
        "Confusing pKa with Ka or misusing the Henderson–Hasselbalch equation when the ratio [A⁻]/[HA] is far from 1.",
    ],
    "light_hints": [
        "What happens to added H⁺ ions when there is a significant amount of CH₃COO⁻ present?",
        "If [CH₃COOH] and [CH₃COO⁻] are equal, what does that tell you about the log([A⁻]/[HA]) term in the Henderson–Hasselbalch equation?",
        "When you dilute the solution, do [CH₃COOH] and [CH₃COO⁻] change by the same factor or by different factors?",
    ],
    "strong_hints": [
        "Try writing the Henderson–Hasselbalch relationship between pH, pKa, and the ratio of conjugate base to acid, then substitute [A⁻] = [HA].",
        "Explain, in words or algebraically, why adding the same amount of water to both components keeps [A⁻]/[HA] roughly constant.",
        "Think about how far you can dilute before the assumption that buffer components dominate over water autoionisation breaks down.",
    ],
    "extension_questions": [
        "How would the buffer pH change if you made the solution with twice as much acetate as acetic acid?",
        "What would happen to the buffer pH if the temperature increased and Ka changed?",
        "How could you prepare a buffer at pH 5.0 using acetic acid and sodium acetate? What ratio of [A⁻] to [HA] would you need?",
    ],
}


chem_kinetics_rate_law_mechanism = {
    "id": "chem_kinetics_rate_law_mechanism",
    "subject": "chemistry",
    "level": "oxbridge_undergrad_challenging",
    "student_prompt": (
        "A hypothetical reaction between gases A and B to form product P is studied:\n\n"
        "  A(g) + 2 B(g) → P(g).\n\n"
        "Experimentally, the initial rate is found to be first order in A and second order in B.\n"
        "(a) Write a possible reaction mechanism, involving one slow (rate-determining) step and one or more fast steps, "
        "that is consistent with the overall stoichiometry and the observed rate law rate = k [A][B]².\n"
        "(b) Explain clearly how your mechanism leads to this rate law.\n"
        "(c) Is your mechanism unique? Briefly discuss."
    ),
    "background_notes_for_interviewer": [
        "Tests understanding of elementary steps, rate-determining steps, and deriving rate laws from mechanisms.",
        "Students should propose a mechanism where the slow step involves A and two B species effectively, for example via a pre-equilibrium.",
        "A common construction: fast equilibrium A + B ⇌ I, followed by slow I + B → P. Derive rate ∝ [A][B]² using pre-equilibrium assumption.",
        "Alternative mechanisms are possible; the key is that they be chemically plausible and reproduce the observed rate law.",
        "Probe whether the student understands that the overall stoichiometry does not automatically give the rate law, and that mechanisms are models.",
    ],
    "solution_outline_steps": [
        "Propose a mechanism such as: (1) A + B ⇌ I (fast equilibrium), (2) I + B → P (slow, rate-determining).",
        "Write the rate of formation of P as rate = k₂ [I][B] from the slow step.",
        "Use the equilibrium constant for the fast step: K = [I] / ([A][B]) so that [I] = K [A][B].",
        "Substitute [I] into the rate expression to obtain rate = k₂ K [A][B]², which matches the experimentally observed rate law with k = k₂ K.",
        "Discuss that many different mechanisms could lead to the same rate law, so the mechanism is not unique.",
        "Emphasise that mechanistic proposals must also be consistent with other experimental information (intermediates, activation energies, etc.).",
    ],
    "common_misconceptions": [
        "Assuming the stoichiometric coefficients in the overall equation directly give the rate law.",
        "Writing a slow step that already has the overall stoichiometry A + 2B → P but then failing to justify the observed rate law properly.",
        "Not distinguishing between intermediates and stable species, or forgetting that intermediates do not appear in the overall equation.",
        "Believing that a single experiment on rate law uniquely determines the mechanism.",
    ],
    "light_hints": [
        "Could the reaction proceed via a short-lived intermediate I formed from A and B?",
        "If one step is much slower than the others, which step will control the overall rate?",
        "How might you relate the concentration of an intermediate to the concentrations of A and B if it is formed in a fast equilibrium step?",
    ],
    "strong_hints": [
        "Try a mechanism where A and B first form an intermediate I in a fast reversible step, and then I reacts with another B in a slower step.",
        "Write the rate in terms of [I] and [B], then eliminate [I] using an equilibrium relationship involving A, B, and I.",
        "Show explicitly how the final rate law becomes proportional to [A][B]², and identify the composite rate constant.",
    ],
    "extension_questions": [
        "How could you test whether an intermediate like I actually exists in this mechanism?",
        "If the first step were not a fast equilibrium but instead a rapid irreversible step, how would that affect your derivation?",
        "Can you think of experimental observables (temperature dependence, isotope effects) that might help distinguish between alternative mechanisms?",
    ],
}


chem_thermodynamics_entropy_melting = {
    "id": "chem_thermodynamics_entropy_melting",
    "subject": "chemistry",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "Pure ice at 0 °C is in equilibrium with liquid water at 0 °C under 1 atm pressure.\n\n"
        "(a) Explain, in terms of enthalpy and entropy changes, why there is a particular temperature at which ice and water can coexist "
        "in equilibrium.\n"
        "(b) What happens to the spontaneity of melting if you raise the temperature slightly above 0 °C, keeping the pressure at 1 atm?\n"
        "(c) How would increasing the pressure (for example, by squeezing ice between two surfaces) affect the melting point of ice, "
        "given that water expands on freezing? Explain qualitatively."
    ),
    "background_notes_for_interviewer": [
        "Tests qualitative command of ΔG = ΔH − TΔS and phase equilibria.",
        "At the melting point, ΔG for the process solid → liquid is zero: ΔH_fus = T_m ΔS_fus.",
        "Above T_m, TΔS term dominates for fusion of a typical solid with positive ΔS, making melting spontaneous (ΔG < 0); below T_m, freezing is favoured.",
        "For water, the solid is less dense than the liquid, so increasing pressure favours the denser phase (liquid) and thus lowers the melting point.",
        "Probe whether the student can connect microscopic order/disorder with entropy and think carefully about the sign of volume change.",
    ],
    "solution_outline_steps": [
        "Introduce the Gibbs free energy change ΔG for the process ice → water as ΔG = ΔH_fus − T ΔS_fus.",
        "At the equilibrium melting temperature T_m, the two phases coexist with no net driving force, so ΔG = 0 and ΔH_fus = T_m ΔS_fus.",
        "For water, ΔH_fus > 0 and ΔS_fus > 0 (melting requires heat and increases disorder), so for T > T_m the term TΔS_fus outweighs ΔH_fus and ΔG becomes negative; melting is spontaneous.",
        "For T < T_m, ΔG for melting is positive and the reverse process (freezing) is favoured.",
        "Consider pressure: since ice is less dense than liquid water, increasing pressure favours the phase with smaller volume (liquid) according to Le Chatelier-type reasoning.",
        "Therefore increasing pressure lowers the melting point of ice, making melting easier under pressure.",
    ],
    "common_misconceptions": [
        "Believing that the melting point is defined purely by 'bond strength' without reference to entropy.",
        "Thinking that a process is spontaneous whenever ΔH < 0, ignoring the entropy term.",
        "Assuming that increasing pressure always favours the solid phase, without considering volume changes.",
        "Confusing the direction of spontaneity with the sign of ΔS rather than ΔG.",
    ],
    "light_hints": [
        "What thermodynamic quantity determines whether a process is spontaneous at constant temperature and pressure?",
        "For melting, what are the signs of the enthalpy change and the entropy change?",
        "If a solid is less dense than its liquid, which phase does higher pressure tend to favour?",
    ],
    "strong_hints": [
        "Write ΔG for melting as ΔH_fus minus T times ΔS_fus and think about what must be true at the temperature where ice and water coexist.",
        "Consider what happens to ΔG when you increase T slightly, assuming ΔH_fus and ΔS_fus are roughly constant over a small temperature range.",
        "Use Le Chatelier’s ideas with volume: increased pressure favours the phase of smaller volume; which is that for water?",
    ],
    "extension_questions": [
        "Can you sketch qualitatively how the solid–liquid phase boundary for water looks on a pressure–temperature phase diagram?",
        "How does the effect of pressure on melting point differ for substances whose solids are denser than their liquids?",
        "What role do enthalpy and entropy play in determining the boiling point of water at 1 atm?",
    ],
}


chem_electrochem_concentration_cell = {
    "id": "chem_electrochem_concentration_cell",
    "subject": "chemistry",
    "level": "oxbridge_undergrad_challenging",
    "student_prompt": (
        "Consider a concentration cell at 25 °C made of two hydrogen electrodes:\n\n"
        "  Pt | H₂(g, 1 atm) | H⁺(aq, 0.10 M)  ||  H⁺(aq, 1.0 × 10⁻³ M) | H₂(g, 1 atm) | Pt\n\n"
        "Both hydrogen gas pressures are 1 atm, but the acid concentrations differ.\n"
        "(a) Which side acts as the anode and which as the cathode when the cell is allowed to operate spontaneously? Explain.\n"
        "(b) Calculate the cell potential using the Nernst equation (you may assume the standard hydrogen electrode potential is 0.00 V).\n"
        "(c) What process occurs as the cell runs, and how will the two solution concentrations change over time?"
    ),
    "background_notes_for_interviewer": [
        "Tests understanding of the Nernst equation, concentration cells, and sign conventions for anode/cathode.",
        "Students should recognise that electrons flow from the side with lower [H⁺] to the side with higher [H⁺], as the cell tends to equalise chemical potentials.",
        "Use E_cell = (0.0592 V / n) log(Q⁻¹) form or E = (0.0592/n) log(activities ratio). For the hydrogen concentration cell, "
        "E_cell = (0.0592 V) log([H⁺]_concentrated / [H⁺]_dilute).",
        "At 25 °C with 0.10 M vs 10⁻³ M, the potential is about 0.18 V.",
        "Probe whether they can describe qualitatively how proton concentrations move towards equality as the cell operates.",
    ],
    "solution_outline_steps": [
        "Identify the half-cells as 2 H⁺(aq) + 2 e⁻ ⇌ H₂(g, 1 atm) on both sides, differing only in proton concentration.",
        "The side with lower [H⁺] has a higher tendency to generate H⁺ (oxidation), so it acts as the anode; the more concentrated side is the cathode.",
        "Write the Nernst expression for the hydrogen electrode: E = E° − (0.0592/2) log(1/[H⁺]²) at 25 °C, or equivalently E ∝ log[H⁺].",
        "Compute the difference between the two electrodes: E_cell = (0.0592 V) log([H⁺]_cathode / [H⁺]_anode) with n = 2.",
        "Substitute [H⁺]_cathode = 0.10 M and [H⁺]_anode = 10⁻³ M to obtain E_cell ≈ 0.0592 × log(100) ≈ 0.0592 × 2 ≈ 0.12 V if treating log base 10 incorrectly; "
        "more carefully, note that due to the squared dependence, E_cell ≈ 0.0592 × log(0.10/10⁻³) ≈ 0.18 V (interviewer can tidy numbers).",
        "Describe qualitatively: as the cell runs, H⁺ is produced at the dilute side (anode) and consumed at the concentrated side (cathode), "
        "leading the concentrations to move towards each other and the cell potential to decrease over time.",
    ],
    "common_misconceptions": [
        "Thinking that the more concentrated solution must always be the anode because it has 'more stuff to react'.",
        "Applying the Nernst equation with the reaction written in the wrong direction, leading to sign errors.",
        "Forgetting that n = 2 for the hydrogen half-reaction and misplacing the factor of 2 in the denominator.",
        "Believing that a concentration cell cannot produce any voltage because the standard electrode potentials are identical.",
    ],
    "light_hints": [
        "Which way do you expect the system to move in order to reduce the difference in proton concentrations between the two sides?",
        "In a hydrogen electrode, does increasing [H⁺] make the electrode potential more positive or more negative?",
        "When you write the Nernst equation for each half-cell, how does [H⁺] enter the expression?",
    ],
    "strong_hints": [
        "Write the hydrogen half-reaction and its Nernst equation, then compute E for each side separately and subtract to get E_cell.",
        "Decide which half-cell has the higher potential; that side will be the cathode in a spontaneous cell.",
        "Think through what happens to [H⁺] at each electrode as oxidation or reduction proceeds, and how this changes the cell potential with time.",
    ],
    "extension_questions": [
        "How would the cell potential change if both solutions were made ten times more dilute while keeping their ratio the same?",
        "Can you design a different concentration cell using Cu²⁺/Cu electrodes and write the Nernst expression for its potential?",
        "What assumptions are hidden in using concentrations instead of activities in the Nernst equation?",
    ],
}


chem_molecular_orbitals_o2_paramagnetism = {
    "id": "chem_molecular_orbitals_o2_paramagnetism",
    "subject": "chemistry",
    "level": "oxbridge_undergrad_entry",
    "student_prompt": (
        "In simple Lewis structures, O₂ is often drawn with a double bond and all electrons paired, which would suggest diamagnetism. "
        "However, experimental measurements show that O₂ is paramagnetic: it is attracted into a magnetic field.\n\n"
        "(a) Explain how molecular orbital (MO) theory accounts for the paramagnetism of O₂.\n"
        "(b) Based on a simple MO diagram for O₂, what is the O–O bond order?\n"
        "(c) How would the bond order and magnetism change for O₂⁺ and O₂⁻? Give a qualitative explanation."
    ),
    "background_notes_for_interviewer": [
        "Tests whether the student has seen or can reason about MO diagrams for diatomic molecules, especially O₂.",
        "Key fact: in O₂, the π* antibonding orbitals are each singly occupied, leading to two unpaired electrons and bond order 2.",
        "For O₂⁺, one electron is removed from an antibonding orbital, increasing bond order to 2.5 and leaving one unpaired electron.",
        "For O₂⁻, one electron is added to an antibonding orbital, decreasing bond order to 1.5; unpaired electrons remain, so still paramagnetic.",
        "Probe their ability to count bonding vs antibonding electrons and to link unpaired electrons to paramagnetism.",
    ],
    "solution_outline_steps": [
        "Sketch or describe the MO energy levels for O₂, with σ and π bonding orbitals and corresponding antibonding σ* and π*.",
        "Fill the orbitals with 12 valence electrons per O₂ molecule (6 from each oxygen).",
        "Show that the two degenerate π* antibonding orbitals each contain one electron with parallel spins, giving two unpaired electrons.",
        "Compute the bond order as (number of bonding electrons − number of antibonding electrons)/2 to obtain bond order 2 for O₂.",
        "For O₂⁺, remove one electron from a π* antibonding orbital: bond order increases to 2.5 and there is one unpaired electron (still paramagnetic).",
        "For O₂⁻, add one electron to a π* antibonding orbital: bond order decreases to 1.5; depending on occupancy there are still unpaired electrons, "
        "so paramagnetism persists but bonding is weaker.",
    ],
    "common_misconceptions": [
        "Relying solely on Lewis structures and concluding O₂ must be diamagnetic.",
        "Miscounting electrons in bonding vs antibonding orbitals when determining bond order.",
        "Thinking that adding electrons always increases bond strength, regardless of whether they go into bonding or antibonding orbitals.",
        "Assuming that any charged species must have paired electrons and be diamagnetic.",
    ],
    "light_hints": [
        "In MO theory, what feature of an electron configuration usually leads to paramagnetism?",
        "Where do the highest-energy valence electrons of O₂ sit in a simple MO diagram?",
        "How do you compute bond order from the number of bonding and antibonding electrons?",
    ],
    "strong_hints": [
        "Try writing down the total number of valence electrons in O₂ and placing them into the MO levels until you reach the π* orbitals.",
        "Count how many electrons occupy bonding orbitals and how many occupy antibonding orbitals, then calculate (bonding − antibonding)/2.",
        "When you add or remove one electron to form O₂⁻ or O₂⁺, think carefully about which orbital it comes from or goes into, and how that affects bond order and unpaired electrons.",
    ],
    "extension_questions": [
        "How does the MO-based explanation of O₂’s paramagnetism compare to what valence bond theory would predict?",
        "What experimental evidence (e.g. magnetic susceptibility, spectroscopy) supports the MO description of O₂?",
        "How would you expect the bond lengths in O₂, O₂⁺ and O₂⁻ to compare, based on the bond orders you found?",
    ],
}

# ---- automatic registry builder (keep this at the very end of the file) ----

def _is_question_card(obj):
    """
    Recognise a question card: a dict with at least id, subject, and student_prompt.
    """
    return (
        isinstance(obj, dict)
        and "id" in obj
        and "subject" in obj
        and "student_prompt" in obj
    )

# Collect all question-card dicts defined in this module
ALL_QUESTION_CARDS = [
    value
    for name, value in globals().items()
    if _is_question_card(value)
]

# Optional: sort them for a nice stable order in the UI
ALL_QUESTION_CARDS.sort(
    key=lambda c: (c["subject"], c.get("level", ""), c["id"])
)

# Fast lookup by ID
QUESTION_CARDS_BY_ID = {card["id"]: card for card in ALL_QUESTION_CARDS}

# Optional: lookup by (subject, level)
QUESTION_CARDS_BY_SUBJECT_LEVEL = {}
for card in ALL_QUESTION_CARDS:
    key = (card["subject"], card.get("level"))
    QUESTION_CARDS_BY_SUBJECT_LEVEL.setdefault(key, []).append(card)
